

# Métodos y propiedades de string.
# Indexar estructuras de datos.
# Todos los tipos de datos.

# Desafío 2: Analizador de textos
# Requisitos técnicos:
# Se te pide crear un programa que le pida al usuario que ingresar un texto
# cualquiera, por ejemplo, un artículo o una frase.
# Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
# elección.
# Nuestro código va a procesar esa información para realizar los análisis
# necesarios para devolverle al usuario la siguiente información:

# 1- Cantidad de veces que aparece cada una de letras que eligió.
# Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
# string
# Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
# encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
# minúscula.
# 2- Cuantas palabras hay en total en todo el texto.
# Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.
# 3- Cual es la primera letra y cuál es la última. (Indexación)
# 4- Mostrar el texto en orden inverso.
# 5- Decir si la palabra "python" aparece en el texto.
# Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
# string para mostrar al usuario.


print("Ingresar un texto cualquiera, por ejemplo, un artículo o una frase.")
texto = input("Ingrese el texto: ") # Igresar un texto
texto_minusculas = texto.lower()
print("Ahora ingrese tres letras diferentes, para analizar si las mismas aparecen en el texto")
letra1 = input("Ingrese la primer letra:" )
letra1_minuscula = letra1.lower()
letra2 = input("Ingrese la segunda letra:" )
letra2_minuscula = letra2.lower()
letra3 = input("Ingrese la tercera letra:" )
letra3_minuscula = letra3.lower()

aparece_letra1 = 0
for letra in texto_minusculas:
    if letra == letra1_minuscula:
        aparece_letra1 +=1
if aparece_letra1 != 0:
    print(f"La letra {letra1_minuscula}, aparece en el texto: {aparece_letra1} veces ")
else: print(f"La letra {letra1_minuscula}, no aparece en el texto")

aparece_letra2 = 0
for letra in texto_minusculas:
    if letra == letra2_minuscula:
        aparece_letra2 +=1
if aparece_letra2 != 0:
    print(f"La letra {letra2_minuscula}, aparece en el texto: {aparece_letra2} veces ")
else: print(f"La letra {letra2_minuscula}, no aparece en el texto")

aparece_letra3 = 0
for letra in texto_minusculas:
    if letra == letra3_minuscula:
        aparece_letra3 +=1
if aparece_letra3 != 0:
    print(f"La letra {letra3_minuscula}, aparece en el texto: {aparece_letra3} veces ")
else: print(f"La letra {letra3_minuscula}, no aparece en el texto")







lista_del_texto = texto_minusculas.split()
print("La cantidad de palabras en el texto es de: ",len(lista_del_texto),"palabras.")





primer_palabra_texto = lista_del_texto[0]
ultima_palabra_texto = lista_del_texto[-1]
print(f"La primer palabra del texto es:{primer_palabra_texto}\nLa última palabra del texto es: {ultima_palabra_texto}")






texto_invertido = texto[::-1] # Invertimos el texto completo, en modo espejo.
print(f"El texto inverso, quedaría:\n {texto_invertido}")






x = texto_minusculas.find("python") # Busca la palabra Python.
if x != -1:
    print("La palabra python se encuentra en el texto")
else: 
    print("La palabra python no se encuentra en el texto")
# Participantes: Enzo Balbani, Leandro Matias, Matias Arroyo, Carlos Gomez, Luis Lopez, Fraco Rios lanco, Edgardo Fernandez.

var = "python"in texto

dir= { True: verdadero,  False: falso}
print(f"python se enceuntra en {dir[var]}")

if "python" in texto:
print("La palabra python aparece en el texto")
else: "La palabra python no aparece en el texto"

lista_texto=texto_rev.split("")
lista_texto.reverse()
texto_rev = "".join(lista_texto)
print(texto_rev)


# Pedir al usuario el texto y las letras a buscar
texto = input("Ingresa un texto: ").lower()
letras = input("Ingresa tres letras separadas por coma: ").lower().split(",")

# Contar la cantidad de veces que aparece cada letra
cantidades = {}
if "a" in letras:
    cantidades["a"] = texto.count("a")
if "b" in letras:
    cantidades["b"] = texto.count("b")
if "c" in letras:
    cantidades["c"] = texto.count("c")

# Imprimir los resultados
print("Cantidad de veces que aparece cada letra:")
if "a" in cantidades:
    print(f"a: {cantidades['a']}")
if "b" in cantidades:
    print(f"b: {cantidades['b']}")
if "c" in cantidades:
    print(f"c: {cantidades['c']}")