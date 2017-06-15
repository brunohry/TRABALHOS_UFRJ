# Trabalho 9.2 por: Bruno Hryniewicz dos Santos Cruz
# Algoritimo Chines
def mdcCompleto(a,b,):
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
		#tratando o caso do print quando r==0 
		if r[i+1]==0:
			print r[i+1],q,' - - '
                        print x[i+1],y[i+1]
                        return [x[i+1],y[i+1]]
		else:
			print r[i+1],q,x[i+2],y[i+2]
		#andand de linha na tabela (transformando linha atual na linha de cima
                i=i+1
		a=b
		b=r[i]
def AlgoChines ():
	nums,mods =input()
	resps=[]
	respsMod=[]
	indice=0
	while indice<len(nums)-1:
		alfaEBeta=mdcCompleto(mods[indice],mods[indice+1])
		respsMod.append(mods[indice]*mods[indice+1])
		resps.append((nums[indice]*alfaEBeta[1]*mods[indice+1]+nums[indice+1]*alfaEBeta[0]*mods[indice])%respsMod[indice])
		print resps[indice], respsMod[indice]
		mods[indice+1]=respsMod[indice]
		nums[indice+1]=resps[indice]
		indice+=1
		



#recebe o numero de repeticoes 
n = input()
#loop principal
for i in range (n) :
        AlgoChines()
        print'---'





