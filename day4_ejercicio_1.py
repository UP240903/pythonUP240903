#conectar cadena 
cadena_1="treinta"
cadena_2="dias"
cadena_3="de"
cadena_4="python"
print(cadena_1 +" "+ cadena_2 +" "+ cadena_3 +" "+ cadena_4  )

cadena__1="codificaion"
cadena__2="para"
cadena__3="todos"
print(cadena__1+" "+ cadena__2+" "+ cadena__3 )
#declarar vairble 
Compañia=("codificaion para todos ")
print(Compañia)
#logitud de la cadena compañia
print(len(Compañia))
#cambiar todos los caracteres a mayusculas 
print(Compañia.upper())
#cambiar todos los caracteres a minuscula
print(Compañia.lower())
#usar capitalzer(), title(), swapcase() para formatear el valor
print(Compañia.capitalize())
print(Compañia.title())
print(Compañia.swapcase())
# cortar la primera palabra de la cadena 
sin_primera_palabra_de_la_cadena=Compañia[11:]
print(sin_primera_palabra_de_la_cadena)
#comprobar si la cadena contien la palabra codificacion 
print(Compañia.find("Codificacion"))
print("codificacion " in Compañia)

#remplazar codificacion para python
texto1= "codificacion para todos".replace("codificacion", "python")
print(texto1)
#cambiar python para todas a python para todos 
texto2="python para todas".replace("todas", "todos")
print(texto2)

palabras= "codificacion para todos ".split()
print(palabras)

empresas= "facebook, google, microsoft, apple, ibm, oracel, amazon".split(",")
print(empresas)

cadena= "codificadion para todos" 
print(cadena [0])
print(len(cadena)-1)
print(cadena[10])

palabraa1= "python para todas".split()
acronimo1="".join([palabra[0]for palabra in palabraa1]).upper()
print(acronimo1)

palabras2="codificacion para todos".split()
acronimo2="".join([palabras[0]for palabras in palabras2]).upper()
print(acronimo2)

print("codificacion para todos".index("c"))

print("codificacion para todos".index("f"))
print("codificacion para todas las personas".rfind("1"))

frase="no puedes terminar una oracion porque porque porque es una conjucion "
print(frase.find("porque"))
print(frase.rindex("porque"))

inicio=frase.find("porque")
fin=frase.rindex("porque")+ len("porque")
print(frase[inicio:fin])
print("codificacion poara todos".startswith("codificaion"))

print("codificacion para todos ".endswith("codificacion"))
texto_espacios="   codificacion para todos   "
print(texto_espacios.strip())

print("30diasdepython".isidentifier())
print("treita_dias_de_python".isidentifier())

librerias=["django", "frasco", "botella", "piramide", "halcon"]
unidas=" # ".join(librerias)
print(unidas)

print ("yo amo python:/es un lenguaje poderoso./nIdeal para principales.")







