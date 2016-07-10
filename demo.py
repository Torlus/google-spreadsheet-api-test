import gspread
import json
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("aquarium").sheet1
# pprint(dir(wks))
# wks = gc.open("1Tua18h30lLC4hKeOmyqzXcDlZxrRl6sG7tAKIPSRTgw").sheet1

val = wks.acell('A2').value
print(val)

val = int(val) + 1

wks.update_acell('A2', val)

