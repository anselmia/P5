from PyQt5 import QtCore


class Message():

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
    
    def impossible_to_load(log, object_name):
        log.appendText(f"Impossible to load {object_name} ...")

    def load_instead(log, object_name):
         log.appendText(f"There is no {object_name} in the database within this category. Application will look on the API instead.")

    def not_in_db(log, object_name):
        log.appendText(f"The {object_name} was not in the database. It will be saved too.")

    def saved(log, object_type, name):
        log.appendText(f"The {object_type} : {name} has been saved in the database.")

    def exist_in_db(log, object_type, name):
        log.appendText(f"The {object_type} : {name} already exist in the database.")

    def http_error(log, err):
        log.appendText("Http Error:" + str(err), (255,30,30))

    def connexion_error(log, err):
        log.appendText("Error Connecting:" + str(err), (255,30,30))

    def timeout(log, err):
        log.appendText("Timeout Error:" + str(err), (255,30,30))
    
    def other_api_exception(log, err):
         log.appendText("OOps: Something Else" + str(err), (255,30,30))

    def mysql_error(log, err):
        log.appendText("MySQL error : " + str(err), (255,30,30))