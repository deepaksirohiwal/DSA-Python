#used merge sort to get the number of inversions in the list

def mergeAndCount(A,B):
    (m,n)=(len(A),len(B))
    '''
    C will hold the sorted list
    i is the iterator for the left list (A)
    j in the iterator for the right list (B)
    k will keep a note of the length of the list as we want to stop the loop is k == m+n
    '''
    (C,i,j,k,count)=([],0,0,0,0)
    while k < m+n:
        #if i pointer has reached to the end 
        if i==m:
            #take all the elements from the right and append to C 
            C.append(B[j])
            (j,k)=(j+1,k+1)
        elif j ==n :
            C.append(A[i])
            (i,k)=(i+1,k+1)
        elif A[i]<B[j]:
            C.append([i])
            (i,k)=(i+1,k+1)
        else:
            C.append(B[j])
            #increment count as the element on the right is smaller so it is case of inversion
            (j,k,count)=(j+1,k+1,count+(m-i))
    return (C,count)


def sortAndCount(A):
    n= len(A)
    #if it is the last element return it
    if n<=1:
        return (A,0)
    #soreted Left and Right part will be merged and the number of inversion will be return
    (L,countL)= sortAndCount(A[:n//2])
    (R,countR)=sortAndCount(A[n//2:])
    (B,countB)=mergeAndCount(L,R)
    return (B,countL+countR+countB)