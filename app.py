from flask import Flask, request, jsonify
from src.account.Account import Account
from src.db.firestore_db import Firestore_DB
from flask_cors import CORS
db = Firestore_DB()
db_client = db.get_db_client()
account = Account(db_client)
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/login', methods = ["POST"])
def login():
    data = request.form 
    email, password = data["email"], data["password"]
    
    res, userId = account.signin(email, password)

    if res:
        print(userId, "is logged in") 
        return "logged in as {}".format(userId)
    
    else:
        return "something went wrong"

@app.route('/signup', methods = ["POST"])
def signup():
    data = request.get_json() 
    
    email, password = data["email"], data["password"]

    res, message = account.signup_user(email, password)
    #Res is a boolean, maintain the new session if the res is true
    response = jsonify({'message': "message"})
    response.headers.add('Access-Control-Allow-Origin', '*')  # Add this line
    return response

if __name__ == '__main__':
    app.run(debug=True)