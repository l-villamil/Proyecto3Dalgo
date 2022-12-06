#Daniel Villar González, 201923374
#Leonidas Villamil, 202013910
#Yesid Almanza, 201921773

import sys

def funcionPrincipal(m,k):
    matriz = [0]*(m+1)
    respuesta = 0
    for i in range(0,m+1):
        matriz[i] = [0]*(m+1)      
    j = k
    while j < len(matriz):
        i = 0 
        while i < len(matriz):
            if i == 0:
                matriz[i][j]=0
            elif j == 0:
                matriz[i][j]=0
            elif j>i:
                matriz[i][j]=0
            elif j == 1:
                matriz[i][j]=1
            elif j == k:
                if i % k == 0:
                    matriz[i][j]=1
                else:
                    matriz[i][j]=0
            else:
                for x in range(1, i//j+1):
                    matriz[i][j] += matriz[i-x*j][j-1]
            i+=1
        respuesta += matriz[i-1][j]
        j+=1
    return respuesta


numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    case_list = list(map(str, sys.stdin.readline().split()))
    m = int(case_list[0])
    k = int(case_list[1])
    print(funcionPrincipal(m,k))