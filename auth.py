
from google.oauth2 import service_account




def authenticate():
    # Path to your service account key file
    SERVICE_ACCOUNT_FILE = 'the-method-427521-p2-74db9b4d1aa9.json'
    
    # Scopes required for your application
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
    # Authenticate using the service account file
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    return creds






