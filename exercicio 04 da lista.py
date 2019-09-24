# -*- coding: utf-8 -*-
"""
@author: Guilherme P. RA: 112679
"""


import numpy
print("Este programa resolve o exercício 07 da lista 02 de maneira geral.")
print("Para utilizar, ensira todas as coordenadas na mesma linha, separado por vírgula, exemplo:\nVetor 1: 1,2,3")
#Declaração das variáveis
index = 0
d = 3
i = 0

#Obtenção das coordendas e os valores de k1, k2 e k3 respectivamente
u = input("Digite a coordenada v1: " ).split(",")
v = input("Digite a coordenada v2: " ).split(",")
w = input("Digite a coordenada v3: " ).split(",")
k1 = int(input("Digite o valor de k1: " ))
k2 = int(input("Digite o valor de k2: " ))
k3 = int(input("Digite o valor de k3: " ))

#Loop que faz a conversão de texto para float dos vetores
while index < d:
    u[index] = float(u[index])
    v[index] = float(v[index])
    w[index] = float(w[index])
    index += 1

#Função da biblioteca Numpy que fará as matrizes e os calculos
A = numpy.array([u,v,w])
B = numpy.array([[k1],[k2],[k3]])
x = numpy.linalg.solve(A,B)

#Imprimindo os resultados obtidos
print("A matriz dos coeficientes é\n" + str(A))
print("O vetor coluna é\n" + str(B))
print("o valor de x é ",x[0][0])
print("o valor de y é ",x[1][0])
print("o valor de z é ",x[2][0])

