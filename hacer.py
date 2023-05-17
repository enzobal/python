
# texto = input("Ingresa un texto: ").lower()
# letras = list(input("Ingresa tres letras separadas por coma: ").lower().split(","))

# # Contar la cantidad de veces que aparece cada letra
# cantidades = {}
# if "a" in letras:
#     cantidades["a"] = texto.count("a")
#     print(cantidades)
# if "b" in letras:
#     cantidades["b"] = texto.count("b")
#     print(cantidades)
# if "c" in letras:
#     cantidades["c"] = texto.count("c")
#     print(cantidades)

texto = list(input("ingresa un texto cabezon  ").lower())
letras=list(input("ingresa 3 letras sin espacios  ").lower())
# print(letras)
print(letras[0])

l1=letras[0]
if l1 in letras:
    l1= texto.count(l1)
    print(l1, f"cantidad de veces que aparece {letras[0]}")

l2= letras[1]
if l2 in texto:
    l2= texto.count(l2)
    print(l2, " es as veces que aparece")
# print(letras[0])
# cantidades ={}
# l1=letras[0]
# if l1 in letras:
#     cantidades[l1]= texto.count(l1)
#     print(cantidades[l1])
    
    
# hola mundo

# 1- Cantidad de veces que aparece cada una de letras 
# que eligió.
# Tip 1: almacenar las letras en una lista para 
# usar algún método de contar un substring en un
# string
# Tip 2: al buscar las letras puede haber mayúscula
#y minúsculas. Para asegurar que se
# encuentren todas las letras, pasa tanto el texto
# original como las letras a buscar a
# minúscula.

# Métodos y propiedades de string.
# Indexar estructuras de datos.
# Todos los tipos de datos.
# Desafío 2: Analizador de textos
# Requisitos técnicos:
# Se te pide crear un programa que le pida al usuario
# que ingresar un texto
# cualquiera, por ejemplo, un artículo o una frase.
# Luego el programa le va a pedir al usuario que
# también ingrese 3 letras a su
# elección.
# Nuestro código va a procesar esa información para realizar los análisis
# necesarios para devolverle al usuario la siguiente información:
