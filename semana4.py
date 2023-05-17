# 1-Crea una función llamada suma que tome dos números como parámetros y
# devuelva la suma de ellos.

# def suma(a,b):
#     resultado= a+b
#     return resultado,"sumado"

# hacer= suma(3,1)
# print("la suma de ambos numeros es  "  , hacer)

# 2-Crea una función llamada saludo que tome el nombre de una persona como
# parámetro e imprima un saludo personalizado.


# def saludo(isaaco):
# # definicion 1
#     print (f"hola querido {isaaco}  como estas hoy?")

# saludo("astor")

# def saludar(nombre, edad):
#     print(f" hola  {nombre} cómo estás hoy?, tu añitos son {edad}  ")
# # definicion 2
# ingresa_nom= input(" escribe tu nombres:  ")
# ingresa_edad= input(" dime tus añitos son  años: ")
# saludar(ingresa_nom, ingresa_edad)



# 3-Crea una función llamada invertir_cadena que tome una cadena de texto como
# parámetro y devuelva la cadena invertida.

def invertir_cadena(texto):
    textos= texto[::-1]
    return textos

escribe= input("escribe un teexto:  ")
print(f"vos ingresaste  { escribe} , lo pasaremos a su version inversa")
invertir_cadena(escribe)
print(f" tu texto inverso es {invertir_cadena(escribe)}")


# 4-Crea una función llamada es_capicua que tome un número como parámetro y
# devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
# derecha a izquierda) y False en caso contrario.
# 5-Crea una función llamada es_divisible que tome dos números enteros como
# parámetros y devuelva Es divisible si el primer número es divisible por el
# segundo número, o No es divisible en caso contrario.
# 6-Crea una función llamada es_par que tome un número como parámetro y
# devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
# devuelva Es impar o No es par.
# 7-Crea una función llamada imprimir_pares que tome un número entero como
# parámetro y imprima todos los números pares desde 1 hasta ese número.
# 8-Crea una función llamada es_palindromo que tome una cadena de texto como
# parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
# de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
# contrario.
# 9-Crea una función llamada promedio que tome una lista de números como
# parámetro y devuelva el promedio de esos números.
# 10-Crea una función llamada calcular_factorial que tome un número entero como
# parámetro y devuelva el factorial de ese número. El factorial de un número
# entero positivo n se define como el producto de todos los números enteros
# positivos desde 1 hasta n.
# 11-Crea una función llamada contar_vocales que tome una cadena de texto como
# parámetro y devuelva el número de vocales que contiene.
# 12-Crea una función llamada convertir_temperatura que tome una temperatura
# en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
# es: Fahrenheit = (Celsius * 9/5) + 32.
# 13-Crea una función llamada calcular_descuento que tome dos parámetros:
# precio y porcentaje_descuento. La función debe calcular y devolver el precio
# después de aplicar el descuento.
# 14-Crea una función llamada encontrar_maximo que tome una lista de números
# como parámetro y devuelva el número máximo de la lista.
# 15-Crea una función llamada contar_palabras que tome una cadena de texto
# como parámetro y devuelva el número de palabras que contiene. Se considera
# que las palabras están separadas por espacios.
# 16-Crea una función llamada eliminar_duplicados que tome una lista como
# parámetro y devuelva una nueva lista sin duplicados, conservando el orden
# original.
# 17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
# parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
# letras pero en distinto orden), o False en caso contrario.
# 18-Crea una función llamada calcular_mayor_diferencia que tome una lista de
# números como parámetro y devuelva la mayor diferencia entre el numero mas
# alto y el numero mas bajo en la lista.
# 19-Crea una función llamada es_bisiesto que tome un año como parámetro y
# devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año
# es bisiesto si es divisible por 4, pero no por 100, a menos que también sea
# divisible por 400.