from flask_wtf import FlaskForm
from wtforms import  StringField,SubmitField
from wtforms.validators import InputRequired

class Registrarvaloracionform(FlaskForm):
   
  diagnostico=StringField("Valoracion del vehiculo", validators = [InputRequired(message="ingrese la Valoracion del vehiculo")])
  submit=SubmitField("Guardar", render_kw={"class": "btn-guardar"})
  