def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    # if the left node is greater than the node
    #then change the largest
    if l<n and arr[i]<arr[l]:
        largest=l
    #if the right node is greater than the largest
    if r<n and arr[largest] < arr[r]:
        largest=r
    if largest !=i:
        arr[i],arr[largest]= arr[largest],arr[i]
        print(largest)
        heapify(arr,n,largest)
        
def heapSort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

L = [int(item) for item in input().split(" ")]
heapSort(L)
print(*L)