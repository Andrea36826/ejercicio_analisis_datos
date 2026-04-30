def  calcular_total(precio,cantidad):
    monto = precio * cantidad
    return monto

def aplicarDescuento(monto):
    if monto >= 100000:
        subtotal = monto * 0.9

    else:
        subtotal = monto
    return subtotal

def calcular_iva(subtotal):
    total = subtotal * 1.19
    return total

precio = int(input("ingrese el precio: "))
cantidad =int(input("Ingrese la cantidad de productos: "))

calcular_total(precio,cantidad)

monto = calcular_total(precio,cantidad)
subtotal = aplicarDescuento(monto)
print("monto total: ", monto)
print("Monto con descuento: ", subtotal)
print("Total a pagar: ", total)