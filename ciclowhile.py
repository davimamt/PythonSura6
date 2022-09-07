#CICLO MIENTRAS 

#Declarar un variable centinela o de control para evalar la ejecución de mi ciclo

i = 0
import math

#MENU DE OPCIONES
print("****** MENÚ *******")
print("1. sumar 2 numeros")
print("2. Restar 2 numeros")
print("3. craiz cuadrada")
print("4. Multiplicar 2 numeros")
print("5. Salir")

#programar la estructura del ciclo mientras

while(i != 5):
    i= int(input("Digite una opcion del menu: "))
    n1=int(input("Digite el primer numero "))
    n2=int(input("Digite el segundo numero "))
    if(i==1):
        print("sumar 2 numeros")
        print(n1+n2)
    elif(i==2):
        print("Restar 2 numeros")
        print(n1-n2)
    elif(i==3):
        print("raiz cuadrada")
        print("la raiz del numero 1 es ",math.sqrt(n1))
        print("la raiz del numero 1 es ", math.sqrt(n2))
    elif(i==4):
        print("Multiplicar 2 numeros")
        print(n1*n2)
    elif(i==5):
        break
    else:
        print("Digita una opcion valida")
    

print("Salimos del While")