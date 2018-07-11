'''
spreadsheet_id = '1pOuH7Dz55DTbRiON_jPuBFi_60ab4V8CposinKh6p3w'

range_ = 'RAW FORM!A2:G'

value_range_body = {'values': full_pack.values()}
'''

from oauth2client.service_account import ServiceAccountCredentials
import google
import googleapiclient.discovery
from google.oauth2 import service_account

# google.appengine.api.urlfetch.set_default_fetch_deadline(60)

scope = ['https://www.googleapis.com/auth/spreadsheets']
# credentials = ServiceAccountCredentials.from_json_keyfile_name('templates/client_secret.json', scope)
SPREADSHEET_ID = '1pOuH7Dz55DTbRiON_jPuBFi_60ab4V8CposinKh6p3w'
RANGE_NAME = 'RAW FORM!A2:G'

SERVICE_ACCOUNT_FILE = 'client_secret.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=scope)


def sheets(package):
    service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)

    values = [package]

    body = {
        'values': values
    }

    result = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, body=body,
                                                    valueInputOption='USER_ENTERED').execute()

    print(result)
