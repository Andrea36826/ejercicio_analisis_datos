"""import pandas

carros = ["Chevrolet" , "Mazda" , "Kia", "Renault"]
serie_carros = pandas.Series(carros)
print(serie_carros)
print(carros)"""

"""import pandas as pd
list_products = ["Lentejas", "Arroz", "Frijol", "Papa", "Yuca"]
serie_products = pd.Series(list_products)
product_inicial = serie_products[0]
product_final = serie_products[4]
print("producto inicial es" , product_inicial, "producto final es", product_final)"""

"""import pandas as pd
lista_nombres = ["Andrea", "Albeiro" , "Milena" , "Carlos" , "Jonier"]
indices = ["A","B","C","D","E"]
product_serie = pd.Series(lista_nombres, indices)
print(product_serie)
print(product_serie["C"])"""

"""import pandas as pd
lista_valores= [120,150,90,200]
lista_indices = ["Semana 1" , "Semana 2", "Semana 3" , "Semana 4"]
serie_data = pd.Series(lista_valores, lista_indices)

print(serie_data)"""
#ventas totales
"""ventas_totales = serie_data.sum()
print("ventas totales, ventas_totales")"""

#promedio ventas
"""prom_ventas = int(serie_data.mean())
print("Promedio ventas", prom_ventas)"""

#Mayor y menor venta

"""mayor_venta = serie_data.max()
menor_venta = serie_data.min()
print("Mayor venta: " , mayor_venta, " | Menor venta:" , menor_venta)"""

#semanas con mayor y menor venta

"""semana_mayor = serie_data.idxmax()
semana_min = serie_data.idxmin()
print("Semana mayor ventas: ", semana_mayor, "| Semana menor venta:" , semana_min)"""

#Serie aumentada

"""serie_aumentada = (serie_data * 1.1).astype(int)
print("Serie aumentada")
print(serie_aumentada)"""

#Data frame

"""import pandas as pd

data = {
    "Nombre":["Ana","Luis","Carlos"],
    "Edad" :[25,30,28],
    "Ciudad":["Bogotá", "Medellin", "Cali"]
}
df_data = pd.DataFrame(data)
print(df_data)"""


