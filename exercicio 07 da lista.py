# -*- coding: utf-8 -*-
"""
@author: Guilherme P. RA: 112679
"""

import math
print("esse programa calcula os ângulos diretores e o módulo de um determinado valor")
print("Para utilizar, ensira todas as coordenadas na mesma linha, separado por vírgula, exemplo:\nVetor 1: 1,2,3")

#Obtenção das coordenadas
v1 = input("Digite as coordenadas do vetor 1: ").split(",")

#Função que calcula a hipotenus (modulo) do vetor dado
def Hipotenusa():
   return ((float(v1[0])**2) + (float(v1[1])**2) + (float(v1[2])**2))**0.5

#Função que calcula o cosseno do vetor i
def Cosseno(i):
    Cos = float(v1[i])/Hipotenusa()
    return Cos

#Imprimindo os resultados
print("\nO primeiro angulo em graus é: " + str(round(math.degrees(math.acos(Cosseno(0))), 2)))
print("O primeiro angulo em graus é: " + str(round(math.degrees(math.acos(Cosseno(1))), 2)))
print("O primeiro angulo em graus é: " + str(round(math.degrees(math.acos(Cosseno(2))), 2)))
