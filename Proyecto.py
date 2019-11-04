#Version 1.3

presupuesto = float(input("Ingrese preupuesto para materiales de construcción:"))

listado_productos = [["Fierro_un_medio",24.47,"varilla"],["Fierro_tres_octavos",13.84,"varilla"],["Fierro_cinco_octavos",37.68,"varilla"],["alambre_negro",3.48,"kg"],["Clavos",3.87,"kg"],["Cemento_portland",21.18,"bolsa"],["Cal",22.03,"bolsa"],["Yeso",7.13,"bolsa"],["Madera",5.9,"pie_cuadrado"],["Triplay",36.82,"plancha"],["Arena_Gruesa",50.41,"metro_cubico"],["Hormigon",50.88,"metro_cubico"],["Mayólica",20.78,"metro_cuadrado"],["Piedra_chancada",59.37,"metro_cubico"],["ladrillo_king_kong",672.53,"millar"],["ladrillo_pandereta",557.5,"millar"],["ladrillo_techo",2059.35,"millar"],["tubo_PVC_electricidad",2.64,"tubo"],["tubo_PVC_desasgüe",10.06,"tubo"],["alambre_TW12",1.85,"metro"],["alambre_TW14",1.23,"metro"],["cable_TW6",3.69,"metro"],["cable_TW8",5.61,"metro"],["alambre_y_cables_inst_tel",1.57,"metro"]]

costo = 0

for i in range(len(listado_productos)):
    print(i+1,listado_productos[i])

while True:
    while True:
        pos = int(input("Ingrese la posición del producto, iniciando de 1 a 24, ingrese 0 para finalizar:"))
        if pos >= 0 and pos <= len(listado_productos):
            break
    if pos == 0:
        break
    cantidad = int(input("ingrese cantidad del producto seleccionado:"))
    costos = costos + (listado_productos[pos-1][1]*cantidad)

print(costos)