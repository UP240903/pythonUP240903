# Nivel 3
import math
from statistics import mean, median, variance, stdev
from collections import Counter
# Ejercicio_1
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Ejercicio_2
def elementos_son_unicos(lista):
    return len(lista) == len(set(lista))

# Ejercicio_3
def todos_mismo_tipo(lista):
    return all(type(x) == type(lista[0]) for x in lista)

# Ejercicio_4
def es_nombre_variable_valido(nombre):
    return nombre.isidentifier()