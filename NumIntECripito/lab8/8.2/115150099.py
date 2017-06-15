# Trabalho 8.2 por: Bruno Hryniewicz dos Santos Cruz
# teste baseado no Teorema de Fermat


def TesteDeFermat ():
    n,base=input()
    mod=n
    r=1
    a=base
    e=n-1
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
    if r==1:
        print 'INCONCLUSIVO'
    else:
        print 'COMPOSTO'




n=input();
#loop principal
for i in range (n) :
        TesteDeFermat()
        print '---'
