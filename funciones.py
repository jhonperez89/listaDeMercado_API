from datetime import *

def registro (resultado):
    fecha = datetime.today()
    archivo = open('resgistroProductos.txt', 'w')
    archivo.write(f' {fecha}  El Producto es: {resultado}\n')
    archivo.close()   
    return (fecha, archivo)  