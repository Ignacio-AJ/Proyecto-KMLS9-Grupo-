#Version 2
listado_productos = [["Fierro_un_medio",24.47,"varilla"],["Fierro_tres_octavos",13.84,"varilla"],["Fierro_cinco_octavos",37.68,"varilla"],["alambre_negro",3.48,"kg"],["Clavos",3.87,"kg"],["Cemento_portland",21.18,"bolsa"],["Cal",22.03,"bolsa"],["Yeso",7.13,"bolsa"],["Madera",5.9,"pie_cuadrado"],["Triplay",36.82,"plancha"],["Arena_Gruesa",50.41,"metro_cubico"],["Hormigon",50.88,"metro_cubico"],["Mayólica",20.78,"metro_cuadrado"],["Piedra_chancada",59.37,"metro_cubico"],["ladrillo_king_kong",672.53,"millar"],["ladrillo_pandereta",557.5,"millar"],["ladrillo_techo",2059.35,"millar"],["tubo_PVC_electricidad",2.64,"tubo"],["tubo_PVC_desasgüe",10.06,"tubo"],["alambre_TW12",1.85,"metro"],["alambre_TW14",1.23,"metro"],["cable_TW6",3.69,"metro"],["cable_TW8",5.61,"metro"],["alambre_y_cables_inst_tel",1.57,"metro"]]
print(listado_productos)
pos = int(input("Ingrese la posición del producto, iniciando de 0 a 23:"))
while pos >=0 and pos <=23:
    cantidad_1 = int(input("ingrese cantidad del producto seleccionado:"))
    if cantidad_1 ==0:
        break
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

#Version 2
listado_productos = [["Fierro_un_medio",24.47,"varilla"],["Fierro_tres_octavos",13.84,"varilla"],["Fierro_cinco_octavos",37.68,"varilla"],["alambre_negro",3.48,"kg"],["Clavos",3.87,"kg"],["Cemento_portland",21.18,"bolsa"],["Cal",22.03,"bolsa"],["Yeso",7.13,"bolsa"],["Madera",5.9,"pie_cuadrado"],["Triplay",36.82,"plancha"],["Arena_Gruesa",50.41,"metro_cubico"],["Hormigon",50.88,"metro_cubico"],["Mayólica",20.78,"metro_cuadrado"],["Piedra_chancada",59.37,"metro_cubico"],["ladrillo_king_kong",672.53,"millar"],["ladrillo_pandereta",557.5,"millar"],["ladrillo_techo,2059.35,millar"],["tubo_PVC_electricidad",2.64,"tubo"],["tubo_PVC_desasgüe",10.06,"tubo"],["alambre_TW12",1.85,"metro"],["alambre_TW14",1.23,"metro"],["cable_TW6",3.69,"metro"],["cable_TW8",5.61,"metro"],["alambre_y_cables_inst_tel",1.57,"metro"]]
print(listado_productos)
cont=0
while True:
    cantidad = int(input("Ingresar cantidad de tipos de productos a registrar:"))