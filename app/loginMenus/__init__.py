from flask import Blueprint


login=Blueprint('loginMenus',__name__,url_prefix='/login',template_folder='templates')


#vincular archivo de rutras
from . import routes