import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase credentials
cred = credentials.Certificate("/Users/shady/Desktop/accountKey.json")
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()

# Define function to create a new user
def signup(email, password):
    # Check if user with email already exists
    user_ref = db.collection("users").where("email", "==", email).limit(1).get()
    if len(user_ref) > 0:
        print("User with email {} already exists".format(email))
        return False
    
    # Create new user document in Firestore
    user_data = {
        "email": email,
        "password": password
    }
    db.collection("users").add(user_data)
    print("User with email {} created successfully".format(email))
    return True  

if __name__ == "__main__":
    signup("someEmail", "somePassword")