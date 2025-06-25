#ejercicio 2 
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

edades.sort()
edad_min = min(edades)
edad_max = max(edades)
print("Edades ordenadas:", edades)
print("Edad mínima:", edad_min)
print("Edad máxima:", edad_max)

edades.append(edad_min)
edades.append(edad_max)
print("Lista con edades añadidas:", edades)

edades.sort()
n = len(edades)
if n % 2 == 0:
    mediana = (edades[n//2 - 1] + edades[n//2]) / 2
else:
    mediana = edades[n//2]
print("Mediana:", mediana)

promedio = sum(edades) / len(edades)
print("Promedio:", promedio)

rango = edad_max - edad_min
print("Rango de edades:", rango)

print("abs(mín - promedio):", abs(edad_min - promedio))
print("abs(máx - promedio):", abs(edad_max - promedio))


#paises 
paises = ['China', 'Rusia', 'EEUU', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

n = len(paises)
if n % 2 == 0:
    medio = paises[n//2 - 1:n//2 + 1]
else:
    medio = [paises[n//2]]
print("País(es) del medio:", medio)

mitad = n // 2
if n % 2 == 0:
    primera_mitad = paises[:mitad]
    segunda_mitad = paises[mitad:]
else:
    primera_mitad = paises[:mitad + 1]
    segunda_mitad = paises[mitad + 1:]
print("Primera mitad:", primera_mitad)
print("Segunda mitad:", segunda_mitad)

pais1, pais2, pais3, *paises_escandinavos = paises
print("Primer país:", pais1)
print("Segundo país:", pais2)
print("Tercer país:", pais3)
print("Países escandinavos:", paises_escandinavos)


