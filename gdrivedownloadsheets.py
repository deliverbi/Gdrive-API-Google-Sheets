# Download Google Sheet via Python with Service Account Key - download all sheets of a google docs spreadsheet as csv
# Download Gdrive Spreadsheet to CSV
# Shahed Munir v1.0

import os, csv, itertools, contextlib
from google.oauth2 import service_account
import sys

from apiclient.discovery import build  # pip install google-api-python-client==1.6.2

SHEET = sys.argv[1]
scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
service_account_file = os.path.join(os.getcwd(), 'SERVICEACCOUNTKEY.json')
creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=scope)
path = "/GCSDrive/output/"

def itersheets(id):
    doc = service.spreadsheets().get(spreadsheetId=id).execute()
    title = doc['properties']['title']
    sheets = [s['properties']['title'] for s in doc['sheets']]
    params = {'spreadsheetId': id, 'ranges': sheets, 'majorDimension': 'ROWS'}
    result = service.spreadsheets().values().batchGet(**params).execute()
    for name, vr in zip(sheets, result['valueRanges']):
        yield (title, name), vr['values']

def write_csv(fd, rows, encoding='utf-8', dialect='excel'):
    csvfile = csv.writer(fd, dialect=dialect, quoting=csv.QUOTE_NONNUMERIC)
    for r in rows:
      csvfile.writerow(r)
                                          #title if workbookname is to be displayed
def export_csv(docid, filename_template='%(SHEET)s_%(sheet)s.csv'):
    for (doc, sheet), rows in itersheets(docid):
        filename = filename_template % {'SHEET': SHEET, 'sheet': sheet}
# For workbook Name to be displayed
       #filename = filename_template % {'title': doc, 'sheet': sheet}
        with open(path+filename, 'wt') as fd:
            write_csv(fd, rows)

creds = creds
service = build('sheets', version='v4', credentials=creds)

export_csv(SHEET)
print('Finished Processing'+' '+SHEET+'to '+path)
