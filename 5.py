5. #Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.
a=float(input("Digite un primer número\n" ))
b=float(input("Digite un segundo numero\n"))
c=float(input("Digite un ultimo numero\n"))
if a+b > c:
    print("El resultado de "+str(a)+" mas "+str(b)+" es mayor que "+str(c) )
elif a+b < c:
    print("El resultado de "+str(a)+" mas "+str(b)+" es menor que "+str(c) )
else:
    print("El resultado de "+str(a)+" mas "+str(b)+" es menor que "+str(c) )
