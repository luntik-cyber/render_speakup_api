from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

logins = {
    "Oto": "Shazam12@",
    "Mate": "Mate123",
    "elene": "eleneadmin"
}

firebase_config = {
    "apiKey": "AIzaSyD93WyvlqmBo_CkChloCabFARucdoDILIA",
    "authDomain": "facebook-clone-fe696.firebaseapp.com",
    "projectId": "facebook-clone-fe696",
    "storageBucket": "facebook-clone-fe696.appspot.com",
    "messagingSenderId": "172533380090",
    "appId": "1:172533380090:web:2f80ab7f5f80d7cefdaa43",
    "measurementId": "G-2GH8KQ7ZNX"
}

@app.route("/getConfig/<input_username>/<input_password>", methods=["GET"])
def give_config(input_username, input_password):
    if input_password == logins[input_username]:
        return jsonify(firebase_config)
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run()
