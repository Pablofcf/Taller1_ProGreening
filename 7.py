7. #Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:El promedio, la mediana, el promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos), ordenar los números de forma ascendente, ordenar los números de forma descendente, la potencia del mayor número elevado al menor número y la raíz cúbica del menor número
a=float(input("Piense en un numero y digitelo: \n"))
b=float(input("Digite un numero completo y seguido del dia, mes y año de su nacimiento\nejemplo, dia 19 mes 10 año 2005, numero resultante 19102005: \n"))
c=float(input("Digite su edad sumando el año en el que estamos: \n"))
d=float(input("digite un numero re random: \n"))
e=float(input("Preguntele a su amigo un numero mayor a 500 y escribalo: \n"))

promedio : float = (a+b+c+d+e)/5
print("El promedio de los numeros es: ", promedio)

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if a > d:
    a, d = d, a
if a > e:
    a, e = e, a
if b > c:
    b, c = c, b
if b > d:
    b, d = d, b
if b > e:
    b, e = e, b
if c > d:
    c, d = d, c
if c > e:
    c, e = e, c
if d > e:
    d, e = e, d

print("La mediana del conjunto es ", c)


promediomultiplicativo = a*b*c*d*e**(1/5)
print("El promedio multiplicativo es ", promediomultiplicativo)

potencia: float = e**a
print("potencia del mayor número elevando el menor número es: ",potencia)

print("La lista en orden ascendente es: ",a,b,c,d,e)
print("La lista en orden descendente es: ",e,d,c,b,a)

raiz = a**(1/3)
print("La raiz cubica del menor es: ", raiz)