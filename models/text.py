"""
    This module represent all the message that will be sent to the user
    trough the QPlainTextEdit object
"""

from PyQt5 import QtCore


class Message:
    """
    Instance of object Message.
    """

    def __init__(self, log):
        """
        Initialization of the Message object.
        Attributes : QPlainTextEdit Log instance.
        """
        self.log = log

    def welcome(self):
        """
        Message : Welcome/select a source
        """
        self.log.appendText("Welcome\nPlease select a source to start.\n")

    def select(self, object_name):
        """
        Method to invite to select a given object
        arg : object's name
        """
        self.log.appendText(f"Please select a {object_name}")

    def loading(self, type, method):
        """
        Message : loading object type from method
        arg : object type
              methode to retrieve object (Source)
        """
        self.log.appendText(f"Loading {type} from {method}...")
        QtCore.QCoreApplication.processEvents()

    def done(self):
        """
        Message Done
        """
        self.log.appendText("Done.")

    def save_substitute(self):
        """
        Method to invite to save substitute
        """
        self.log.appendText("You can now save your substitute.")

    def favorite_saved(self):
        """
        Message that favorite was saved
        """
        self.log.appendText("Your substitute was added to your favorite substitute.")

    def impossible_to_load(self, object_type):
        """
        Message that object type is impossible to load
        arg : object type
        """
        self.log.appendText(f"Impossible to load {object_type} ...", (255, 30, 30))

    def load_instead(self, object_type):
        """
        Message that prevent the user that object type will be loaded from API
        instead of Database
        arg : object type
        """
        self.log.appendText(
            f"There is no {object_type} in the database within this category. Application will look on the API instead."
        )

    def not_in_db(self, object_type):
        """
        Message that object type is not in Database and will be saved.
        arg : object type
        """
        self.log.appendText(f"The {object_type} was not in the database. It will be saved too.")

    def saved(self, object_type, name):
        """
        Message that object type was saved in the database.
        arg : object type
        """
        self.log.appendText(f"The {object_type} : {name} has been saved in the database.")

    def exist_in_db(self, object_type, name):
        """
        Message that object type already exist in the database.
        arg : object type
              name of the object
        """
        self.log.appendText(f"The {object_type} : {name} already exist in the database.")

    def http_error(self):
        """
        HTTP error occured (API connexion)
        """
        self.log.appendText("Http Error during the connection to the API.", (255, 30, 30))

    def connexion_error(self):
        """
        Connexion error occured (API connexion)
        """
        self.log.appendText(
            "Error Connecting to the API. Please verify your connection.", (255, 30, 30)
        )

    def timeout(self):
        """
        Timeout error occured (API connexion)
        """
        self.log.appendText("Timeout Error while connecting to the API", (255, 30, 30))

    def other_api_exception(self):
        """
        General error occured (API connexion)
        """
        self.log.appendText(
            "Error while connecting to the API. Please contact the administrator of the application.",
            (255, 30, 30),
        )

    def mysql_error(self, err):
        """
        SQL error occured (Database connexion)
        arg : error
        """
        self.log.appendText("MySQL error : " + str(err), (255, 30, 30))

    def mysql_file_execute_command_skipped(self, error, line_num):
        """
        SQL command skipped
        arg : error (string)
              command number (int)
        """
        self.log.appendText(f"Command skipped in line N°{line_num} : " + error, (255, 30, 30))
