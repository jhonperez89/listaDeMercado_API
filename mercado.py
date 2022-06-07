
from flask import Flask, jsonify, render_template, request
import funciones

app = Flask(__name__)

productos = []

@app.errorhandler(404) # Mustra el error 404 en una pagina html personalizada 
def pagina_no_encontrada(e):
    return render_template('404.html'),404



@app.route("/") # Mustra todos los productos que han sido agregados
def obtenerProductos():
    try:
        return jsonify({"Productos" : productos})
    except:
        return 'Verifica tus datos ha ocurrido un error'
       
        

@app.route("/producto/<string:nombreProducto>", methods=['GET']) # Mustra un solo producto por su nombre
def obtenerProducto(nombreProducto):
    try:
        devuelveProducto = [producto for producto in productos if producto['nombre'] == nombreProducto]
        if (len(devuelveProducto) > 0):
            return jsonify({"producto" : devuelveProducto[0]})
        return 'Producto NO encontrado'
    except:
        return 'Verifica tus datos ha ocurrido un error'
    

@app.route("/agregar", methods=['POST']) # Al agregar productos debe hacerce por body 
def agregar():                           # y en formato json en thunder client o postman
    try:
        nuevosProductos = {
            "nombre" : request.json['nombre'],
            "cantidad" : request.json['cantidad'],
            "precio" : request.json['precio']
        }
        productos.append(nuevosProductos)
        return jsonify({
                "mensaje": "Exito agregando producto",
                "productos": nuevosProductos
                
            })
    except:
        return 'Verifica tus datos ha ocurrido un error'
    
    


@app.route("/editar/<string:nombreProducto>", methods=['PUT']) # edita los productos mediante un json 
def editar(nombreProducto):
    try:
        cambioProducto = [producto for producto in productos if producto['nombre'] == nombreProducto]
        if (len(cambioProducto) > 0):
            cambioProducto[0]['nombre'] = request.json['nombre']
            cambioProducto[0]['cantidad'] = request.json['cantidad']
            cambioProducto[0]['precio'] = request.json['precio'] 
            return jsonify({
                "mensaje" : "Exito editando el producto",
                "producto" : cambioProducto[0]
            })
        return 'producto NO encontrado'
    except:
        return 'Verifica la informacion ha ocurrido un error'



@app.route("/eliminar/<string:nombreProducto>", methods=['DELETE']) # selecciona el nombre del producto 
def eliminar(nombreProducto):                                       # que desea eliminar indicando el nombre
    try:
        eliminarProducto = [producto for producto in productos if producto['nombre'] == nombreProducto]
        if len(eliminarProducto) > 0:
            productos.remove(eliminarProducto[0])
            return jsonify({
                "mensaje": "Producto Eliminado",
                "productos": productos
            })
        return "Producto NO encontrado"
    except:
        return 'Verifica la informacion ha ocurrido un error'


