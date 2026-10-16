primeraNota = int(input("Ingrese una calificacion: "))
primeraNotaPeso = int(input("Ingrese el peso de la calificacion anterior: "))
primeraNotaPeso = primeraNotaPeso / 100

segundaNota = int(input("Ingrese una calificacion: "))
segundaNotaPeso = int(input("Ingrese el peso de la calificacion anterior: "))
segundaNotaPeso = segundaNotaPeso / 100

terceraNota = int(input("Ingrese una calificacion: "))
terceraNotaPeso = int(input("Ingrese el peso de la calificacion anterior: "))
terceraNotaPeso = terceraNotaPeso / 100

promedioPonderado = ((primeraNota * primeraNotaPeso) + (segundaNota * segundaNotaPeso) + (terceraNota * terceraNotaPeso) / (primeraNotaPeso + segundaNotaPeso + terceraNotaPeso))


print(f"El promedio ponderado es {promedioPonderado:.2f}")