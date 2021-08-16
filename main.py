from flask import Flask, request
from db import db
import os

app = Flask(os.path.basename(os.path.dirname(__file__)))
app.secret_key = "My_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./db/master.db"

db.init_app(app)
#db.create_all(app=app)


@app.route("/")
@app.route("/index")
def index():
    pass


if __name__ == "__main__":
    app.run("127.0.0.1", 8080, debug=True)
