# Trabalho 7 por: Bruno Hryniewicz dos Santos Cruz
# Calculo de inverso multiplicativo

#funcao executa  algoritmo de euclides completo e chama o inverso multi
def mdcCompletoEInversMulti(a,b):
	#definindo x e y iniciais
	x=[1,0]
	y=[0,1]
	mod=b
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
		#tratando o caso do print quando r==0 e calculando o inverso multiplicativo
		if r[i+1]==0:
			print r[i+1],q,' - - '
                        inversMulti(x[i+1],mod,r[i])
		else:
			print r[i+1],q,x[i+2],y[i+2]
		#andand de linha na tabela (transformando linha atual na linha de cima
                i=i+1
		a=b
		b=r[i]

#funcao para calcular o inverso multiplicativo
def inversMulti(alfa, mod , mdc):
	#caso de nao ter inverso multi
	if mdc !=1 :
		print 0
	else :
		print alfa%mod
    
    
#recebe o numero de repeticoes 
n = input()
#loop principal
for i in range (n) :
        a,b=input()
        mdcCompletoEInversMulti(a,b)
        print'---'


