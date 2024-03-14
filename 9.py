#Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.

def un_pais_america(pais):
    return pais.lower() in ["argentina","bolivia","brasil","chile","colombia","costa rica","cuba","ecuador","el salvador","guatemala","hati","honduras","mexico","nicaragua","panama","paraguay","peru","republica dominicana","uruguay","venezuela","guayana francesa","puerto rico"]

