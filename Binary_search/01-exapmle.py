#Search problem 
# Naive solution
def naivesearch(v):
    for x in l:
        if v==x:
            return True
    return False

#If the list is in accending order
def binarysearch(v,l): #l is the sorted list in accending order
#v is the int we are looking for
    if l==[]: #if the list is empty return false
        return False
    m=len(l)//2 #index of the middle element in the list
    # if the v is the middle element return True
    if v==l[m]:
        return True
    if v<l[m]:# if v is samller than the middle element 
        #then search on the left part of the list
        return (binarysearch(v,l[:m]))
    else:
        #if v is bigger than the middle element 
        #search on the right part of the list
        return (binarysearch(v,l[m+1:]))


'''
-log(n)- number of times to divide the n by 2 to reach 1
-O(log n)
'''