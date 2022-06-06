
from flask import Flask, jsonify, render_template, request
import funciones

app = Flask(__name__)

productos = []

@app.route("/")
def obtenerProductos():
    try:
        return jsonify({"Productos" : productos})
    except:
        return render_template('404.html'), 404

@app.route("/producto/<string:nombreProducto>", methods=['GET'])
def obtenerProducto(nombreProducto):
    
    devuelveProducto = [producto for producto in productos if producto['nombre'] == nombreProducto]
    if (len(devuelveProducto) > 0):
        return jsonify({"producto" : devuelveProducto[0]})
    return 'Producto NO encontrado'

@app.route("/agregar", methods=['POST'])
def agregar():
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


@app.route("/editar/<string:nombreProducto>", methods=['PUT'])
def editar(nombreProducto):
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



@app.route("/eliminar/<string:nombreProducto>", methods=['DELETE'])
def eliminar(nombreProducto):
    eliminarProducto = [producto for producto in productos if producto['nombre'] == nombreProducto]
    if len(eliminarProducto) > 0:
        productos.remove(eliminarProducto[0])
        return jsonify({
            "mensaje": "Producto Eliminado",
            "productos": productos
        })
    return "Producto NO encontrado"



