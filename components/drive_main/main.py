from components.drive_main.app.conecction.conecction import Conecction
from components.drive_main.app.controllers.drive_controllers import  Drive_controllers

#CREAR TOKEN PARA ACCESO A GOOGLE DRIVE SI ESTE NO EXISTE
#Conecction().create_token_drive()

class Drive_main:
  
  search_file = Drive_controllers().search_file()