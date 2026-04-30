"""l1 = float(input("Ingrese primer lado: "))
l2 = float(input("Ingrese segundo lado: "))
l3 = float(input("Ingrese tercer lado: "))

if L1== l2 and l2 == L3:
    print("El triángulo es equilátero.")
elif l1 == l2 or l2 == l3:
    print("El triángulo es isóceles.")
else:
    print("El triángulo es escaleno")"""

"""num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número "))
num3 = float(input("Ingrese el tercer núnero"))

sumatoria = num1 + num2 + num3
promedio = sumatoria / 3 
print("La media de los números es : " , promedio)"""

"""materias = ["matematicas", "fisica", "quimica", "historia", "lenguaje", "programacion"]
notas = []
for i in range(len("asignaturas")):
    notas.append(float(input("Ingrese la nota de: "+ materias [i] + " : ")))

for nota in notas: 
    print(materias [i], notas [i])"""


"""articulos = []
precios = []
while True:
    articulo = input("ingrese el articulo : ")
    if articulo == "Fin":
        break
    articulos.append(articulo)
    precios.append(input("Ingrese el precio: "))

    carrito_de_compra = {
        "articulos":articulos,
        "precios": precios
    }
print(carrito_de_compra)"""

empleados = []
while True:
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        nombre = input("Ingrese su nombre: ")
        salario = input("Ingrese su salario: ")
        cargo = input("Ingrese su cargo: ")
        empleados.append([nombre, cargo , salario])
    elif opcion == 2 :
        print(empleados)
    elif opcion == 3:
        break






 
