var_digitada = input("Digite su edad:  ")
var_edad = int(var_digitada)
if(not(var_digitada =="")):
    if(var_edad < 0):
        print("edad incorrecta, no puede ser negativa")
    elif(var_edad == 0):
        print("La edad es incorrecta y debe ser mayor a cero")
    elif(var_edad > 0 and var_edad < 18):
        print("es niño o joven no mayor de edad")
else:
    print("no puede ser vacio")

if(var_edad < 0 or var_edad == 0):
        print("edad incorrecta, no puede ser negativa")
elif(var_edad > 0 and var_edad < 18):
    print("es niño o joven no mayor de edad")
