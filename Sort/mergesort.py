#merge sort
'''
let n be the lenfht of the list
Sort A[:m//2]
Sort A[n//2:]
Merge the sorted halves into B
-Sorting can be done recursively
'''
#Merging sorted list
def merge(A,B):
    (m,n)=(len(A),len(B))
    (C,i,j,k)=([],0,0,0)
    while k<m+n:
        #if A is empty
        if i==m:
            C.extend(B[j:]) #add everything to C
            k=k+(n-j)
        #if B is empty
        elif j==n:
            C.extend(A[i:])
            k=k+(n-i)
        elif A[i] < B[j]: #if the ith element in A is smaller than the jth element in B, append A[i] to C and then move  i to i +1
            C.append(A[i])
            (i,k)=(i+1,k+1)
        else:
            C.append(B[j])
            (j,k)=(j+1,k+1)
        return C

#merge sort
def mergesort(A):
    n=len(A)
    if n<=1:
        return A
    #dividing into 2 part
    L=mergesort(A[:n//2])
    R=mergesort(A[n//2:])
    B=merge(L,R)#Merging left and right sorted list
    return B

'''
T(n)=O(nlogn)
'''
