#!/usr/bin/python2
# Laboratorio 14.2 : Bruno Hryniewicz dos Santos Cruz

from math import sqrt

import math 
def fermat(a):
    x=int(math.sqrt(a))
    y=0
    while (x**2-y**2!=a):
        print x,y,'N'
        x=x+1
        y=int(math.sqrt(x**2-a))
        if x==(a+1)/2:
            print 1,a
            return
    if (x**2-y**2==a):
        print x,y,'S'
    print x-y,x+y
    return(x-y, x+y)

def mdcCompleto(a,b):
    #definindo x e y iniciais
    x=[1,0]
    y=[0,1]
    #printando as duas primeiras linhas
    print a,'-',x[0],y[0]
    print b,'-',x[1],y[1]
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
        #tratando o caso do print quando r==0 e calculando a diofantina
        if r[i+1]==0:
            print r[i+1],q,' - - '
            return x[i+1]
        else:
            print r[i+1],q,x[i+2],y[i+2]
        #andand de linha na tabela (transformando linha atual na linha de cima
        i=i+1
        a=b
        b=r[i]

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
    print r


def BreakRSA ():
    n,e,b=input()
    p,q=fermat(n)
    fi= (p-1)*(q-1)
    print fi
    d = mdcCompleto(e, fi) % fi
    print d
    PotencializaModulo(b,d,n)


#recebendo a quantidade de numeros
x=input()
#loop principal
for i in range (x):
    #recebendo numeros
    BreakRSA()
    print'---'

