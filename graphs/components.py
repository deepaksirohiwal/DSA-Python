#defining the queue
class Queue:
    def __init__(self):
        self.queue=[]
    #appending to queue
    def addq(self,v):
        self.queue.append(v)
    #checking if the queue is empty
    def isempty(self):
        return (self.queue==[])
    #deleting from queue
    def delq(self):
        v=None
        if not self.isempty():
            v=self.queue[0]
            self.queue=self.queue[1:]
        return v
    def __str__(self):
        return (str(self.queue))

'''
BFS algo which return the dictionary with visited nodes
'''
def BFSList(AList,v):
    visited = {}
    for i in AList.keys():
        visited[i] = False
    q = Queue()
    
    visited[v] = True
    q.addq(v)
    
    while(not q.isempty()):
        j = q.delq()
        for k in AList[j]:
            if (not visited[k]):
                visited[k] = True
                q.addq(k)               
    return(visited)


def Components(AList):
    components={}
    for i in AList.keys():
        components[i]=-1
    #seen will keep track of the number of elements visited
    (compid,seen)=(0,0)
    while seen < max(AList.keys()):
        #taking the minimum of the keys which is not the part of any component
        startv=min([i for i in AList.keys() if components[i]==-1])
        visited=BFSList(AList,startv) #return the dictionary where True indicated the visited node
        for i in visited.keys():
            if visited[i]: #for all the true values
                 seen = seen +1
                 components[i]=compid
        compid+=1
    return(components)


AList = {0: [1], 1: [2], 2: [0], 3: [4, 6], 4: [3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
print(Components(AList))
'''
{0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
So, the number of components are 2
'''