dvr={}
n=input("number of nodes : ")
costmat=[]
print "enter the cost"
for i in range(0,n):
	temp=[]
	dvr[i]=[]
	dvr[i].append([])
	dvr[i].append([])
	for j in range(0,n):
		k=input(":")
		if(i==j):
			t=0
		else:
			t=k
		temp.append(t)
		dvr[i][0].append(t)
		dvr[i][1].append(j)
	costmat.append(temp)
print dvr
print costmat
#main algorithm
#0 is distance and 1 is from table
for i in range(0,n):
	for j in range(i+1,n):
		for k in range(0,n):
			if(dvr[i][0][j]>costmat[i][k]+dvr[k][0][j]):
				dvr[i][0][j]=dvr[i][0][k]+dvr[k][0][j]
				dvr[j][0][i]=dvr[i][0][j]
				dvr[i][1][j]=k
				dvr[j][1][i]=k
#printing
for i in range(0,n):
	print "\nfor router "+str(i+1)
	for j in range(0,n):
		print "node "+str(j+1)+" via "+str(dvr[i][1][j]+1)+" distance "+str(dvr[i][0][j])
