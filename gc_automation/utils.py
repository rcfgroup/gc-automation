import glob
import os
from xml.dom import minidom

import pandas


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
    return results


def parse_report(csv_path: str):
    """return list of blob name, firstcol and secondcol from the combined table csv"""
    basename = os.path.basename(csv_path)
    print(basename)
    # if the report csv file structure has changed, edit skiprows
    df = pandas.read_csv(csv_path, skiprows=33)
    df_not_matched = None
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
    return results


def write_csv(csv_data, csv_path, header=False):
    """write matched template and blob to csv file"""
    df = pandas.DataFrame(csv_data)
    df.to_csv(csv_path, header=header, index=False)


def compare_match(date, tray, filepath):
    f_date, f_tray, *_ = filepath.split(" ")
    return f_date == date and f_tray == tray