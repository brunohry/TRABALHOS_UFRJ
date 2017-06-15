# Trabalho 2 por: Bruno Hryniewicz dos Santos Cruz
# MDC por Algoritmo Euclidiano

#funcao recursiva de do algoritmo de euclides
def mdc(a,b):
	print a
	r=b
	#se resto ==0 parar a recursao
	if r==0:
		print b
		return
	#se nao, devolve b como a, e b como a modulo b (resto) 
	else:
		mdc (b,a%b)

#recebe o numero de repeticoes 
n = input()
#loop principal
for i in range (n) :
        a,b=input()
        mdc(a,b)
        print'---'

