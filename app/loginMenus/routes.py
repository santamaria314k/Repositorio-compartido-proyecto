from app import *
from flask import session
from flask import Flask
from flask import render_template, request, redirect, Response, url_for, session
from . import login

#LOGIN  CON LOS ROLES DE USUARIO


@login.route('/acceso-login')
def home():
    return render_template('login.html')   

@login.route('/admin')
def admin():
    return render_template('admin.html')   


@login.route('/valoracion')
def valoracion():
    return render_template('registro_valoracion.html')  

@login.route('/acceso-login', methods= ["GET", "POST"])
def login():
   
    if request.method == 'POST' and 'user' in request.form and 'password' in request.form:
       
        _user = request.form['user']
        _password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE user = %s AND password = %s', (_user, _password,))
        account = cur.fetchone()
      
        if account:
            session['logueado'] = True
            session['Id_user'] = account['Id_user']
            session['id_rol'] = account['id_rol']
            
            if session['id_rol']==1:
                return render_template("admin.html")
            elif session['id_rol']==2:
                return render_template("user.html")
        else:
            return render_template('login.html',mensaje="Hola su usuario o contraseña son incorrectas ")
  
  #metodo para el sierre de session
       
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/acceso-login')