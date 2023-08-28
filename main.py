#Importacionde dependencias

from app import app

    
if __name__ == '__main__':
   app.secret_key = "paginamecanica"
   app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)




