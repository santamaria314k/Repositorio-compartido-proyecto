from app.config import Config
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mysqldb import MySQL,MySQLdb 
from flask_bootstrap import Bootstrap

            #OBJETOS  DE LA APLICASION 

# crear el objeto de aplicación
app = Flask(__name__)



#configurar app para conectarse a bd desde config
app.config.from_object(Config)



# crear el objeto sqlalchemy
db = SQLAlchemy(app)

mysql = MySQL(app)

#configurar MIGRACIONES con app (objeto)
migrate = Migrate(app , db)



#configurar BOOTSTRAP con app (objeto)
bootstrap = Bootstrap(app)



#Traer los modelos
from .models import Valoracion

app.Valoracion = Valoracion


#from .models import NOMBRE DE LOS MODELOS QUE SE IMPORTAN

#registrar los  modulos
from app.loginMenus import login
from app.registroValoracion import valoracion

app.register_blueprint(login)
app.register_blueprint(valoracion)







  
