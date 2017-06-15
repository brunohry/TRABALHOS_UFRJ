# Trabalho 9.3 por: Bruno Hryniewicz dos Santos Cruz
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
def AlgoChines (nums , mods):
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
		
def fatora(a):
    fator=2
    #iniciando uma lista
    fatores=[]
    fatoresnew=[]
    i=0
    while fator<=a:
        if a%fator==0:
            a=a/fator
            fatores.append(fator)
        else:
            fator=fator+1
        i=i +1
    i=0
    #excluindo o zero usado para iniciar a lista
    cont=1
    while i<len(fatores)-1:
        if fatores[i]==fatores[i+1]:
            cont=cont+1
        else:
            print fatores[i],cont
            fatoresnew.append(fatores[i])
            cont=1
        i=i+1
    # tratando o caso dos ultimo print
    print fatores[i],cont
    return fatores

def PotencializaModulo (base,exp,mod):
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
    return r

def AlgoChinesPotenciasMod():
	base,exp,mod=input()
	mods=fatora(mod)
	nums=[]
	i = 0
	while i<len(mods) :
		if mods[i]%base==0:
			print 0
			nums.append(0)
			i+=1
		else:
			nums.append(PotencializaModulo (base,exp,mods[i]))
			i+=1
	AlgoChines(nums,mods)



#recebe o numero de repeticoes 
n = input()
#loop principal
for i in range (n) :
        AlgoChinesPotenciasMod()
        print'---'
