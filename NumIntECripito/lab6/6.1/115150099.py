# Trabalho 6.1 por: Bruno Hryniewicz dos Santos Cruz
# Operacoes modulares
def OperaModulo ():
    a,b,mod=input()
    #forma reduzida de a
    reduA= a%mod
    #forma reduzida de b
    reduB= b%mod
    #forma reduzida da soma
    reduSoma= (a+b)%mod
    #forma reduzida da diferenca
    reduDife= (a-b)%mod
    #forma reduzida do produto
    reduProdu= (a*b)%mod

    print reduA, reduB, reduSoma, reduDife, reduProdu

n=input();
#loop principal
for i in range (n) :
        OperaModulo()


