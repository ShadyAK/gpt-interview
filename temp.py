from src.account.Account import Account
from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from src.utils.utils import hash_string
cred = credentials.Certificate("/Users/shady/Desktop/accountKey.json")
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()
print(hash_string("ashwin's password"))
print(hash_string("ashwin's password") == "85680845085f8ae394b9718ece07bed8") 

account = Account(db)
password = "abc"
email = "ashwin07kaurav@gmail.com"
account.signup_user(email, password)
print(hash_string(password))
res = account.signin(email, hash_string(password))
print(res)