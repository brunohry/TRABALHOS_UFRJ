#!/usr/bin/python2
# Laboratorio 10.1 : Bruno Hryniewicz dos Santos Cruz
#funcao recursiva de do algoritmo de euclides
def mdc(a,b):
	while True:
		if b==0:
			return a
		#se nao, devolve b como a, e b como a modulo b (resto) 
		else:
			aux=a
			a=b
			b=aux%b

def totiente (n):
	lista=[]
	for i in range (1,n):
		a =  mdc(i,n)
		if a==1:
			lista.append(i)
	print lista

#recebendo a quantidade de numeros
x=input()
#loop principal
for i in range (x):
	#recebendo numeros
	a=input()
	totiente(a)



