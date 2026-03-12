
print

#1)Crea un programa que calcule el promedio de las 3 calificaciones de la pelicula
#(enteros entre 1 y 10) en IMDB para “Flow” ingresados por el usuario

calificaciones_usuario=[]
suma_calificaciones= 0
while len(calificaciones_usuario) <= 2:
    calificaciones=int(input("Introducir calificacion del 1 al 10: "))
    if calificaciones >=1 and calificaciones <=10:
        calificaciones_usuario.append(calificaciones)
    else:
        print("Debes ingresar una nota del 1 al 10")
for calificaciones in calificaciones_usuario:
    suma_calificaciones+=calificaciones
promedio= int(suma_calificaciones/len(calificaciones_usuario))
print("El promedio es",promedio)

#2)Modifica el programa para pedir a un robot C1 que siga haciendo choripán
#mientras un cliente sigue diciendo "si". Este programa ahora solo puede hacer
#choripán 2 veces como máximo.
contador=0
while contador !=2:
    res = input("¿Quieres más choripán?")
    if res == "si":
        print("C1, haz un choripán!")
        contador+=1
print("Es el maximo de CHORIPAN")

#3)Crea un programa que determine si cada entero entre N y M es un par o impar. P.ej.,
#Ingresa un entero (valor menor): 2      Ingresa otro entero (valor mayor): 4
#2 par      3 inpar 4 par
N=int(input("Ingrese un numero menor "))
M=int(input("Ingresa un numero mayor "))
valor_inicial=N
while valor_inicial <= M:
    if valor_inicial%2==0:
        print("Par")
    else:
        print("Impar")
    valor_inicial+=1

