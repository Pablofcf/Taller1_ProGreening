4. #Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
num1=int(input("ingresa un numero real 1\n"))
num2=int(input("ingresa un numero real 2\n"))
if num1 % num2 == 0 :
   print("el numero 1 es multiplo del numero 2")
elif num2 % num1 == 0:
 print("el numero 2 es multiplo del numero 1")  
else:
  print("niguno de los dos numeros el multiplo del otro numero")