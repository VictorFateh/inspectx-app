import ConfigParser

import googleapiclient.discovery
import requests
from google.oauth2 import service_account

config = ConfigParser.ConfigParser()
config.read('config.ini')

MAILGUN_DOMAIN_NAME = config.get('MAILGUN', 'MAILGUN_DOMAIN_NAME')
MAILGUN_API_KEY = config.get('MAILGUN', 'MAILGUN_API_KEY')
BCC = config.get('MAILGUN', 'BCC')
SPREADSHEET_ID = config.get('SHEETS', 'SPREADSHEET_ID')
RANGE_NAME = config.get('SHEETS', 'RANGE_NAME')
SCOPE = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'client_secret.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPE)


# params [timestamp, name, email, phone, car, location, service, date]
def confirmation_email(package):
    email_body = open("static/email/email_html_body.html", "r").read().format(package[1], package[6].lower(), package[4])
    email_head = open("static/email/email_html_head.html", "r").read()
    email_full = email_head + email_body
    url = 'https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN_NAME)
    auth = ('api', MAILGUN_API_KEY)
    data = {
        'from': 'InspectX Vehicle Inspections <inspections@{}>'.format(MAILGUN_DOMAIN_NAME),
        'to': package[2],
        'bcc': 'victorfateh@yahoo.com',
        'subject': '{} Confirmation'.format(package[6]),
        'html': email_full
    }

    response = requests.post(url, auth=auth, data=data)
    response.raise_for_status()


def sheets(package):
    service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)

    values = [package]

    body = {
        'values': values
    }

    result = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, body=body,
                                                    valueInputOption='USER_ENTERED').execute()
    confirmation_email(package)

    print(result)
