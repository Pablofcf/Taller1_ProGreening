a = int(input("Digite un numero: "))
b = int(input("Digite otro numero: "))

if a%2==0 and b%2==0:
    print("Ambos numeros son pares")
elif a%2==0 and b%2!=0:
    print(f"{a} es par")
elif a%2!=0 and b%2==0:
    print(f"{b} es par")
else:
    print("Ambos numeros son impares")