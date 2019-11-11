#Version 1.3

# Registro de presupuesto

presupuesto = float(input("Ingrese presupuesto del proyecto con respecto a los materiales de construcción: "))

# Materiales organizados en lista

listado_productos = [["Fierro_un_medio",24.47,"Varilla"],["Fierro_tres_octavos",13.84,"Varilla"],["Fierro_cinco_octavos",37.68,"Varilla"],["Alambre_negro",3.48,"kg"],["Clavos",3.87,"kg"],["Cemento_portland",21.18,"Bolsa"],["Cal",22.03,"Bolsa"],["Yeso",7.13,"Bolsa"],["Madera",5.9,"Pie_cuadrado"],["Triplay",36.82,"Plancha"],["Arena_gruesa",50.41,"Metro_cúbico"],["Hormigón",50.88,"Metro_cúbico"],["Mayólica",20.78,"Metro_cuadrado"],["Piedra_chancada",59.37,"Metro_cúbico"],["Ladrillo_king_kong",672.53,"Millar"],["Ladrillo_pandereta",557.5,"Millar"],["Ladrillo_techo",2059.35,"Millar"],["Tubo_PVC_electricidad",2.64,"Tubo"],["Tubo_PVC_desasgüe",10.06,"Tubo"],["Alambre_TW12",1.85,"Metro"],["Alambre_TW14",1.23,"Metro"],["Cable_TW6",3.69,"Metro"],["Cable_TW8",5.61,"Metro"],["Alambre_y_cables_instalación_telefónica",1.57,"Metro"]]

costo = 0

for i in range(len(listado_productos)):
    print(i+1, listado_productos[i])

# Registro del material requerido (tipo, cantidad y costo)

while True:
    while True:
        pos = int(input("Ingrese la posición del producto, iniciando de 1 a 24; digite 0 para finalizar: "))
        if pos >= 0 and pos <= len(listado_productos):
            break
    if pos == 0:
        break
    cantidad = int(input("Ingrese cantidad del producto seleccionado: "))
    costo = costo + (listado_productos[pos-1][1]*cantidad)

# Round para evitar el error de decimales con los múltiplos de 3

costo = round(costo,2)

print("El costo total de los materiales registrados es de", costo, "soles.")

# Verificación de la viabilidad del proyecto

viabilidad = presupuesto - costo
if viabilidad > 0:
    print("El proyecto es viable. Su presupuesto excede en", viabilidad, "soles.")
elif viabilidad == 0:
    print("El proyecto es viable. Sin embargo, su presupuesto es exacto; le quedan", viabilidad, "soles.")
else:
    print("El proyecto no es viable. El costo de materiales excede a su presupuesto en", viabilidad*(-1), "soles.")