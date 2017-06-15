# Trabalho 1 por: Bruno Hryniewicz dos Santos Cruz
# MDC por Algoritmo Euclidiano Completo + eq. diofantina

#funcao executa  algoritmo de euclides completo e chama a diofantina
def mdcCompletoEDiofantina(a,b,c):
	#definindo x e y iniciais
	x=[1,0]
	y=[0,1]
	#printando as duas primeiras linhas
	print a,'-',x[0],y[0]
	print b,'-',x[1],y[1]
	#recebendo valor de r para q=0
	r=[b]
        #contador 
        i=0
	while r[i]>0:
		#obtendo e printando de uma linha q, r ,x, y
		q=a/b
		r.append(a%b)
		x.append(x[i]-x[i+1]*q)
		y.append(y[i]-y[i+1]*q)
		#tratando o caso do print quando r==0 e calculando a diofantina
		if r[i+1]==0:
			print r[i+1],q,' - - '
                        diofantina(x[i+1],y[i+1],c,r[i])
		else:
			print r[i+1],q,x[i+2],y[i+2]
		#andand de linha na tabela (transformando linha atual na linha de cima
                i=i+1
		a=b
		b=r[i]
#funcao para calcular eq diofantina
def diofantina(alfa, beta, c, mdc):
    if c%mdc==0:
        print alfa*c/mdc, beta*c/mdc
    else:
        print 0
    
#recebe o numero de repeticoes 
n = input()
#loop principal
for i in range (n) :
        a,b,c=input()
        mdcCompletoEDiofantina(a,b,c)
        print'---'


