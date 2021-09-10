import configparser

class TestProperties:
    def __init__(self, file_path='config.ini', section='DEFAULT'):
        config_ini = configparser.ConfigParser()
        config_ini.read(file_path, encoding='utf-8')

        self.config = config_ini[section]
        
        print("******設定ファイルの内容*******")
        print(self.config)
        print(dict(self.config))


    @property
    def username(self):
        return self.config.get('username')

    @property
    def password(self):
        return self.config.get('password')
        