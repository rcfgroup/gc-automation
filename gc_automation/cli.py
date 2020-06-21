import subprocess
from pathlib import Path

import click
import pandas
from rich.console import Console

from gc_image import GCIProcessCmd, GCIProcessChildCmd, GCICmdParameter, process_image
from utils import (
    parse_template,
    get_reports,
    parse_report,
    match_template,
    write_csv,
    compare_match,
)


@click.group()
def cli():
    pass


@cli.command(name="align")
@click.option(
    "--gci",
    "-g",
    "gci_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True),
    prompt=True,
    help="Path to GC Image CommandLine.bat file",
)
@click.option(
    "--method",
    "-m",
    "method",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True),
    prompt=True,
    help="Path to process method cmd file",
)
@click.option(
    "--source",
    "-s",
    "source",
    type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True),
    prompt=True,
    help="Path to source image(s), can be a single image file or a directory which contains one or more image files",
)
@click.option(
    "--output",
    "-o",
    "output",
    type=click.Path(exists=False, file_okay=False, dir_okay=True, writable=True),
    prompt=True,
    help="Path to output directory, this is where processed images will be saved",
)
@click.option(
    "--export",
    "-e",
    "export",
    type=click.Path(exists=False, file_okay=False, dir_okay=True, writable=True),
    prompt=True,
    help="Path to export directory, this is where exported csv files will be saved",
)
@click.option(
    "--log",
    "-l",
    "log",
    type=click.Path(exists=False, file_okay=True, dir_okay=False, writable=True),
    prompt=True,
    help="Path to where logs will be saved",
)
def align(gci_path, method, source, output, export, log):
    console = Console()
    source_path = Path(source)
    output_path = Path(output)
    export_path = Path(export)
    log_path = Path(log)
    if source_path.is_file():
        process_image(
            gci_path,
            method,
            str(source_path.absolute()),
            str(output_path.absolute()),
            str(export_path.absolute()),
            str(log_path.absolute()),
        )
    else:
        source_files = list(source_path.glob("**/*.gci"))
        console.print(
            f"{len(source_files)} found in source directory", style="bold green"
        )
        for source_file in source_files:
            process_image(
                gci_path, method, source_file, output_path, export_path, log_path
            )


@cli.command(name="method")
@click.option(
    "--output",
    "-o",
    "output",
    type=click.Path(exists=False),
    prompt="Please specifiy a path where this new method will be saved",
    help="Path to method cmd file, this is where generated method cmd file will be saved",
)
def create_method(output):
    if not output:
        return
    console = Console()
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = GCIProcessCmd(
        configure=click.prompt(
            "GC Image configuration file:",
            type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True),
        )
    )
    console.print("Now start adding some command to this method", style="bold cyan")
    console.print("Your method need to include as least one command", style="bold red")
    while True:
        child_cmd = GCIProcessChildCmd(
            name=click.prompt("Command identifier"), label=click.prompt("Command name")
        )
        if click.confirm("Add parameter for this command?"):
            while True:
                param = GCICmdParameter(
                    cmd_id=click.prompt("Parameter identifier"),
                    label=click.prompt("Parameter name"),
                    value=click.prompt("Parameter value"),
                )
                child_cmd.parameters.append(param)
                if not click.confirm("Add another parameter?"):
                    break
        cmd.child_cmd.append(child_cmd)
        if not click.confirm("Add another command?"):
            break
    console.print("Generating method cmd file...", style="bold cyan")
    cmd.to_cmd(output_path)
    console.print("Done!", style="bold green")
    console.print(
        f"Your generated method cmd file is: {str(output_path.absolute())}",
        style="bold green",
    )


@cli.command(name="templatematch")
@click.option(
    "--template",
    "-t",
    "template",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    help="template file",
)
@click.option(
    "--source",
    "-s",
    "source",
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    help="single csv file or directory that contains multiple csv file",
)
@click.option(
    "--destination",
    "-d",
    "dest",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="destination directory to save template match csv file",
)
def template_match(source, template, dest):
    templates = parse_template(template)
    csv_files = list()
    if Path(source).is_dir():
        csv_files = get_reports(source)
    elif Path(source).is_file():
        csv_files.append(source)
    not_match_report = list()
    for csv_report in csv_files:
        blobs, csv_basename, not_match = parse_report(csv_report)
        not_match_report.extend(not_match)
        """edit _Combined_Tables.csv to make it match your csv filename pattern """
        if "_Combined_Tables.csv" in csv_basename:
            """edit _Template_Match.csv to make your csv filename pattern """
            new_csv_basename = csv_basename.replace(
                "_Combined_Tables.csv", "_Template_Match.csv"
            )
        else:
            """edit _Template_Match.csv to make your csv filename pattern """
            new_csv_basename = csv_basename.replace(".csv", "_Template_Match.csv")
        csv_data = match_template(blobs, templates)
        csv_path = Path(dest).joinpath(new_csv_basename)
        write_csv(csv_data, csv_path)
    if len(not_match_report):
        write_csv(
            not_match_report,
            Path(dest).joinpath("Template Not Matched.csv"),
            header=True,
        )


@cli.command()
@click.option(
    "--images",
    "-i",
    "images",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="image directory",
)
@click.option(
    "--match",
    "-m",
    "match",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="extracted match directory",
)
@click.option(
    "--report",
    "-r",
    "report",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="directory to save summary report",
)
@click.option(
    "--export",
    "-e",
    "export",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="directory to export TIC as CSV",
)
@click.option(
    "--output",
    "-o",
    "output",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="directory to save aligned image",
)
@click.option(
    "--nomatch",
    "-nm",
    "nomatch",
    type=click.Path(exists=False, file_okay=True),
    help="log if not match file exists",
)
def cli(image, match, report, export, output, nomatch):
    no_match_list = list()
    matches = [x for x in list(Path(match).glob("*.csv"))]
    images = [x for x in list(Path(image).glob("*.gci"))]
    report = Path(report).absolute()
    export = Path(export).absolute()
    output = Path(output).absolute()
    nomatch = Path(nomatch).absolute()

    for img in images:
        image_name = img.name
        print("Processing image [{}]".format(image_name))
        date, tray, *_ = image_name.split(" ")
        match_list = [m for m in matches if compare_match(date, tray, m.name)]
        match_file = match_list[0] if match_list else None
        if match_file:
            print("Using exported match [{}]".format(str(match_file.name)))
            with open("process_base.cmd", "r") as process_base_file:
                process_base = process_base_file.read()
                with open("process.cmd", "w+") as process_file:
                    process = (
                        process_base.replace(
                            "$$MATCH_FILE$$", str(match_file.absolute())
                        )
                        .replace("$$EXPORT_DIR$$", str(export))
                        .replace("$$REPORT_DIR$$", str(report))
                    )
                    process_file.write(process)
            cmd = '"C:\\GC Image\\GC Image 2.8r2 GCxGC (64-bit)\\bin\\CommandLine.bat" -sysu -cmdFile C:\\temp\\meow\\process.cmd -s "{}" -d "{}\\{}" 2>&1 1>nul | more'.format(
                img, output, image_name
            )
            proc = subprocess.Popen(
                cmd,
                shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                encoding="utf8",
            )
            stdout, stderr = proc.communicate(cmd)
            print("=====output=====")
            print(stdout)
            print("=====error=====")
            print(stderr)
        else:
            print("Cannot find match. Skipping.")
            no_match_list.append({"image": image_name, "date": date, "tray": tray})
    if len(no_match_list) > 0:
        df = pandas.DataFrame(no_match_list)
        df.to_csv(nomatch, header=True, index=False)


if __name__ == "__main__":
    cli()
