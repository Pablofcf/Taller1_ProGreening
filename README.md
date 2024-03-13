# Taller1_ProGreening
1. Realice el quiz Python Beginner Quiz (20 preguntas) y adjunte pantallazo con el resultado (mínimo 90% bien).
![Quiz ProGreening](https://github.com/Pablofcf/Taller1_ProGreening/assets/159049788/e2229855-3e9a-43a6-9c9a-3b5d0cf38959)

2. Realice un programa que lea tres números reales y determine cuál es el mayor.
```python
a = int(input("Digite un numero: "))
b = int(input("Digite un numero: "))
c = int(input("Digite un numero: "))

if a>=b and a>=c:
    print(f"El numero mayor es {a}")
elif b>=a and b>=c:
    print(f"El numero mayor es {b}")
elif c>=a and c>=b:
    print(f"El numero mayor es {c}")
```
3. Realice un programa que lea un número enteros y determine si es par o impar.
```python
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
```
