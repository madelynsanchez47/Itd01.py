#lista donde se guardaran los estudiantes
estudiantes = []

promedioGeneral = 0

#preguntamos cuantos estudiantes se registraran
n = int(input("¿Cuantos estudiantes desea registrar?"))

#leer datos de los estudiantes
for i in range(n):
    print(f"\nEstudiante {i+1}:")

    nombre = input("Nombre:")
    notas = []
    suma = 0

    #pedir las 4 notas
    for j in range(4):
        nota = float(input(f"Ingrese la nota {j+1}:"))
        notas.append(nota)
        suma += nota

    promedio = suma / 4

    estudiantes.append({
        "nombre": nombre,
        "notas": notas,
        "promedio": promedio
    })

    promedioGeneral += promedio

#buscar mejor y peor promedio
mejor = estudiantes[0]
peor = estudiantes[0]

for i in range(n):
    if estudiantes[i]["promedio"] > mejor["promedio"]:
        mejor = estudiantes[i]

    if estudiantes[i]["promedio"] < peor["promedio"]:
        peor = estudiantes[i]

#mostrar resultados
print("\nMejor promedio:")
print(mejor)

print("\nPeor promedio:")
print(peor)

print("\nEstudiantes aprobados:")

for i in range(n):
    if estudiantes[i]["promedio"] >= 70:
        print(estudiantes[i]["nombre"], estudiantes[i]["promedio"])

#promedio general del curso
promedioGeneral = promedioGeneral / n

print(f"\nPromedio general del curso: {promedioGeneral}")