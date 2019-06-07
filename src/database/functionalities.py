import src.database.constants as cnsts
import pyrebase

config = cnsts.config

# Firebase connections
def connect_firebase():
    """Connect to firebase with its functionalities."""

    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    storage  = firebase.storage()
    return database, storage

def retrieve( path):
    """Get info in database."""

    db, _ = connect_firebase()
    return db.child( path).get().val()  


def update( path, data):
    """Update parent with child."""

    db, _ = connect_firebase()
    db.child( path).update( data)
