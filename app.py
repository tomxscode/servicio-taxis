from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creación de la APP Web
app = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = 'XXXXXXXXXXX'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Importación de las rutas
from routes.vehiculos import *


if __name__ == "__main__":
    app.run(debug=True, port=8000)