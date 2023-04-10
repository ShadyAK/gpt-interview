from src.utils.utils import hash_string
from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Account:
    def __init__(self, db):
        self.__db = db
        pass 

    def check_user_exists(self, email : str) -> bool: 
        user_ref = self.__db.collection("users").where("email", "==", email).limit(1).get()
        if len(user_ref) > 0:
            print("User with email {} already exists".format(email))
            return False
        return (user_ref, True) 
    
    def signup_user(self, email : str, password : str) -> tuple[bool, str]:
         # Create new user document in Firestore
        if not self.check_user_exists(email): return False, "User already Exists" 

        user_data = {
            "email": email,
            "password": hash_string(password) # Hashed Password for security
        }
        self.__db.collection("users").add(user_data)
        print("User with email {} created successfully".format(email))

        return True, "User created successfully" 
    
    def signin(self, email: str, password: str):
        try:
            user_ref = self.__db.collection("users").where("email", "==", email).limit(1).get()
            if len(user_ref):
                user_details = user_ref[0].to_dict()
                if user_details["password"] == password:
                    return True, user_details["email"]
            return False, None
        
        except Exception as e:
            print("Failed to sign in user with email {}".format(email))
            print("throwing exception: {}".format(e))
            return False, None
        
if __name__ == "__main__":
    pass
