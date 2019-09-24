# -*- coding: utf-8 -*-
"""
@author: Guilherme P. RA: 112679
"""
print("Esse programa calcula o produto vetorial de qualquer vetor em qualquer dimensão.\nPara utilizar, ensira todas as coordenadas na mesma linha, separado por vírgula, exemplo:\nVetor 1: 1,2,3")

# Declaração das variáveis
v1 = []
v2 = []
ii = 0
result = 0

# Obtendo informações como o número de dimensões e as coordenada dos vetores
Dimens = input("Em qual dimensão você deseja trabalhar?\n")
v1 = input("Digite as coordenadas do vetor 1: ").split(",") # .split irá separar as coordenadas
v2 = input("\nDigite as coordenadas do vetor 2: ").split(",")

# Função que faz o cálculo do produto escalar
def ProdutoEscalar(v1, v2):
    # Declaração das variáveis que serão utilizadas dentro do While
    global ii
    global result
    
    # Loop que irá calcular o produto escalar em qualquer dimensão que o usuário escolher.
    while int(ii) < int(Dimens):
        result += float(v1[ii]) * float(v2[ii])
        ii += 1
    return result;

# Fazendo Call na função acima
PE = ProdutoEscalar(v1,v2)

# Imprimindo o resultado
print("O produto escalar de " + str(v1) + str(v2) + " = " + str(result))