'''
BFS using adjacency list

'''
def BFSListPath(AList,v):#v is the starting point in the graph
    (visited,parent)=({},{})
    #initializing the visited with False and parent with -1
    for i in AList.keys():
        visited[i]=False
        parent[i]=-1
    q=[]
    #the 1st element to start with 
    visited[v]=True
    q.append(v)

    while (len(q)!=0):#while the queue is not empty 
        #take out the first element from the list
        j= q[0]
        q=q[1:]
        for k in AList[j]:
            if (not visited[k]):
                visited[k]=True
                parent[k]=j
                q.append(k)

    return (visited,parent)
'''
returning the level of each node from the source node and the path followed
'''   
def BFSListPathlevel(AList,v):#v is the starting point in the graph
    (level,parent)=({},{})
    output=[]
    #initializing the visited with False and parent with -1
    for i in AList.keys():
        level[i]=-1
        parent[i]=-1
    q=[]
    #the 1st element to start with
    level[v]=0
    q.append(v)

    while (len(q)!=0):#while the queue is not empty 
        #take out the first element from the list
        j= q[0]
        output.append(j)
        q=q[1:]
        for k in AList[j]:
            if (level[k]==-1):
                #increment from the level it came from
                level[k]=level[j]+1
                parent[k]=j
                q.append(k)

    return (level,parent,output)

'''
Shortest path to any node from the source node
'''
def shortest(target,parent_dict):
    path=[]
    while target != -1:
        path.append(target)
        #now v  will be the parent node of the existing v
        target=parent_dict[target]
    path.reverse()
    return path


adj_list={
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
    }
print(BFSListPath(adj_list,"A"))
print(BFSListPathlevel(adj_list,"A"))
(level,parent,output)=BFSListPathlevel(adj_list,"A")
print(shortest("G",parent))