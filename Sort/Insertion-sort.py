#insertion sort
'''
Idea: Pick an element and insert into sorted list
Assume L[:i] is sorted
Insert L[i] in L[:i]
'''
def InsertionSort(L):
    n=len(L)
    if n<1:
        return L
    for i in range(n):
        #assume L[:i] is sorted
        #move L[i] to correct position in L
        j=i
        while(j>0 and L[j]<L[j-1]):# while the element we are inserting is smaller than the previous element in the list
        #swap them 
            (L[j],L[j-1])=(L[j-1],L[j]) #swap with the element
            j=j-1 #change the focus
        #Now L[:i+1] is sorted
    return L
'''
outer loop iterates n times
inner loop: i steps to insert L[i] in L[:i]
T(n)=n(n-1)/2
O(n^2)
'''

#Using recursion
def Insert(L,v):
    n=len(L) #length of the list
    if n==0: #if the list is empty 
        return ([v]) #create a new list with v in it
    if v>=L[-1]: #if v is greater than the last element in the list
        #add v to the end of the list
        return (L+[v])
    else:
        #if v is smaller than the last element, reduce the size of the list by 1 and
        # check for the conditon again using recursion
        return (Insert(L[:-1]),v)+L[-1:]

#sorting the list
def Isort(L):
    n=len(L)
    if n<1:
        return (L)
    #Coz L is not sorted , we will go the first element of the list and Insert function will be
    # used to insert element at the right position by comparing if the element is greater than or less than the 
    #previous element
    L=Insert(Isort(L[:-1]),L[-1])
    return (L)

'''
TI(n) be the time taken by Insert
TS(n) be the time taken by ISort
TI(0)=1
TI(n)=TI(n-1)+1
Unwind to get TI(n)=n

TS(0)=1
TS(n)=TS(n-1)+TI(n-1)
1+2+3..+n-1
O(n^2)

Note:
worst case is O(n^2)
unlike selection sort, not all cases take time n^2
if the list is already sorted, Inset stops in 1 step
overall time can be close to O(n)
'''