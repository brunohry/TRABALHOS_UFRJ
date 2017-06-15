#!/usr/bin/python2
# Laboratorio 14.1 : Bruno Hryniewicz dos Santos Cruz

from math import sqrt

def M (p):
	m=2**p-1
	print m
	return m


def FatoresDeM ():
	num = input()
	num_M=M(num)
	r_max= int ((int(sqrt(2**num))-1)/(2*num))
	print r_max
	for p in range (1, r_max + 1):
		print p
		mod = 1 + 2*num*p
		r = PotencializaModulo(2,num, mod)
		if r == 1 :
			print mod
			return
	print  num_M	


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


#recebendo a quantidade de numeros
x=input()
#loop principal
for i in range (x):
    #recebendo numeros
    FatoresDeM()
    print'---'

