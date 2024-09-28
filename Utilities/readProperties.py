import configparser
from faker import Faker
# faker library to generate random names and email addresses.

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getUsername():
        username = config.get('common info', 'User_name')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'Password')
        return password

    # Initialize Faker
    fake = Faker()

    # faker library to generate random names and email addresses.
    @staticmethod
    def getFirstUserName():
        first_user_name = ReadConfig.fake.first_name()
        return first_user_name

    @staticmethod
    def getEmailAddress():
        email_address = ReadConfig.fake.email()
        return email_address
