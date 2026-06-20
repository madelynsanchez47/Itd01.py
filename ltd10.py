# Lista vacia donde se guardan los dias
dias = []

# Variables donde se almacenaran la suma de las temperaturas
sumaTempMaximas = sumaTempMinimas = 0

# Preguntamos la cantidad de dias a ingresar
n = int(input("¿Cuantos dias desea ingresar? "))

# Leemos las temperaturas de cada dia 
for i in range(n):
    print(f"\nDia {i+1}:")
    dia = input("Nombre del dia: ")
    maxima = float(input("Temperatura maxina: "))
    minima = float(input("Temperatura minima: "))
    dias.append((dia, maxima, minima))

    #Sumamos las temperaturas maximas y minimas 
    sumaTempMaximas += maxima
    sumaTempMinimas += minima

    # Mostramos el promedio de las temperaturas maximas y minimas 
    print(f"Promedio temperaturas maximas: {sumaTempMaximas/n}")
    print(f"Promedio temperaturas minimas: {sumaTempMinimas/n}")

    # Mostramos los dias con diferencias de temperaturas > 10
    for i in range(n):
        if dias[i][1] - dias[i][2] > 10:
            print(dias[i])

#Variables para guardar el día más caliente y más frío
diaCaliente = dias[0]
diaFrio = dias[0]

for i in range(n):
    if dias[i][1] > diaCaliente[1]:
        diaCaliente = dias[i]
    if dias[i][2] < diaFrio[2]:
        diaFrio = dias[i]

#Mostramos resultados
print(f"Día más caliente: {diaCaliente[0]} con {diaCaliente[1]}°")
print(f"Día más frío: {diaFrio[0]} con {diaFrio[2]}°")