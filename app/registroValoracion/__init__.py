from flask import Blueprint


valoracion=Blueprint('registroValoracion',__name__,url_prefix='/valoracion',template_folder='templates')


#vincular archivo de rutras
from . import routes