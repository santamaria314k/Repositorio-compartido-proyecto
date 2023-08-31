import app
from flask import session
from flask import render_template
from .forms import Registrarvaloracionform
from . import valoracion




@valoracion.route('/registroval',methods=["GET", "POST"])
def registroval():
    form=Registrarvaloracionform()
    if form.validate_on_submit():
        v=app.models.Valoracion()
        form.populate_obj(v)
        app.db.session.add(v)
        app.db.session.commit()
        return "producto registrado" 
     

    return render_template('registro_valoracion.html', form=form) 


