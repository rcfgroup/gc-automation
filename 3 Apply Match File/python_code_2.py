from pathlib import Path
import subprocess
import click
import pandas
import os

def compare_match(date, tray, filepath):
    f_date, f_tray, *_ = filepath.split(" ")
    return f_date == date and f_tray == tray


@click.command()
@click.option('--image', type=click.Path(exists=True, file_okay=False, dir_okay=True), help='image directory')
@click.option('--match', type=click.Path(exists=True, file_okay=False, dir_okay=True), help='extracted match directory')
@click.option('--report', type=click.Path(exists=True, file_okay=False, dir_okay=True), help='directory to save summary report')
@click.option('--export', type=click.Path(exists=True, file_okay=False, dir_okay=True), help='directory to export TIC as CSV')
@click.option('--output', type=click.Path(exists=True, file_okay=False, dir_okay=True), help='directory to save aligned image')
@click.option('--nomatch', type=click.Path(exists=False, file_okay=True), help='log if not match file exists')
def cli(image, match, report, export, output, nomatch):
    no_match_list = list()
    matches = [os.path.abspath(x) for x in list(Path(match).glob("*.csv"))]
    images = [os.path.abspath(x) for x in list(Path(image).glob("*.gci"))]
    report = os.path.abspath(report)
    export = os.path.abspath(export)
    output = os.path.abspath(output)
    nomatch = os.path.abspath(nomatch)

    for img in images:
        image_name = os.path.basename(img)
        print("Processing image [{}]".format(image_name))
        date, tray, *_ = image_name.split(" ")
        match_list = [m for m in matches if compare_match(date, tray, os.path.basename(m))]
        match_file = match_list[0] if match_list else None
        if match_file:
            print("Using exported match [{}]".format(os.path.basename(match_file)))
            with open("process_base.cmd", 'r') as process_base_file:
                process_base = process_base_file.read()
                with open("process.cmd", "w+") as process_file:
                    process = process_base.replace("$$MATCH_FILE$$", match_file).replace("$$EXPORT_DIR$$", str(export)).replace("$$REPORT_DIR$$", str(report))
                    process_file.write(process)
            cmd = "\"C:\\GC Image\\GC Image 2.8r2 GCxGC (64-bit)\\bin\\CommandLine.bat\" -sysu -cmdFile \"C:\\temp\\Example folders\\3 Apply Match File\\process.cmd\" -s \"{}\" -d \"{}\\{}\" 2>&1 1>nul | more".format(img, output, image_name)
            proc = subprocess.Popen(cmd, shell=True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding='utf8')
            stdout, stderr = proc.communicate(cmd)
            print("=====output=====")
            print(stdout)
            print("=====error=====")
            print(stderr)
        else:
            print("Cannot find match. Skipping.")
            no_match_list.append(
                {
                    "image": image_name,
                    "date": date,
                    "tray": tray
                }
            )
    if len(no_match_list) > 0:
        df = pandas.DataFrame(no_match_list)
        df.to_csv(nomatch, header=True, index=False)


if __name__ == '__main__':
    cli()