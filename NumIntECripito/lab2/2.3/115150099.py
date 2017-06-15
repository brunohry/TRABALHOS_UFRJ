# Trabalho 3 por: Bruno Hryniewicz dos Santos Cruz
# MDC por Algoritmo Euclidiano Completo

#funcao executa  algoritmo de euclides completo
def mdcCompleto(a,b):
	#definindo x e y iniciais
	x1=1
	x2=0
	y1=0
	y2=1
	#printando as duas primeiras linhas
	print a,'-',x1,y1
	print b,'-',x2,y2
	#recebendo valor de r para q=0
	r=b
	while r>0:
		#obtendo e printando de uma linha q, r ,x, y
		q=a/b
		r=a%b
		x=x1-x2*q
		y=y1-y2*q
		#tratando o caso do print quando r==0
		if r==0:
			print r,q,' - - '
		else:
			print r,q,x,y
		#andand de linha na tabela (transformando linha atual na linha de cima)
		x1=x2
		x2=x
		y1=y2
		y2=y
		a=b
		b=r

#recebe o numero de repeticoes 
n = input()
#loop principal
for i in range (n) :
        a,b=input()
        mdcCompleto(a,b)
        print'---'


