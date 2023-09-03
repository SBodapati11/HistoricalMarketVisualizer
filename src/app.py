from flask import Flask
from models.user import User


app = Flask(__name__)

if __name__ == "__main__":
    
    app.run(host="localhost", port=8080)