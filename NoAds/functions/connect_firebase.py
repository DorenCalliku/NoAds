import pyrebase

#
# Firebase connections
#

def connect_firebase(config):
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    storage  = firebase.storage()
    return database, storage