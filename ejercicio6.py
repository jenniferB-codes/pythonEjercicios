montoARetirar = int(input("Ingrese un monto: "))

billetesDisponibles = [50, 20, 10, 1]


contador = 0

cantidadBillete50 = 0
cantidadBillete20 = 0
cantidadBillete10 = 0
cantidadMoneda1 = 0

for i in billetesDisponibles:

    if i == 50:
        cantidadBillete50 = montoARetirar // 50
        contador = cantidadBillete50 * 50
        montoARetirar = montoARetirar - contador

        
    elif i == 20 and montoARetirar >= 20:
        cantidadBillete20 = montoARetirar // 20
        contador = cantidadBillete20 * 20
        montoARetirar = montoARetirar - contador


    elif i == 10 and montoARetirar >= 10:
        cantidadBillete10 = montoARetirar // 10
        contador = cantidadBillete10 * 10
        montoARetirar = montoARetirar - contador

    elif i == 1:
        cantidadMoneda1 = montoARetirar // 1
        contador = cantidadMoneda1 * 1
        print(contador)
        montoARetirar = montoARetirar - contador


print(f"la cantidad de billete de $50 que puedes retirar es", cantidadBillete50)
print(f"la cantidad de billete de $20 que puedes retirar es", cantidadBillete20)
print(f"la cantidad de billete de $10 que puedes retirar es", cantidadBillete10)
print(f"la cantidad de monedas de $1 que puedes retirar es", cantidadMoneda1)




