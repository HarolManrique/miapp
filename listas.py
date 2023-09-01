lenguajes = ["Python","Csharp", "PHP","GO","JAVA","Javascript"]
"""print(lenguajes)
print(lenguajes[2]) #IMPRIME LA POSICION DADA
lenguajes[2] = "C++" # CAMBIA EL VALOR DE LA POSICION DE LA LISTA 
print(lenguajes)
print(lenguajes[-1]) # IMPRIME LA LISTA DE DERECHA A IZQUIERDA
print(lenguajes[1:3]) # IMPRIME LAS POSCIONES DADAS EN LA LISTA SIN INCLUIR LA ULTIMA POSICION DADA
print(lenguajes[:3]) #IMPRIME TOD0 HASTA LA POSICION ANTERIOR A LA 3
print(lenguajes[1:]) #IMPRIME DE LA POSICION 1 Y COMO DESPUES DEL PUNTO NO HAY VALOR, IMPRIME TOD0"""

"""lenguajes.insert(3,"Cobol") 
print(lenguajes)

lenguajes.insert(0,"Pascal")

lenguajes.remove("PHP")
print("PHP" in lenguajes) #COMPROBAR SI UN VALOR ESTA EN LA LISTA
print(lenguajes)
"""
"""lenguajes.append("C") #AÑADIR UN VALOR AL FINAL DE LA LISTA
print(lenguajes)
print(len(lenguajes))
"""
#TUPLAS

"""tupla = ("C++",True,25) #LAS TUPLAS SE USAN PARA CREAR DATOS FIJOS QUE NO SE MODIFICAN, Y SE CREAN CON EL (TUPLA) Y NO CON EL [LISTA]
print(tupla[1]) #MUESTRA LA POSICION DEL ELEMENTO EN LA TUPLA
print(tupla.count(True)) #cuenta LAS VECES QUE ESTA EL VALOR DADO
print(tupla.index(25)) #MUESTRA LA POSICION DEL VALOR DADO
"""

#ARREGLOS MULTIDIMENSIONALES

"""
lenguajes2 = ["Python","Csharp", "PHP","GO","JAVA","Javascript"]
personas = [[1,"Carlos",25], [2,"Tomas",15], [3,"Mauricio",36]] #cada corchete es una posicion 
personas = [[1,"Carlos",25], [2,"Tomas",15[25,25,"Galan"]], [3,"Mauricio",36]] #cada corchete es una posicion 
print(personas) #imprime la lista multidimensional
print(personas[1])  #imprime los datos de la posicion 1
print(personas[1][1]) #imprime de la posicion 1, el valor de la posicion interna 1
personas[1][2] = 13 # cambia el valor del elemento de una posicion determinada
print(personas[1])
"""

#ARRAYS

array_datos = [[]]              #Crea un arreglo de datos
array_datos[0].append(1)        #Añade un valor al areglo de la posicion 0
array_datos[0].append("Harol")
array_datos[0].append(17)
print(array_datos)

array_datos.append([])              #añade un nuevo arreglo ala rray
array_datos[1].append(2)            ##Añade un valor al areglo de la posicion 1
array_datos[1].append("Tomas")
array_datos[1].append(35)
tamano = len(array_datos)
if(tamano==50):
    print("sale llena")

if (len(array_datos)==50):
    print("Lista llena")
print(array_datos[1])
