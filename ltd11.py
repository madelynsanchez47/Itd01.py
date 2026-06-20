#diccionario donde se guardaran los contactos
contactos = {}

#preguntamos cuantos contactos desea ingresar
n = int(input("¿Cuantos contactos desea agregar?"))

#leemos cada contacto y lo guardamos en el diccionario
for i in range(n):
    print(f"\nContacto {i+1}:")

    nombre = input("Nombre:")
    telefono = input("Telefono:")
    email = input("Email:")
    ciudad = input("Ciudad:")

    contactos[nombre] = {
        "telefono": telefono,
        "email": email,
        "ciudad": ciudad
    }

#preguntamos una ciudad
buscarCiudad = input("\nIngrese una ciudad para buscar contactos:")

print(f"\nContactos de la ciudad {buscarCiudad}:")

for nombre in contactos:
    if contactos[nombre]["ciudad"].lower() == buscarCiudad.lower():
        print(nombre, contactos[nombre])

#mostrar el contacto con el nombre mas largo
nombreLargo = ""

for nombre in contactos:
    if len(nombre) > len(nombreLargo):
        nombreLargo = nombre

print("\nContacto con el nombre mas largo:")
print(nombreLargo, contactos[nombreLargo])

#preguntar un nombre para eliminar
eliminar = input("\nIngrese el nombre del contacto que desea eliminar:")

if eliminar in contactos:
    del contactos[eliminar]
    print("Contacto eliminado")
else:
    print("El contacto no existe")

#mostrar agenda final
print("\nAgenda final:")

for nombre in contactos:
    print(nombre, contactos[nombre])