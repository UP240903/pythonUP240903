# Día 12 – Nivel 1
import random
import string
# Ejercicio 1
def id_usuario_aleatorio():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Ejercicio 2
def generar_ids_por_usuario():
    longitud = int(input("Ingresa el número de caracteres por ID: "))
    cantidad = int(input("Ingresa la cantidad de IDs a generar: "))
    for _ in range(cantidad):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=longitud)))

# Ejercicio 3
def generar_color_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
