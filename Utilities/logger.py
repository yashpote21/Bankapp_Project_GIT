import inspect
import logging

# Creating class for Logs
class Log_Class:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)

        # Give the location of the bankapp.log file
        file = logging.FileHandler("C:\\Users\\Yash\\OneDrive\\Desktop\\Automation Testing Revision_Scratch\\Framework_Revision_5_Days\\Logs\\Bankapp.log")
        logformat = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
        file.setFormatter(logformat)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
