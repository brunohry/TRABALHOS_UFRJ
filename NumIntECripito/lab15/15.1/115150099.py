#!/usr/bin/python2
# Laboratorio 15.1 : Bruno Hryniewicz dos Santos Cruz

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

def Drecript ():
    p,a,s,t = input()
    SLinha=PotencializaModulo(s, (p-1-a),p)
    b=SLinha*t %p
    print b




#recebendo a quantidade de numeros
x=input()
#loop principal
for i in range (x):
	#recebendo numeros
	Drecript()
	print "---"



