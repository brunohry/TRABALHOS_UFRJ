# Trabalho 4 por: Bruno Hryniewicz dos Santos Cruz
# Crivo de eratostenes
import math
# inicia o vetor com todos os numeros impares de 3 ao limite dado
def iniciaVetor(limite, lista ):
    i=0
    while ((lista[i]+2)<=limite):
        lista.append(lista[i]+2)
        i+=1
#descobre a posicicao de inicio de corte de acorco com a 2 melhoria
def posicionaCorte(posicao, lista):
    return (lista[posicao]**2 - 3)/2

#realizando corte e imprimindo etapas
def corte (lista, listaMemoria, limite):
    #inicializando posicoes e lista de restantes
    posicao=0
    posicaoCorte=0
    listaRestantes=[]+lista
    #primeiro loop, avanca um na lista a cada rodada de corte
    #nele e! aplicada a primeira melhoria 
    while lista[posicao]<=int(math.sqrt(limite)):
        #ignora posicao cortada
        if lista[posicao]==0:
            posicao+=1
            continue
        #atribui a primeira posicao de corte
        posicaoCorte=posicionaCorte(posicao,lista)
        #print do valor de salto, valor do primeiro corte e posicao do primeiro corte 
        print lista[posicao], lista[posicaoCorte], posicaoCorte
        #inicia uma lista para por valores cortados a cada rodada 
        listaCortados=[]
        #segundo loop, anda do inicio do corte ao fim da lista, ao passo do valor de salto
        while posicaoCorte<len(lista):
            salto=lista[posicao]
            # usando lista memoria para poder utilizar valores ja cortados
            listaCortados.append(listaMemoria[posicaoCorte])
            #caso valor ainda nao tenha sido cortado la lista dos restantes
            if lista[posicaoCorte]!=0:
                listaRestantes.remove(listaMemoria[posicaoCorte])
            #cortando ( atribuindo 0 a um valor cortado)
            lista[posicaoCorte]=0
            posicaoCorte+=salto
        posicao+=1    
        print listaCortados
        print listaRestantes
    #adicionando o 2 ao inicio da lista
    listaRestantes=[2] + listaRestantes
    #printando os primos restantes
    print listaRestantes
        
def crivo(limite):
    lista=[3]
    iniciaVetor(limite, lista)
    #criando uma segunda lista para auxilio
    listaMemoria=[]+lista
    print lista
    print int(math.sqrt(limite))
    corte(lista,listaMemoria,limite)
limite=input()
crivo(limite)


