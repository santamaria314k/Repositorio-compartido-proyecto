class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost:3311/mechanics'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3311
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'admin'
    MYSQL_DB = 'mechanics'
    MYSQL_CURSORCLASS = 'DictCursor'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'paginamecanica'