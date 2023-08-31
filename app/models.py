from app import db

##Modelos <<entities>>

class Valoracion(db.Model):
    __tablename__="Valoracion"
    id_val = db.Column(db.Integer,primary_key=True)
    diagnostico =db.Column(db.String(3000))
    