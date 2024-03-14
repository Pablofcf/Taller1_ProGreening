#Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.

x = float(input("Digite un numero en Hz segun la frecuencia de onda entre 30e+18 y 30e+3: "))
if x >= 30e+18:
    print("La frecuencia de onda esta en Rayos Gamma")
elif x >= 30e+15 and x < 30e+18:
    print("La frecuencia de onda esta en Rayos X")
elif x >= 7.89e+14 and x < 30e+15:
    print("La frecuencia de onda esta en Ultravioleta")
elif x >= 384e+12 and x < 1.5e+15:
    print("La frecuencia de onda esta en Espectro visible")
elif x >= 300e+9 and x < 384e+12:
    print("La frecuencia de onda esta en Infrarrojo")
elif x >= 3e+8 and x < 300e+9:
    print("La frecuencia de onda esta en Microondas")
elif x >= 30e+3 and x < 3e+8:
    print("La frecuencia de onda esta en Onda larga de radio")
elif x < 30e+3:
    print("La frecuencia de onda esta en Muy baja frecuencia de radio")