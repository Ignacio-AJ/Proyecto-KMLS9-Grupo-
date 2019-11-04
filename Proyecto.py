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
print(lista)
#Preguntar presupuesto para la compra de materiales
pre = float(input("Ingresar presupuesto para la compra de materiales para la obra:"))
#Preguntar si el presupuesto cubre el costo
a = 0
costos = 0
while a < cantidad:
    costos = costos + (lista[a][1]*lista[a][2])
    a+=1
print(costos)
viabilidad = pre-costos
if viabilidad >= 0:
    print("Es viable por:", viabilidad)
else:
    print("No es viable por", viabilidad)