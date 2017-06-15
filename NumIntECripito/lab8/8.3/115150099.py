# Trabalho 2 por: Bruno Hryniewicz dos Santos Cruz
# Teorema de Korselt
def Korselt(n,fatores):
    for i in fatores:
        if ((n-1)%(i-1)!=0)or(n%(i**2)==0 or n==i):
            print 'NAO'
            return
    print'SIM'

def fatora(a,fatores):
    fator=2
    #iniciando uma lista
    i=0
    while fator<=a:
        if a%fator==0:
            a=a/fator
            fatores.append(fator)
        else:
            fator=fator+1
        i=i +1
    #ordenando lista
    # contando e imprimindo
    i=0
    #excluindo o zero usado para iniciar a lista
    cont=1
    while i<len(fatores)-1:
        if fatores[i]==fatores[i+1]:
            cont=cont+1
        else:
            print fatores[i],cont
            cont=1
        i=i+1
    # tratando o caso dos ultimo print
    print fatores[i],cont

n=input();
#loop principal
for i in range (n) :
        a=input()
        fatores=[]
        fatora(a,fatores)
        Korselt(a,fatores)

        print'---'


