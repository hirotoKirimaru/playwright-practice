import configparser

class ScenarioProperties:
    def __init__(self, file_path='config.ini', section='DEFAULT'):
        config_ini = configparser.ConfigParser()
        config_ini.read(file_path, encoding='utf-8')

        self.config = config_ini[section]
        self._section = section

    @property
    def url(self):
        return self.config.get('url')

    @property
    def height(self):
        return int(self.config.get('height'))

    @property
    def width(self):
        return int(self.config.get('width'))

    @property
    def section(self):
        return self._section
        