from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


class Conecction:
 
    def create_token_drive(self):

        try: 
            """Shows basic usage of the Drive v3 API.
            Prints the names and ids of the first 10 files the user has access to.
            """
            #SCOPE ME PERMITE TENER ACCESO COMPLETO A LOS ARCHIVOS DE GOOGLE DRIVE
            SCOPES = ['https://www.googleapis.com/auth/drive']
            
            creds = None
            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('config/token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'config/credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Crea token para utiliza los servicios de google drive 
                with open('config/token_drive.json', 'w') as token:
                    token.write(creds.to_json())
        
        except Exception as e:
            raise Exception(str(e)) 
        



