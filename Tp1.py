# Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_a_decimal(romano):
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if romano == "":
        return 0

    if len(romano) == 1:
        return valores[romano]

    if valores[romano[0]] < valores[romano[1]]:
        return -valores[romano[0]] + romano_a_decimal(romano[1:])
    else:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
# Prueba
print(romano_a_decimal("XIV"))

"""
El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
para encontrarlo;
c. Utilizar un vector para representar la mochila.
"""

def usar_la_fuerza(mochila, sacados=0):
    # Caso base: mochila vacía
    if len(mochila) == 0:
        return False, sacados

    # Tomo el primer objeto
    objeto = mochila[0]
    print("Se sacó:", objeto)

    # Caso base: se encuentra el sable
    if objeto == "sable de luz":
        return True, sacados + 1
    else:
        # Caso recursivo
        return usar_la_fuerza(mochila[1:], sacados + 1)


# Prueba
mochila = ["comida", "capa", "mapa", "sable de luz", "botella"]

encontrado, cantidad = usar_la_fuerza(mochila)

if encontrado:
    print("\nSe encontró el sable de luz.")
    print("Objetos sacados:", cantidad)
else:
    print("\nNo se encontró el sable de luz.")
    print("Objetos revisados:", cantidad)