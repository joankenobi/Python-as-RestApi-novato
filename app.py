# aplicacion de python, nuestro bakend, nuetra rest API
#jsonify combierte un objeto al formato para navegador
from flask import Flask ,jsonify

#flask devolvera un objeto llamado app
app=Flask(__name__) #app sera la aplicacion del servidor

#la funcion principal del servidor será enviar datos (los de products.py)

from products import products
#ruta de prueba para ver el funcionamiento del servidor
@app.route("/ping") #Las rutas permiten especificar los metodos HTTP(estos simplemente quieren decir que es lo que queremos hacer dentro del servidor)
def ping(): #funcion ping que se ejecuta despues de pedir la ruta ping
      return jsonify({"mensaje":"pong!"}) #Un objeto json

@app.route("/products", methods= ["GET"]) #tenemos otra ruta que funciona (trabaja) por el metodo http GET, por defecto las rutas funcionan con metodo GET
def getProducts(): #funcion que retorna los productos like json
    return jsonify({"products": products, "mensaje": "product's list"}) #Se puede agregar informacion extra

@app.route("/products/<string:product_name>", methods= ["GET"]) #<string:product_name> entrada dinamica de la aplicacion clientes
def nameProducts(product_name):
    print(product_name) #imprime la modificacion de la ruta en el product name
    return "received"

    #return jsonify(products[name:])

if __name__ == "__main__": #si corre commo la principal
    app.run(debug=True, port=4000) #debug is for and 4000 is the port where escucha el servidor
    