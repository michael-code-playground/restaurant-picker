from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def update_sheet(creds, spreadsheet_id, range_name, values):
    """Updates data in a Google Sheet."""
    try:
        service = build("sheets", "v4", credentials=creds)
        body = {"values": values}
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()
        print(f"{result.get('updatedCells')} cells updated.")
    except HttpError as err:
        print(f"An error occurred: {err}")
