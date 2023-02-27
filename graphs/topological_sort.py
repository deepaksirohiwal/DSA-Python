def toposort(AList):
    visited={}
    for i in AList.keys():
        visited[i] = False
    seq=[]
    stack=[]#LIFO
    v=min(AList.keys())
    
    stack.append(v)
    while(len(stack)!=0):
        
        j=stack.pop()
        seq.append(j)
        if visited[j]==False:
            visited[j]=True
            for k in AList[j][::-1]:
                if (not visited[k]):
                    stack.append(k)
    return seq

AList={0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
print(toposort(AList))

