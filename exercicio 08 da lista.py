# -*- coding: utf-8 -*-
"""
@author: Guilherme P. RA: 112679
"""
import math

#Obtenção dos angulos e do módulo
rad1 = float(input("Digite o primeiro ângulo diretor em radianos: "))
rad2 = float(input("Digite o segundo ângulo diretor em radianos: "))
rad3 = float(input("Digite o terceiro ângulo diretor em radianos: "))
mod = float(input("Digite o módulo do vetor: "))

#Função que transforma o rad em cos
def Cos(radx):
    return math.cos(radx)

#Função que obtém as coordenadas
def Coord(radx):
    return round(mod*Cos(radx),2)

#Colocando os resultados em uma cadeia (array)
coord = Coord(rad1), Coord(rad2), Coord(rad3)

#Imprimindo o resultado
print("\nA coordenada dos vetores é: " + str(coord))