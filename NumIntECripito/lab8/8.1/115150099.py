# Trabalho 8.1 por: Bruno Hryniewicz dos Santos Cruz
# Algoritmo de Potenciacao Modular auxiliado pelo Teorema de Fermat


def PotencializaModulo ():
    base,exp,mod=input()
    exp = exp % (mod-1)
    r=1
    a=base
    e=exp
    print e
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




n=input();
#loop principal
for i in range (n) :
        PotencializaModulo()
        print '---'

