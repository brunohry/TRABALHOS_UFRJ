# Trabalho 2 por: Bruno Hryniewicz dos Santos Cruz
# Fatoracao por algoritimo de Fermat
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

n=input();
#loop principal
for i in range (n) :
        a=input()
        fermat(a)
        print'---'


