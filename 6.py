6. #Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
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