def bellmanford(WMat,s):
    (rows,cols,x)=WMat.shape
    infinity=np.max(WMat)*rows+1
    distance={}
    #initially assignning all distance from the source to infinity
    for v in range(rows):
        distance[v]= infinity
    distance[s]=0
    for i in range(rows):
        for u in range(rows):
            for v in range(cols):
                #if there is connection
                if WMat[u,v,0]==1:
                    #update the distance if the current distance is smaller than the d(u)+edge
                    distance[v]=min(distance[v], distance[u]+WMat[u,v,1])
    return distance
    




edges = [(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]
size = 8
import numpy as np
W = np.zeros(shape=(size,size,2))
for (i,j,w) in edges:
    W[i,j,0] = 1
    W[i,j,1] = w    

print(bellmanford(W,0))

