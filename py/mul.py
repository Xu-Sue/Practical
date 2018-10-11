f = open("w.csv","a+")
for i in range(0,10):
	for j in range(1,i+1):
		print(i,"x",j,"=",i*j,end="   "	,file = f)
		if(i==j):
			print("",end="\n",file = f)

f.close()
