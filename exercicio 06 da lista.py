# -*- coding: utf-8 -*-
"""
@author: Guilherme P. RA: 112679
"""

import math

#Cabeçário
print("Esse programa calcula as medidas dos três angulos internos de um triangulo qualquer.\nO usuário irá fornecer os vértices e o programa fará o resto.\n")
print("Para utilizar, ensira todas as coordenadas na mesma linha, separado por vírgula, exemplo:\nVetor 1: 1,2,3")

#Obtenção das coordenadas dos vérticies 1, 2 e 3
v1 = input("Digite as coordenadas do vértice 1: ").split(",")
v2 = input("Digite as coordenadas do vértice 2: ").split(",")
v3 = input("Digite as coordenadas do vértice 3: ").split(",")

#Função que calcula a distancia entre um vértice 1 e 2
def calcDist(v1, v2):
    Dist = float(v2[0]) - float(v1[0]), float(v2[1]) - float(v1[1]), float(v2[2]) - float(v1[2])
    return Dist

#Função que calcula a hipotenus (modulo) entre o vertice 1 e 2
def Hipotenusa(v1, v2):
   dist = calcDist(v1, v2)
   return ((dist[0]**2) + (dist[1]**2) + (dist[2]**2))**0.5

#Função que calcula o produto escalar entre três vértices
def ProdEscalar(v1, v2, v3):
    Dist1 = calcDist(v1, v2)
    Dist2 = calcDist(v1, v3)
    return ((Dist1[0]*Dist2[0]) + (Dist1[1]*Dist2[1]) + (Dist1[2]*Dist2[2]))

#Função que calcula os angulos
def Cosseno():
    Escalar1 = ProdEscalar(v1, v2, v3)
    Escalar2 = ProdEscalar(v2, v1, v3)
    Escalar3 = ProdEscalar(v3, v2, v1)
    Cos = Escalar1/(Hipotenusa(v1, v2) * Hipotenusa(v1, v3)), Escalar2/(Hipotenusa(v2, v1) * Hipotenusa(v2, v3)), Escalar3/(Hipotenusa(v3,v2) * Hipotenusa(v1, v3))
    return Cos

#Imprimindo os resultados obtidos
print("\nO primeiro angulo em graus é: " + str(round(math.degrees(math.acos(Cosseno()[0])), 2)))
print("O segundo angulo em graus é: " + str(round(math.degrees(math.acos(Cosseno()[1])), 2)))
print("O terceiro angulo em graus é: " + str(round(math.degrees(math.acos(Cosseno()[2])), 2)))