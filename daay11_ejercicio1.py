# Level 1
import math
# Ejercicio_1
def sumar_dos_numeros(a, b):
    return a + b

# Ejercicio_2
def area_circulo(r):
    return math.pi * r * r

# Ejercicio_3
def sumar_todos(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    return "Todos los argumentos deben ser números"

# Ejercicio_4
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

# Ejercicio_5
def determinar_estacion(mes):
    mes = mes.lower()
    if mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    elif mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    else:
        return 'Mes inválido'

# Ejercicio_6
def calcular_pendiente(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Ejercicio_7
def resolver_ecuacion_cuadratica(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "No hay raíces reales"
    elif d == 0:
        raiz = -b / (2 * a)
        return (raiz,)
    else:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        raiz2 = (-b - math.sqrt(d)) / (2 * a)
        return (raiz1, raiz2)

# Ejercicio_8
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

# Ejercicio_9
def invertir_lista(lista):
    return lista[::-1]

# Ejercicio_10
def capitalizar_elementos(lista):
    return [elemento.capitalize() for elemento in lista]

# Ejercicio_11
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista


# Ejercicio_13
def suma_numeros(n):
    return sum(range(n + 1))

# Ejercicio_14
def suma_impares(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# Ejercicio_15
def suma_pares(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)