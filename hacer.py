texto = input("ingresa un texto cabezon").lower().split()
letras_usuario =input("ingresa 3 letras con espacios de por medio").lower().split()
print(letras_usuario)
cantidades ={}
 if letras_usuario[0] in texto:
     cantidades[letras_usuario[0]] = texto.count(letras_usuario[0])


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
