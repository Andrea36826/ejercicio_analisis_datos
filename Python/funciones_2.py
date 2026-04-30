"""edades = [27, 35, 50, 15, 23]

def promediar():
    prom = int(sum(edades)/len(edades))
    return prom

def calcular_mayor():
    maximo = max(edades)
    return maximo

def calcular_minimo():
    minimo = min(edades)
    return minimo

promedio = promediar()
print("promedio: ", promedio)
edad_maxima = calcular_mayor()
print("edad maxima: ", edad_maxima)
edad_minina = calcular_minimo()
print("edad minima: ", edad_minina)"""

#diccionario

"""personas = {
    "Nombre": "Jonier",
    "Edad" : 28,
    "Profesión": "Ing",
    "Ciudad": "Bogotá"
} 
print(personas["Nombre"], personas["Edad"])"""

"""personas = {
    "Nombres": ["Jonier" , "Ana" , "Luis" , "Sofia" , "Juan" , "Alfredo"],
    "Edad": [32 ,30 , 24 , 40 , 20 , 36],
    "Profesion": ["ing" , "Admin" , "Cont" , "Med" , "Arq" , "Ing"],
    "Ciudad": ["Bogota" , "Funza" , "Mosquera" , "Manizales" , "Pereira" , "Medellin"]
    }

personas["Edad"][4] = 37
personas["Profesion"][4] = "Enfermero"
personas["Ciudad"][4] = "Choco"
personas["Genero"] = ["M" , "F" ,"M" , "F" , "M" , "M"]


for i in range(len(personas["Nombres"])):
    print(personas["Nombres"][i], personas["Edad"][i], personas["Profesion"][i], personas["Ciudad"][i], personas["Genero"][i])"""

carros = {
    "Marca": ["Susuki" , "Mazda" , "Chevrolet"],
    "Modelo":[2020 , 2021 , 2018],
    "Serie":["Swift" , "3" , "Spark"],
    "Motor":[1.2 , 1.8 , 1.0]
}

for i in range(len(carros["Marca"])):
    print(carros ["Marca"][i], carros ["Modelo"][i], carros["Serie"][i], carros["Motor"][i])

modelo = [2020 , 2021 , 2018]

def calcular_modelo_reciente ():
    modelo_reciente_ = max(carros["Modelo"]) 
    return modelo_reciente_

def calcular_modelo_antiguo():
    modelo_antiguo = min(carros["Modelo"])
    return min(carros[modelo])

def calcular_promedio():
    return round(sum(carros["Motor"]) / len (carros["Motor"]),1)

print("Modelo más reciente" , calcular_modelo_reciente())
print("Modelo más antiguo", calcular_modelo_antiguo())
print("Promedio motor" , calcular_promedio())