# -*- coding: utf-8 -*-
"""
@author: Guilherme P. RA: 112679
"""

print("\nEsse programa calcula o produto vetorial de qualquer vetor em três dimensões.\nPara utilizar, ensira todas as coordenadas na mesma linha, separado por vírgula, exemplo:\nVetor 1: 1,2,3")

#Declaração das variáveis
Dimens = 3
Result2 = []

#Obtenção das cooredenadas e do valor de K
v1 = input("Digite as coordenadas do vetor 1: ").split(",")
k = float(input("Digite o valor de K ; u*v=k: "))

#Função para fazer o cálculo
def Calcular():
    global index
    global Result
    
    #Loop que calcula o produto escalar
    while index < Dimens:
        Result += float(v1[index])*float(v1[index])
        index += 1
    index = 0
    x = k/Result
    
    #Loop que calcula as coordenadas do vetor V em 3 dimensões
    while index < Dimens:
        Result2.append(float(v1[index])*x)
        Result2[index] = round(Result2[index], 3)
        index += 1
    print(str("O vetor V é: " + str(Result2)))
    
#Chamando a função acima
Calcular()