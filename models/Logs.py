from flask_sqlalchemy import SQLAlchemy
from app import db

# Creación de la tabla "Logs", con las columnas: id, fecha, acción y responsable (fk de User)
class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    accion = db.Column(db.String(100))
    responsable = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, fecha, accion, responsable):
        self.fecha = fecha
        self.accion = accion
        self.responsable = responsable

    def __repr__(self):
        return '<Logs %r>' % self.id