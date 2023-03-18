'''
Single source shortest path
Distance of each vertex from the source
'''
def dijkstralist(Wlist,s):#take a list and source
    #infinity is the maximum of the distance *number of vertices +1
    infinity=1+len(Wlist.keys())*max([d for u in Wlist.keys() for (v,d) in Wlist[u]])
    #initially the visited will be False and the distance from the source is infinity
    (visited,distance)=({},{})
    for v in Wlist.keys():
        (visited[v],distance[v])=(False, infinity)
    distance[s]=0

    for u in Wlist.keys():
        #taking out the minimum distance, if it is not visited``nextd=min([distance[v] for v in Wlist.keys() if not visited[v]])
        #list of the vertex which have distance equals to nextd
        nextvlist=[v for v in Wlist.keys() if (not visited[v]) and distance[v]==nextd]
        if nextvlist==[]:
            break
        #taking the minimum of the vertex (if nextlist have more than 1 element: 2 edges with same weight)
        nextv=min(nextvlist)
        visited[nextv]=True
        for (v,d) in Wlist[nextv]:
            if not visited[v]:
                #taking minimum of the existing distance and distance via a vertex (nexv)
                distance[v]=min(distance[v], distance[nextv]+d)
    return distance

dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in dedges:
    WL[i].append((j,d))
print(WL)
print(dijkstralist(WL,0))
