# Trabalho 2 por: Bruno Hryniewicz dos Santos Cruz
# Fatoracao por algoritimo ingenuo

def fatora(a):
    fator=2
    #iniciando uma lista
    fatores=[0]
    i=0
    while fator<=a:
        if a%fator==0:
            a=a/fator
            fatores.append(fator)
        else:
            fator=fator+1
        i=i +1
    #ordenando lista
    fatores.sort()
    # contando e imprimindo
    i=0
    #excluindo o zero usado para iniciar a lista
    del fatores[0]
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
        fatora(a)
        print'---'


