#2) [Nivel 2] Crea una función es_primo(x) que determine si un número x es primo. Si es un número primo, retorna True, de lo contrario, retorna     False.
#Asumimos que x dado es un entero positivo.
#que es un numero primo?: entero que solo es divisible por si mismo y uno
#como se cuando se cumplen esos parametros? si es divisible por otro numero no es primo y se retorna a falso je

def es_primo(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

numero=int(input("Ingrese numero entero je "))

print(es_primo(numero))
