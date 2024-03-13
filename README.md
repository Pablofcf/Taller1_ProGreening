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
4. Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
```python
num1=int(input("ingresa un numero real 1\n"))
num2=int(input("ingresa un numero real 2\n"))
if num1 % num2 == 0 :
   print("el numero 1 es multiplo del numero 2")
elif num2 % num1 == 0:
 print("el numero 2 es multiplo del numero 1")  
else:
  print("niguno de los dos numeros el multiplo del otro numero")
```
5. Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.
```python

```
6. Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
```python
def una_vocal(letra):
  #def_define una nueva variable
  return letra.lower() in ["a","e","i","o","u"]
  # []es una  lista  a la cula podemos accerder cuando necesitamos
  # return_indica el final de la función y continúa la ejecución del programa tras la llamada a la función y el lower me indica que este en minuscula 
  #ademas el in devuelve True si un elemento se encuentra dentro de otro
letra = input('Ingresa una letra por favor: ')
if una_vocal(letra):
  print("es  una vocal")
else:
  print("Es una consonante")
```


