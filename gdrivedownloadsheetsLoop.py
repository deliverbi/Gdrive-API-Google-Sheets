#Shahed Munir v1.0
# Create a File called anything you like each google sheet id must be on a seperate row within the file !!
import os, csv, itertools, contextlib
from google.oauth2 import service_account
import sys
import re
from apiclient.discovery import build  # pip install google-api-python-client==1.6.2
# Create a File in the same directory With Google Sheet IDs on new lines to export more than 1 sheet
filepath = 'mysheets.txt'

#Loop Over mysheets.txt with Google Sheet ID's and Export All Google Sheets
with open(filepath) as fp:
   line = fp.readline()
   while line:

       SHEET = line.strip()
       scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
       service_account_file = os.path.join(os.getcwd(), 'SERVICEKEYGOESHERE.json')
       creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=scope)
       path = "/GCSDrive/output/"

# Rotate over sheets etc
       def itersheets(id):
          doc = service.spreadsheets().get(spreadsheetId=id).execute()
          title = doc['properties']['title']
          sheets = [s['properties']['title'] for s in doc['sheets']]
          params = {'spreadsheetId': id, 'ranges': sheets, 'majorDimension': 'ROWS'}
          result = service.spreadsheets().values().batchGet(**params).execute()
          for name, vr in zip(sheets, result['valueRanges']):
           yield (title, name), vr['values']

# Write CSV output ready for export
       def write_csv(fd, rows, encoding='utf-8', dialect='excel'):
          csvfile = csv.writer(fd, dialect=dialect, quoting=csv.QUOTE_NONNUMERIC)
          for r in rows:
           csvfile.writerow(r)

#Initiate Export and Writing
       def export_csv(docid, filename_template='%(title)s_%(sheet)s.csv'):
          for (doc, sheet), rows in itersheets(docid):
           filename = filename_template % {'title': doc.replace(' ','').replace('(', '').replace(')', '') , 'sheet': sheet.replace(' ','')}
           with open(path+filename, 'wt') as fd:
            write_csv(fd, rows)

       creds = creds
       service = build('sheets', version='v4', credentials=creds)

       export_csv(SHEET)
       print('Finished Processing'+' '+SHEET+'to '+path)
       line = fp.readline()