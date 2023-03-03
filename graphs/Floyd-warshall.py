import numpy as np

def floydwarshall(WMat):
    (rows,cols,x)=WMat.shape
    inifinity=np.max(WMat)*rows*rows+1
    
    #creating a shortest path matrix
    SP=np.zeros(shape=(rows,cols,cols+1))
    for i in range(rows):
        for j in range(cols):
            SP[i,j,0]=inifinity

    for i in range(rows):
        for j in range(cols):
            #if there is a edge between i and j
            if WMat[i,j,0]==1:
                #assigned the shortest path 
                SP[i,j,0]=WMat[i,j,1]

    for k in range(1, cols+1):
        for i in range(rows):
            for j in range(cols):
                SP[i,j,k]=min(SP[i,j,k-1], SP[i,k-1,k-1]+SP[k-1,j,k-1])
    return (SP[:,:,cols])

    
edges = [(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]
size = 8
import numpy as np
W = np.zeros(shape=(size,size,2))
for (i,j,w) in edges:
    W[i,j,0] = 1
    W[i,j,1] = w 
print(floydwarshall(W))