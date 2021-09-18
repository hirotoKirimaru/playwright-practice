# import configparser

class TestProperties:
    def __init__(self, file_path='config.ini', section='DEFAULT'):
        import configparser
        config_ini = configparser.ConfigParser()
        config_ini.read('config.ini', encoding='utf-8')

        print("******設定ファイルの内容*******")
        print(config_ini.items('IT'))
        print(dict(config_ini.items('IT')))
        print(config_ini['ST'])
        print(dict(config_ini['ST']))
        print({section: dict(config_ini[section]) for section in config_ini.sections()})




        self.config = config_ini[section]
        



    @property
    def username(self):
        return self.config.get('username')

    @property
    def password(self):
        return self.config.get('password')
        