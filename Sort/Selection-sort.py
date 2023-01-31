# Selection sort
'''
swap the minimum element with the first element in the list

'''
def SelectionSort(L):
    n=len(L)
    if n<1:
        return L
    for i in range(n):
        #assume L[:i] is sorted
        min_pos=i 
        for j in range(i+1,n):#iterate from the ith positon to the last position in the list
            # if the jth position element is samller than the ith position element then swap them
            if L[j]<L[min_pos]:
                min_pos=j
        #swap the positon after comparing with all the rest of the values
        (L[i],L[min_pos])=(L[min_pos],L[i])
    return L #L is sorted

'''
The outer loop itterates n times
inner loop itterates n-i steps to find minimum in L[i:]
T(n)=n+(n-1)+....1
T(n)=n(n+1)/2
T(n)=O(n^2)
'''

