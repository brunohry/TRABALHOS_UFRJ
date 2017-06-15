#trabalho 1 por: Bruno Hryniewicz dos Santos Cruz
#Algoritimo da divisao simples

#funcao de disisao
def divide (a ,b):
	#atribuindo q e r
	q=0
	r=a
	#printando  q e r ao passo de q++
	while r >= b:
		r= a - b * q
		print q, r
		q=q+1
		
#recebendo numero de repeticoes
n = input()
#loop principal
for i in range (n) :
	a,b=input()
	print''
	divide(a,b)
	print'---'

	





