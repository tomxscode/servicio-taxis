from flask import Flask

# Creación de la APP Web
app = Flask(__name__)

from routes.vehiculos import *


if __name__ == "__main__":
    app.run(debug=True, port=8000)