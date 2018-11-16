# Gdrive-API-Google-Sheets Extract to CSV with SERVICE KEY
Google Python Scripts I Drive Extract Google Sheet with Service Key json

The python script can be used to extract google sheets as csv . The script will extract all worksheets within a Google Sheets workbook.

# Mandatory Parameters
Service Key and a Google Sheet ID.

Service Keys can be generated for a project within google. Then the email address of the service key needs to be used for sharing of
the spreadsheet within google sheets

For : gdrivedownloadsheetsLoop.py

Requires only service key.json file name, The google sheet names are derived from a.txt file you place in the same directory


# Setup

Make sure your python library for google api is this version ( can be higher but not tested on higher versions)

pip install google-api-python-client==1.6.2

Also make sure all other libraries are installed using pip these are visible in the script under import.

Download Python Script gdrivedownloadsheets.py to a directory on Linux.

Ammend the Following

Replace YOURSERVICEKEY.json with the filename of the service key you generated in Google.
service_account_file = os.path.join(os.getcwd(), 'YOURSERVICEKEY.json')

This will be your output Path for your csv files (1 per worksheet within a workbook)
path = "/GCSDrive/output/"

For : gdrivedownloadsheetsLoop.py
Requires only service key.json file name, The google sheet names are derived from a.txt file you place in the same directory

# Run Commands

The parameter is the google sheet ID which is visible in most url's when viewing the sheet in google.

--------------- For running 1 workbook at a time
python3 gdrivedownloadsheets.py 1gWxy05uEcO8a8fNAfUSIdV1OcRWxH7RnjXezoHImJLE

--------------- For running Multiple Workbooks one after another
python3 gdrivedownloadsheetsLoop.py 

# Notes: Google Sheet ID

https://developers.google.com/sheets/api/guides/concepts

Spreadsheet ID
Every API method requires a spreadsheetId parameter which is used to identify which spreadsheet is to be accessed or altered. This ID is the value between the "/d/" and the "/edit" in the URL of your spreadsheet. For example, consider the following URL that references a Google Sheets spreadsheet:

https://docs.google.com/spreadsheets/d/1qpyC0XzvTcKT6EISywvqESX3A0MwQoFDE8p-Bll4hps/edit#gid=0
The ID of this spreadsheet is 1qpyC0XzvTcKT6EISywvqESX3A0MwQoFDE8p-Bll4hps.


Enjoy 

Shahed Munir
