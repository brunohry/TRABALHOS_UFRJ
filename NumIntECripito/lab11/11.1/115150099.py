#!/usr/bin/python2
# Laboratorio 11.1 : Bruno Hryniewicz dos Santos Cruz

#funcao executa  algoritmo de euclides completo e chama o inverso multi
def mdc(a,b):
    #definindo x e y iniciais
    x=[1,0]
    y=[0,1]
    mod=b
    #printando as duas primeiras linhas
    #recebendo valor de r para q=0
    r=[b]
    #contador 
    i=0
    while r[i]>0:
        #obtendo e printando de uma linha q, r ,x, y
        q=a/b
        r.append(a%b)
        x.append(x[i]-x[i+1]*q)
        y.append(y[i]-y[i+1]*q)
        #tratando o caso do print quando r==0 e calculando o inverso multiplicativo
        if r[i+1]==0:
            inv=inversMulti(x[i+1],mod,r[i])
            return(r[i], inv)
        #andand de linha na tabela (transformando linha atual na linha de cima
        i=i+1
        a=b
        b=r[i]

#funcao para calcular o inverso multiplicativo
def inversMulti(alfa, mod , mdc):
    #caso de nao ter inverso multi
    if mdc !=1 :
        return 0
    else :
        return alfa%mod


def totiente (n):
    lista=[]
    for i in range (1,n):
        a,b =  mdc(i,n)
        if a==1:
            lista.append(i)
    return lista

def subgrupo():
    num,teste=input()
    mod=num
    grup = totiente(num)
    if (len(grup)%len(teste)!=0):
        print "NAO"
        return
    if (not (1 in teste)):
        print "NAO"
        return
    for i in teste:
        for j in teste:
            if not ((i*j)%mod in teste):
                print "NAO"
                return
            a,b= mdc(i,mod)
        if not b in teste:
            print"NAO"
            return 

    print"SIM"


#recebendo a quantidade de numeros
x=input()
#loop principal
for i in range (x):
    #recebendo numeros
    subgrupo()

