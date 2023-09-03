import app
from flask import session
from flask import render_template
from .forms import Registrarvaloracionform
from . import valoracion


@valoracion.route("/listarvaloracion")
def listarvaloracion():
    valoraciones = app.models.Valoracion.query.all()
    return render_template("listar_valoracion.html", valoraciones=valoraciones)


@valoracion.route('/registroval',methods=["GET", "POST"])
def registroval():
    form=Registrarvaloracionform()
    if form.validate_on_submit():
        v=app.models.Valoracion()
        form.populate_obj(v)
        app.db.session.add(v)
        app.db.session.commit()
        return "valoracion registrada" 
     

    return render_template('registro_valoracion.html', form=form) 


