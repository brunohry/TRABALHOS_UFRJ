#!/usr/bin/python2
# Laboratorio 12 : Bruno Hryniewicz dos Santos Cruz
def fatora(a):
    fator=2
    #iniciando uma lista
    fatores=[]
    fatoresnew=[]
    i=0
    while fator<=a:
        if a%fator==0:
            a=a/fator
            fatores.append(fator)
        else:
            fator=fator+1
        i=i +1
    i=0
    #excluindo o zero usado para iniciar a lista
    cont=1
    while i<len(fatores)-1:
        if fatores[i]==fatores[i+1]:
            cont=cont+1
        else:
            print fatores[i],cont
            fatoresnew.append(fatores[i])
            fatoresnew.append(cont)
            cont=1
        i=i+1
    # tratando o caso dos ultimo print
    print fatores[i],cont
    fatoresnew.append(fatores[i])
    fatoresnew.append(cont)
    return fatoresnew
def PotencializaModulo (base,exp,mod):
    r=1
    a=base
    e=exp
    while e!=0:
        if (e%2)!=0:
            print r,a,e,'S'
            r=(r*a)%mod
            e=(e-1)/2
        else:
            print r,a,e,'N'
            e=e/2
        a=(a*a)%mod
    print r,a,e,'N'
    return r

def Fermat(n):
	return 2**(2**n)+1

def Pepin ():
    n=input()
    fermat=Fermat(n)
    print fermat
    x=PotencializaModulo(5,(fermat-1)/2,fermat)
    if x!=1 and x**2%fermat==1:
        print "PRIMO"
    else:
        print "COMPOSTO"
    





#recebendo a quantidade de numeros
x=input()
#loop principal
for i in range (x):
    #recebendo numeros
    Pepin()
    print '---'

