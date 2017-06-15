def Miller ():
	n,b=input()
	q=n-1
	t=0
	while (q%02)==0:
		q=q/2
		t += 1
	print t ,q
	r=PotencializaModulo (n , b , q)
	print q, r

	if (r==1 or r == n - 1):
		print "INCONCLUSIVO"
		return
	count =1	
	while (count < t):
		r=(r**2)%n
		q=q*2
		print q, r
		if (r == n - 1):
			print "INCONCLUSIVO"
			return
		count+=1
	print "COMPOSTO"



	

def PotencializaModulo (mod, base , exp): 
    r=1
    a=base
    e=exp
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

n=input();
#loop principal
for i in range (n) :
        Miller()

        print'---'