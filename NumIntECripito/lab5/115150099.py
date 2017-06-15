# Trabalho 4 por: Bruno Hryniewicz dos Santos Cruz
# numeros altamente compostos 
import math
def contaDivisores(i):
    numDivisores=0
    aux=1
    while aux <= int (math.sqrt(i)):
        aux2=i/aux
        int(aux2)
        if (i-aux*aux2) ==0:
            if aux==aux2:
                numDivisores+=1
            else:
                numDivisores= numDivisores +2
        aux+=1
    return numDivisores


def altamenteComposto(n):
    vet=[1,2]
    vetDivisores=[1,2]
    vetResp=[1,2]
    cont=1
    while vet[cont]<=n:
        vet.append(vet[cont]+2)
        cont +=1
    cont =2
    armazena=0
    while cont<len(vet)-1:
        vetDivisores.append(contaDivisores(vet[cont]))
        if vetDivisores[cont]>armazena:
            vetResp.append(vet[cont])
            armazena= vetDivisores[cont]
        cont+=1

    print vetResp

k=input()
altamenteComposto(k)


  

