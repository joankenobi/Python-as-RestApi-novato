# aplicacion de python, nuestro bakend, nuetra rest API
#utilizamos flask como franword, pero existen muchos otros
from flask import Flask

#flask devolvera un objeto llamado app
app=Flask(__name__) #app sera la aplicacion del servidor

#la funcion principal del servidor será enviar datos (los de products.py)

from products import products
#ruta de prueba para ver el funcionamiento del servidor
@app.route("/ping") #cuando el navegador pida la ruta "/ping" respondera con:
def ping(): #funcion ping que se ejecuta despues de pedir la ruta ping
      return "pong!" #proceso de testeo, queremos responder Json



if __name__ == "__main__": #si corre commo la principal
    app.run(debug=True, port=4000) #debug is for and 4000 is the port where escucha el servidor
    