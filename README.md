# Gdrive-API-Google-Sheets Extract to CSV with SERVICE KEY
Google Python Scripts I Drive Extract Google Sheet with Service Key json

The python script can be used to extract google sheets as csv . The script will extract all worksheets within a Google Sheets workbook.

# Mandatory Parameters
Service Key and a Google Sheet ID.

Service Keys can be generated for a project within google. Then the email address of the service key needs to be used for sharing of
the spreadsheet within google sheets

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

# Run Command

The parameter is the google sheet ID which is visible in most url's when viewing the sheet in google.

python3 gdrivedownloadsheets.py 1gWxy05uEcO8a8fNAfUSIdV1OcRWxH7RnjXezoHImJLE


Enjoy 

Shahed Munir
