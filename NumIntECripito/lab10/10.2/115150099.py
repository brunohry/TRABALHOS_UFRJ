#!/usr/bin/python2
# Laboratorio 10.2 : Bruno Hryniewicz dos Santos Cruz

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
def fi ( a ):
	fat=[]
	expoentes=[]
	x=1
	lista = fatora(a)
	for i in range (0,len(lista), 2):
		x=x*(lista[i]**((lista[i+1]-1)))*(lista[i]-1)
	print x



#recebendo a quantidade de numeros
x=input()
#loop principal
for i in range (x):
	#recebendo numeros
	a=input()
	fi(a)
	print "---"



