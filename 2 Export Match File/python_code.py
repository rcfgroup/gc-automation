import glob
import os
from xml.dom import minidom
"""
Please run `pip install click pandas` before using this script
"""
import click
import pandas

"""
Run the command below to see help information, or see cli function
python python_code.py --help
"""


def get_reports(input_path: str):
    """return list of csv files"""
    gci_path_pattern = os.path.join(input_path, '*.csv')
    return glob.glob(gci_path_pattern)


def parse_template(template_path: str):
    """return list of peak name, firstcol and secondcol from the template"""
    doc = minidom.parse(template_path)
    peaks = doc.getElementsByTagName('peak')
    results = list()
    for peak in peaks:
        results.append({
            'compound': peak.getElementsByTagName('compound')[0].firstChild.data,
            'first': float(peak.getElementsByTagName('peakfirstcol')[0].firstChild.data),
            'second': float(peak.getElementsByTagName('peaksecondcol')[0].firstChild.data)
        })
    print(results)
    return results


def parse_report(csv_path: str):
    """return list of blob name, firstcol and secondcol from the combined table csv"""
    basename = os.path.basename(csv_path)
    print(basename)
    # if the report csv file structure has changed, edit skiprows
    df = pandas.read_csv(csv_path, skiprows=33)
    df_not_matched = None
    print(df)
    blobs = list()
    for index, row in df.iterrows():
        print(row)
        if row['Template'] == 'Template Peaks Not Matched':
            df_not_matched = pandas.read_csv(csv_path, skiprows=33+index+4)
            break
        if not pandas.isna(row['Template']):
            blobs.append({
                'compound': row['Blob'],
                'first': row['Blob.1'],
                'second': row['Blob.2']
            })
    print(blobs)
    not_match = list()
    if df_not_matched is not None:
        print(df_not_matched)
        for index, row in df_not_matched.iterrows():
            print(row)
            not_match.append({
                'file': basename,
                'compound': row['Name'],
                'rt1': row['RT1'],
                'rt2': row['RT2'],
                'clic': row['Qualifier CLIC'],
                'desc': row['Match Description']
            })
    return blobs, basename, not_match


def match_template(blobs, templates):
    """return list of matched template and blob"""
    results = list()
    for blob in blobs:
        template = next(t for t in templates if t['compound'] == blob['compound'])
        results.append({
            't1': template['first'],
            't2': template['second'],
            'b1': blob['first'],
            'b2': blob['second']
        })
    print(results)
    return results


def write_csv(csv_data, csv_path, header=False):
    """write matched template and blob to csv file"""
    df = pandas.DataFrame(csv_data)
    df.to_csv(csv_path, header=header, index=False)


@click.command()
@click.option('--template', type=click.Path(exists=True, file_okay=True, dir_okay=False), help='template file')
@click.option('--source', type=click.Path(exists=True, file_okay=True, dir_okay=True), help='single csv file or directory that contains multiple csv file')
@click.option('--destination', type=click.Path(exists=True, file_okay=False, dir_okay=True), help='destination directory to save template match csv file')
def cli(source, template, destination):
    templates = parse_template(template)
    csv_files = list()
    if os.path.isdir(source):
        csv_files = get_reports(source)
    elif os.path.isfile(source):
        csv_files.append(source)
    not_match_report = list()
    for csv_report in csv_files:
        blobs, csv_basename, not_match = parse_report(csv_report)
        not_match_report.extend(not_match)
        """edit _Combined_Tables.csv to make it match your csv filename pattern """
        if '_Combined_Tables.csv' in csv_basename:
            """edit _Template_Match.csv to make your csv filename pattern """
            new_csv_basename = csv_basename.replace('_Combined_Tables.csv', '_Template_Match.csv')
        else:
            """edit _Template_Match.csv to make your csv filename pattern """
            new_csv_basename = csv_basename.replace('.csv', '_Template_Match.csv')
        csv_data = match_template(blobs, templates)
        csv_path = os.path.join(destination, new_csv_basename)
        write_csv(csv_data, csv_path)
    if len(not_match_report):
        write_csv(not_match_report, os.path.join(destination, 'Template Not Matched.csv'), header=True)


if __name__ == '__main__':
    cli()
