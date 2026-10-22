import numpy as np
# Johan Paulo Aros NC 0016
# Ejemplos de numpy
print(" -- Especiado Linealmente en array -- 0016")
arre = np.linspace(start=0, stop=5,num=10)
print(arre)
print(" -- Especiado identidad en 2D array -- 0016")
matrix = np.eye(3)
print(matrix)
print("-- Genera numeros al azar (Aleatorios) en 2D array -- 0016")
numale=np.random.random((3,4)) # genera 12 numeros aleatorios
print(numale)
print("genera 9 numeros aleatorios entre el 0 y el 1")
numale=np.random.random((3,3)) # genera 9 numeros aleatorios
print(numale)
# como generar 9 numeros aleatorios comprendidos entre el 1 y 20
# con numpy en un arreglo de 3 por 3
print("Genera 9 numeros aleatorios entre el 1 y el 20")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print (arre)
print("Johan Paulo Aros NC 0016")