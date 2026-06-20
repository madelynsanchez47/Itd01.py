estudiantes = {
    "Maria": [8, 9, 7, 10],
    "Joshua": [9, 8, 8, 7],
    "Ingrid": [10, 9, 9, 8]
}

for nombre, notas in estudiantes.items():
    promedio = sum(notas) / 4
    print(nombre, "promedio:", promedio)