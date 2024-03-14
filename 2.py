2. #Realice un programa que lea tres números reales y determine cuál es el mayor.

a = int(input("Digite un numero: "))
b = int(input("Digite un numero: "))
c = int(input("Digite un numero: "))

if a>=b and a>=c:
    print(f"El numero mayor es {a}")
elif b>=a and b>=c:
    print(f"El numero mayor es {b}")
elif c>=a and c>=b:
    print(f"El numero mayor es {c}")