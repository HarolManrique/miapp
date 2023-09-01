#def funcion_suma(numero1=0,numero2=1):         #se le asignan valores a las variables dentro de la funcion
def funcion_suma(numero1,numero2):           #Define una funcion que se ejecuta siempre y cuando llamemos la funcion y le asignemos valores
    print(numero1 + numero2)

"""opcion = int(input("Digite numero:   "))
if opcion > 5:                              #Por medio del IF le decimos a la funcion que se ejecute cuando un valor es mayor a 5.
    funcion_suma(5,3)

funcion_suma(5,)"""

"""
def cuenta_hacia_atras(numero):
    numero = numero -1      # o se puede escribir numero -= 1
    if(numero > 0):
        print("vamos en el numero:  ",numero)
        cuenta_hacia_atras(numero)
    else:
        print("termino")

numero_ingresado= int(input("Ingrese numero:   "))
cuenta_hacia_atras(numero_ingresado)
"""

def factorial(numero):
    if(numero > 1):
        numero = numero * factorial(numero - 1)
    return numero
print(factorial(3))
