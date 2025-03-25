import configparser

# Taking configparser.RawConfigParser for reading the data which is available in "Configurations\\config.ini" file
config = configparser.RawConfigParser()
# Reading values from 'config.ini 'file
config.read(".\\Configurations\\config.ini")

# Creating Class
class ReadConfigFile:

    # Creating method to read Username from 'config.ini' file
    @staticmethod
    def GetUsername():
        Username = config.get('login data', 'username' )
        return Username

    # Creating method to read Password from 'config.ini' file
    @staticmethod
    def GetPassword():
        Password = config.get('login data', 'password')
        return Password

    # Creating method for test_SearchUser_004
    @staticmethod
    def getUsername_for_SearchUser():
        Username = config.get('search user', 'username')
        return Username