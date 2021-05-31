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
    productsFound = [product for product in products if product["name"] == product_name]#hacer un recorrio con un for loop para recorrer la lista de productos
    if(len(productsFound)>0): #maneja la situacion cuando no hay producto
        return jsonify({"product":productsFound[0]}) #sin el [0] devuelve una lista
    return jsonify({"message":"product not found"})

if __name__ == "__main__": #si corre commo la principal
    app.run(debug=True, port=4000) #debug is for and 4000 is the port where escucha el servidor
    
    #estamos obteniendo datos de una RestApi pero para crear datos necesitamos crear una aplicacion o un formulario que nos permita ingresar los datos que queremos guardar:
    #los programas para esto son Postman, Insomnia, se usaran para probar las otras rutas de la RestApi.
    #la resapi no depende de donde se corra, se puede hacer usar en casi todo.