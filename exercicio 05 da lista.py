# -*- coding: utf-8 -*-
"""
@author: Guilherme P. RA: 112679
"""
import math

print("Esse programa receberá dois vetores em 3 dimensões e irá calcular o angulo entre eles\n")
print("Para utilizar, ensira todas as coordenadas na mesma linha, separado por vírgula, exemplo:\nVetor 1: 1,2,3")

#Declaração das variáveis
index = 0
d = 3

#Obtenção das coordenadas dos vetores 1 e 2
v1 = input("Digite as coordenadas do vetor 1: ").split(",")
v2 = input("Digite as coordenadas do vetor 2: ").split(",")

#Loop que irá converter os vetores de string para float
while index < d:
    v1[index] = float(v1[index])
    v2[index] = float(v2[index])
    index += 1

#Função que calcula o módulo de V
def calcModulo(v):
    return ((v1[0]**2) + (v1[1]**2) + (v1[2]**2))**0.5

#Função que calcula o produto escalar
def calcProdEscalar():
    return (v1[0]*v2[0])+(v1[1]*v2[1])+(v1[2]*v2[2])

#Obtendo o cosseno do angulo
cos = calcProdEscalar()/(calcModulo(v1) * calcModulo(v2))

#Imprimindo o resultado em graus
print("O angulo é: " + str(round(math.degrees(math.acos(cos)), 2)))