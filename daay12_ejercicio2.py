# Nivel 2
import random
import string 
# Ejercicio 1
def lista_colores_hexadecimales(cantidad):
    colores = []
    for _ in range(cantidad):
        color_hex = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colores.append(color_hex)
    return colores

print("list_of_hexa_colors"(3))


#2 Lista RGB
def list_of_rgb_colors(n):
    colores = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores.append(f"rgb({r},{g},{b})")
    return colores

print(list_of_rgb_colors(3))