# Nivel 3
import random
import string

# Ejercicio 1
def mezclar_lista(lista):
    lista_mezclada = lista[:]
    random.shuffle(lista_mezclada)
    return lista_mezclada

# Ejercicio 2
def numeros_aleatorios_unicos():
    return random.sample(range(10), 7)