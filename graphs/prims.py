def prims(WList):
    infinity=1+max([d for u in WList.keys()
                    for (v,d) in WList[u]])
    (visited,distance,parent)=({},{},{})
    for v in WList.keys():
        (visited[v],distance[v],parent[v])=(False,infinity,-1)

    visited[0]=True
    distance[0]=0
    for (v,d) in WList[0]:
        #update the parent dict and the distance
        distance[v]=d
        parent[v]=0
    '''
    initially the nodes which are connected to the 0th node will have updated distance
    '''
    #get the nodes connected to the current node
    for i in range(1,len(WList.keys())):  
        #minimum weight edge from the node
        nextd = min([distance[v] for v in WList.keys() if not visited[v]])
        #the vertex
        nextvlist = [v for v in WList.keys() if (not visited[v]) and distance[v] == nextd]
        if nextvlist==[]:
            break
        #if there are more than 1 vertex with the same weight then take minimum of them 
        nextv = min(nextvlist)
        #mark the vertex visited
        visited[nextv]=True
        for (v,d) in WList[nextv]:
            if not visited[v]:
                #if the distance is smaller than the current distance
                if d< distance[v]:
                    parent[v]=nextv
                    distance[v]=d
    return parent









dedges = [(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]
edges = dedges + [(j,i,w) for (i,j,w) in dedges]
size = 5
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in edges:
    WL[i].append((j,d))


print(prims(WL))