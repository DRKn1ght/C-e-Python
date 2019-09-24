# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 23:32:46 2019

@author: guipa
"""
import math
n = 0
continuar = 1
AB = [0,0,0]
AC = [0,0,0]
v1 = eval(input("Digite as coordenadas do ponto A:\n"))
v2 = eval(input("Digite as coordenadas do ponto B:\n"))
t = float(input("Digite a área do triângulo:\n"))
v3 = [0,0,1]
print("A = (", v1[0], v1[1], v1[2],")")
print("B = (", v2[0], v2[1], v2[2],")")
print("C = (", v3[0], v3[1], "z",")")

#Calcula a distância entre A-B e A-C
while (n < 3):
    AB[n] = v2[n] - v1[n]
    AC[n] = v3[n] - v1[n]
    n += 1

#Calcula o produto vetorial
i = (AB[1] * AC[2]) - (AB[2] * AC[1])
j = (AB[2] * AC[0]) - (AB[0] * AC[2])
k = (AB[0] * AC[1]) - (AB[1] * AC[0])

#Resolve a equação utilizando a área do triângulo
r = (t*2)**2
r = r-(k**2)
r = r/(i**2 + j**2)

#Imprime o resultado
if (v1[1] != 0 or v1[2] != 0):
    print("\nPara que A pertença ao eixo 0x, sua coordenada Y e Z deve ser 0, digite uma coordenada de A válida.")
    continuar = 0
    
if (v2[0] != 0 or v2[2] != 0):
    print("\nPara que B pertença ao eixo 0y, sua coordenada X e Z deve ser 0, digite uma coordenada de B válida.")
    continuar = 0
    
if (r < 0):
    if (k < 0):
        k = k*-1
    print("\nImpossível formar um triângulo dos respectivos pontos com essa área. Digite uma área maior que", round(k/2,2))
    continuar = 0
    
if (continuar == 1):
    r = math.sqrt(r)
    v3[2] = r
    print("\nAs coordenadas de C são: (", v3[0], v3[1], round(v3[2], 2),") ou (", v3[0], v3[1], -round(v3[2],2), ")")

