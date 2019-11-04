#Pedir la cantidad de materiales
cantidad = int(input("Ingresar cantidad de tipos de productos a registrar:"))
lista = []
for i in range(cantidad):
    num = str(1+i)
    nombre = input("Ingresar el nombre del producto" + num + ":")
    precio = float(input("Ingresar el precio del producto" + num + ":"))
    cantidad_productos = int(input("Ingrese la cantidad de productos a emplear" + num + ":"))

    producto = [nombre,precio,cantidad_productos]
    lista.append(producto)
#Preguntar presupuesto para la compra de materiales
pre = float(input("Ingresar presupuesto para la compra de materiales para la obra:"))
#Preguntar si el presupuesto cubre el costo

print(lista)