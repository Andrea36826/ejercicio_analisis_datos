"""limit = 100 
for i in range(limit):
    print (i,"jonier")"""

"""list_mercado = ["arroz","azucar","sal","carne"]
for i in range (4):
    print(list_mercado[i])"""

"""list_paises = ["Italia", "Colombia", "Brasil" , "México"]
longitud = len(list_paises)
for i in range(longitud):
    print(list_paises[i])"""

"""list_paises = ["Italia", "Colombia","Brasil","Mexico ", "Bolvia"]
list_poblacion = ["10 mill", "50 mill","110 mil","120 mill", "30 mill"]
longitud = len(list_paises)

for pos in range(4, 0, -1):
    print(list_paises[pos], list_poblacion [pos])"""

"""for pos in range (100, -1 , -2):
    print (pos)"""

"""for pos in range (-10, 11, 1):
    print(pos)"""
"""lista_electro = ["TV", "Barra sonido", "Computador"]
lista_precios= ["100 mil", "300 mil", "500 mil"]
longitud = len(lista_electro)
for pos in range (longitud):
    print (lista_electro [pos], lista_precios [pos])

general = ["TV 100 mil", "Barra sonido 300 mil" , "Computador 500 mil"]
longitud = len (general)

for pos in range (int(len(general)/2)):
    print (general [pos*2], general [pos*2+1])"""

"""marcas_zapatos = ["adidas","Nike" ,"Puma"]

for marca in marcas_zapatos:
    print (marca)"""

notas = [["Ana",4,3.8,3.9],["Jonier", 4.8,4.8,5.0], ["Luz",3.5,3.8,3],["Javier",2.5,3.8,2]]

"""sumatoria = 0
for fil in range (4):
    sumatoria_est= 0
    for col  in range (1, 4):
        sumatoria = sumatoria + notas[fil][col]
        sumatoria_est = sumatoria_est + notas[fil][col]
        prom_estu =round(sumatoria_est/3,1)
    print(notas[fil][0],prom_estu)

promedio_gen = round(sumatoria/12,2)
print("general", promedio_gen)"""

list_persona = [["Jonier", 32, "ingeniero"],
                ["Andrea", 35, "Docente"],
                ["Johana", 37, "Ingeniera"],
                ["Pedro", 50, "Médico"]]
cant_filas=len(list_persona)
cant_col = len (list_persona[0])
for i in range (cant_filas):
    for j in range(cant_col):
        print(list_persona[i][j])

    print ("----------")

"""list_car = [["Audi","2021","Q4" , "Rojo"],["Toyota","2015","Prado","Negra"],["Renault","2025","Logan","Azul"]]
             
cant_filas=len(list_car)
cant_col= len(list_car[0])
for i in range (cant_filas):
    for j in range (cant_col):
        print(list_car[i][j])

    print ("----------")"""

list_data =[["Jonier", "Bogotá",102036],["Juan","Pereira",48562],["Jenny","Barranquilla", 789651]]

id= int(input("Ingrese su cédula"))
buscar=True
for i in range(len(list_data)):
    if id == list_data[i][2]
    buscar = True
    break

if buscar == True:
    print("Usuario registrado")
else:
    print("Usuario NO registrado")



    
