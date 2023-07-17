from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from parser.config_parsers import Config

class Drive_controllers:
    
    def search_file(self):
        """
            Este methodo se encarga de encontrar los archivos dentro de google drive
            return: retornara el nombre del archivo y su id
        """
        try:
            #..... necesito encontrar la forma de retornar la ruta
            creds_path = "C:\\Users\\Fsalazar\\Documents\\cursos\\Comunicación con Google Workplace\\search_drive\\config\\token_drive.json"
            #Cargar las credenciales
            creds = Credentials.from_authorized_user_file(creds_path)
            #crear cliente de API GOOGLE DRVE
            drive_serivice = build('drive', 'v3', credentials=creds)
            #......... necesito pasarle la id folder en un archivo .ini
            config = Config().config_parser()
            folder_id = config["id_folder"]
            result = drive_serivice.files().list(q=f"'{folder_id}' in parents").execute()
            files = result.get('files', [])

            file_dicc = {}
            for file in files:
                file_dicc[file['name']] = file['id']
           
            return file_dicc
               

        except Exception as e:
            raise Exception(str(e))
        
    def transform_gsheet_to_df():
        """
        Este methodo tomara la id el archivo de google sheet, creara un df con su informacion 
        
        """
        pass
    def process_df():
        pass
    def send_df_with_gmail():
        pass
#.................. listar archivos de tu google drive
# try:
#             service = build('drive', 'v3', credentials=creds)

#             # Call the Drive v3 API
#             results = service.files().list(
#                 pageSize=10, fields="nextPageToken, files(id, name)").execute()
#             items = results.get('files', [])

#             if not items:
#                 print('No files found.')
#                 return
#             print('Files:')
#             for item in items:
#                 print(u'{0} ({1})'.format(item['name'], item['id']))
#         except HttpError as error:
#             # TODO(developer) - Handle errors from drive API.
#             print(f'An error occurred: {error}')