

import var, cred

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
credential = ServiceAccountCredentials.from_json_keyfile_name(cred.gspread_json, scope)
client = gspread.authorize(credential)

sheet = client.open("text_msg").sheet1