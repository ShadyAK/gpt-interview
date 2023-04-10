from os import getcwd, listdir
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db,firestore

class Firestore_DB:
    print(getcwd())
    print(listdir('.'))
    __cred = credentials.Certificate("/Users/shady/Desktop/accountKey.json")

    def __init__(self):
        firebase_admin.initialize_app(self.__cred)
        self.__db = firestore.client()

    def get_db_client(self):
        return self.__db