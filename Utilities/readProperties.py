import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig():
    @staticmethod
    def getUsername():
        username = config.get('common info', 'User_name')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'Password')
        return password
