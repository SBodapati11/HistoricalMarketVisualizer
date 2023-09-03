from flask import Flask
from flask_cors import CORS
from routes.user import usersAPI


app = Flask(__name__)
app.register_blueprint(usersAPI, url_prefix="/api/v1")
cors = CORS(app)

@app.route("/")
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)