import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = "sirius-355912-ca31fefaf074.json"

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

# spreadsheet = service.spreadsheets().create(body={
#     'properties': {'title': 'Sirius_DB_Dumps', 'locale': 'ru_RU'},
#     'sheets': [{'properties': {'sheetType': 'GRID',
#                                'sheetId': 0,
#                                'title': 'Dumps',
#                                'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
# }).execute()
# spreadsheetId = spreadsheet['spreadsheetId']
# print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)


spreadsheet_id = "1dmoUSGS1SGtv9MuMH7rYLbhTU8qREpVZizo9i4OKY_c"

driveService = apiclient.discovery.build('drive', 'v3', http=httpAuth)
access = driveService.permissions().create(
    fileId=spreadsheet_id,
    body={'type': 'user', 'role': 'writer', 'emailAddress': 'your_email@gmail.com'},  # Вставить свой email
    # Открываем доступ на редактирование
    fields='id'
).execute()
