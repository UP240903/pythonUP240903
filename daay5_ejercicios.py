#lista vacia 
lista_vacia=[]

frutas=["manzana", "platan" ,"mango" ,"naranja0", "uva" , "piña " ]

print(len(frutas))
print("primero:",frutas[0])
print("medio:", frutas[len(frutas)//2])
print("ultimo:", frutas[-1])

mixed_data_types=["john doe", 30, 1.75, "single", "123 main st"]

compañias=["faceboock ", "google ", "microsoft", "apple ", "ibm", "oracle ", "amazon"]
print[compañias]

print(len(compañias))


print("primra compañia", compañias[0])
print("compañia del medio ", compañias[len(compañias)//2])
print("ultima compañia", compañias[-1])

compañias[1]= "alfabeto"
print("lista modificada:", compañias)

compañias.append("spotify")
print("despues agregar:", compañias)

compañias.insert(len(compañias)//2, "tesla")
print("despues de insertar en el medio :", compañias)

compañias[0]=compañias[0].upper()
print("compañias en mayusculas:",compañias)

unidas="#;".join(compañias)
print("compañias unidas :",compañias)

print("¿esta amazon en la lista?", "amazon"in compañias)

compañias.sort()
print("lista ordenada:", compañias)

compañias.reverse()
print("lista de orden decendente :",compañias)

print("primeras 3 emprezas:", compañias[3])

print("ultimas 3 compañias :", compañias[-3])

medio=len(compañias)//2
if len(compañias)%2==0:
   print("compañias del medio:", compañias[medio-1:medio+1])
else:
    print("compñias del medio", compañias[medio])

compañias.pop(0)
print("Después de eliminar la primera:", compañias)

medio = len(compañias) // 2
compañias.pop(medio)
print("Después de eliminar la del medio:", compañias)

compañias.pop()
print("Después de eliminar la última:", compañias)

compañias.clear()
print("Lista vacía:", compañias)

del compañias

frontend = ['HTML', 'CSS', 'JS', 'React', 'Redux']
backend = ['Node', 'Express', 'MongoDB']
pila_completa = frontend + backend
print("Pila completa:", pila_completa)

indice = pila_completa.index('Redux')
pila_completa.insert(indice + 1, 'Python')
pila_completa.insert(indice + 2, 'SQL')
print("Pila completa actualizada:", pila_completa)



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


