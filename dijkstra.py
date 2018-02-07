print 'shortest path algorithm using djikstras algorithm \n--------------------------------------------'
inf=99999
n=input("enter number of nodes : ")

def djikstra(cost,source,target):
	global n
	global inf
	dist=[]
	prev=[]
	selected=[]
	for k in range(0,n):
		selected.append(0)
	path=[]
	for k in range(0,n):
		dist.append(inf)
		prev.append(-1)
	start=source
	selected[start]=1
	dist[start]=0
	while selected[target]==0:
		min1=inf
		m=0
		for i in range(1,n):
			d=dist[start]+cost[start][i]
			if d<dist[i] and selected[i]==0:
				dist[i]=d
				prev[start]
			if min1>dist[i] and selected[i]==0:
				min1=dist[i]
				m=i
		start=m
		selected[start]=1
	start=target
	path=' '
	while start!=-1:
		path+=chr(start+65)
		start=prev[start]
	print "path is :"+path[::-1]
	return dist[target]


cost=[]
for k in range(0,n):
	temp=[]
	for l in range(0,n):
		temp.append(inf)
	cost.append(temp)

print cost

for k in range(1,n):
	for l in range(k+1,n):
		weight=input("enter weight of path between "+str(k)+" and "+str(l)+" : ")
		cost[k][l]=weight
		cost[l][k]=weight

print cost

source=input("enter the source:")
target=input("enter the target:")

co=djikstra(cost,source,target)

print "the minimum cost is : "+str(co)
