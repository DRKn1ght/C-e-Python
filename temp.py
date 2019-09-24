# -- coding: utf-8 --
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
v1 = [0,0]
v2 = [0,0]
v3 = [0,0]
vr = [0,0]
v1 = input("Digite as coordenadas do vetor 1:\n").split(",")
v2 = input("Digite as coordenadas do vetor 2:\n").split(",")
v3 = input("Digite as coordenadas do vetor 3:\n").split(",")
vo = input("Insira o dígito do vetor oposto:\n1: Vetor 1\n2: Vetor 2\n3: Vetor 3\n")
print("Vetor 1: (" + v1[0] + ", " +v1[1] +")")
print("Vetor 2: (" + v2[0] + ", " +v2[1] +")")
print("Vetor 3: (" + v3[0] + ", " +v3[1] +")")
print("Vetor oposto ao Vetor " + vo)
def subVectors(v1,v2, v3):
    vx = int(v1[0]) - int(v2[0])
    vy = int(v1[1]) - int(v2[1])
    vr[0] = int(v3[0]) + int(vx)
    vr[1] = int(v3[1]) + int(vy)
    return vr;
if vo == "1":
        vr = subVectors(v2,v1,v3);
        print("Vetor resultante: (" + str(vr[0]) + ", " + str(vr[1]) + ")")

if vo == "2":
        vr = subVectors(v1,v2,v3);
        print("Vetor resultante: (" + str(vr[0]) + ", " + str(vr[1]) + ")")

if vo == "3":
        vr = subVectors(v1,v3,v2);
        print("Vetor resultante: (" + str(vr[0]) + ", " + str(vr[1]) + ")")