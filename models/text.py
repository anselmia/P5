from PyQt5 import QtCore


class Message:
    def __init__():
        pass

    def welcome(log):
        log.appendText("Welcome\nPlease select a source to start.\n")

    def select(log, object_name):
        log.appendText(f"Please select a {object_name}")

    def loading(log, type, method):
        log.appendText(f"Loading {type} from {method}...")
        QtCore.QCoreApplication.processEvents()

    def done(log):
        log.appendText("Done.")

    def save_substitute(log):
        log.appendText("You can now save your substitute.")

    def favorite_saved(log):
        log.appendText("Your substitute was added to your favorite substitute.")

    def impossible_to_load(log, object_name):
        log.appendText(f"Impossible to load {object_name} ...", (255, 30, 30))

    def load_instead(log, object_name):
        log.appendText(
            f"There is no {object_name} in the database within this category. Application will look on the API instead."
        )

    def not_in_db(log, object_name):
        log.appendText(
            f"The {object_name} was not in the database. It will be saved too."
        )

    def saved(log, object_type, name):
        log.appendText(f"The {object_type} : {name} has been saved in the database.")

    def exist_in_db(log, object_type, name):
        log.appendText(f"The {object_type} : {name} already exist in the database.")

    def http_error(log):
        log.appendText("Http Error during the connection to the API.", (255, 30, 30))

    def connexion_error(log):
        log.appendText(
            "Error Connecting to the API. Please verify your connection.", (255, 30, 30)
        )

    def timeout(log):
        log.appendText("Timeout Error while connecting to the API", (255, 30, 30))

    def other_api_exception(log):
        log.appendText(
            "Error while connecting to the API. Please contact the administrator of the application.",
            (255, 30, 30),
        )

    def mysql_error(log, err):
        log.appendText("MySQL error : " + str(err), (255, 30, 30))

    def mysql_file_execute_command_skipped(log, error, line_num):
        log.appendText(
            f"Command skipped in line N°{line_num} : " + error, (255, 30, 30)
        )

