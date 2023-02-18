def DFSInit(AMat):
    #initialization
    (rows,cols)=AMat.shape
    (visited,parent)=({},{})
    for  i in range(rows):
        visited[i]=False
        parent[i]=-1
    return (visited,parent)

def DFSlist(AList,v):
    (visited,parent)=({},{})
    for i in AList.keys():
        visited[i]=False
        parent[i]=-1
    st=[]#stack --> last come first out
    st.append(v)
    while(len(st)!=0):
        j=st.pop() #take out the last element of the list
        if visited[j]==False: #if the node has never been visited before
            visited[j]=True
            for k in AList[j][::-1]: #checking for all the neighbours 
                if(not visited[k]):
                    parent[k]=j
                    st.append(k)
    return (visited,parent)

AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

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

print(DFSlist(adj_list,"A"))