from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def read_sheet(creds, spreadsheet_id, range_name):
    """Reads data from a Google Sheet."""
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get("values", [])
        
        if not values:
         print("No data found.")

        return values
    except HttpError as err:
        print(f"An error occurred: {err}")
        return None
