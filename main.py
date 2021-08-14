from flask import Flask
from auth import login_manager
from models import db
import os

app = Flask(os.path.basename(os.path.dirname(__file__)))
app.secret_key = "My_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////db/master.db"

login_manager.init_app(app)

db.init_app(app)

if __name__ == "__main__":
    app.run("127.0.0.1", 8080, debug=True)