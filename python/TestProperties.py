import configparser

class TestProperties:
    def __init__(self):
        # --------------------------------------------------
        # configparserの宣言とiniファイルの読み込み
        # --------------------------------------------------
        config_ini = configparser.ConfigParser()
        config_ini.read('config.ini', encoding='utf-8')

        self.config = config_ini['DEFAULT']

    @property
    def username(self):
        return self.config.get('username')

    @property
    def password(self):
        return self.config.get('password')
        