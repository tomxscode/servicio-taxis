from app import app
from flask import render_template

@app.route('/vehiculos/', methods=['GET', 'POST'])
def index_vehiculos():
    return "Index de vehículos"

@app.route('/vehiculos/listar/', methods=['GET', 'POST'])
def listar_vehiculos():
    return "Vista de listado"

@app.route('/vehiculos/detalle/', methods=['GET', 'POST'])
def detalle_vehiculo():
    return "Detalle especifico de cada vehículo"

@app.route('/vehiculos/crear/', methods=['GET', 'POST'])
def crear_vehiculo():
    return "Vista de creación"

@app.route('/vehiculos/actualizar/', methods=['GET', 'POST'])
def actualizar_vehiculo():
    return "Vista de actualización"