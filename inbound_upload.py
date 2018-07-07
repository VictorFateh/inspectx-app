'''
spreadsheet_id = '1pOuH7Dz55DTbRiON_jPuBFi_60ab4V8CposinKh6p3w'

range_ = 'RAW FORM!A2:G'

value_range_body = {'values': full_pack.values()}
'''
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.authorize(credentials)


def sheets(package):
    sh = gc.open_by_key('1pOuH7Dz55DTbRiON_jPuBFi_60ab4V8CposinKh6p3w')
    worksheet = sh.worksheet("RAW FORM")

    return sh.worksheets()


def old_sheets(package):
    full_pack = package
    ts = time.time()
    full_pack['submission_time'] = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    # return full_pack.values()

