import configparser

import configparser 

class Config:

    def config_parser(self):
        config = configparser.ConfigParser()
        config.read('config/config.ini')

        id_folder = config.get('Drive', 'folder_id')

        with open('config/config.ini', 'w') as configfile:
            config.write(configfile)

        return {"id_folder":id_folder}


