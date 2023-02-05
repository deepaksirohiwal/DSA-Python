#Counting sort

def countingSort(arr,r): #[2,0,1,1,2,3,0,2,1,0,2,3,1,2]
    n = len(arr)
    max_element = max(arr)
    counting_array = [0] * r #create a list of r 0s
    #itterate through all the element in the arr 
    #increment the value at index arr[i]
    for i in range(n):
        counting_array[arr[i]] += 1
    #counting_array will be a list of array with count of each value 
    #[3,4,5,2]
    index=0 #to keep track of the original array
    for i in range(r):
        for _ in range(counting_array[i]): #iterate number of times the value present in the ith position
           arr[index]=i #replace the current value in arr at index posion with i
           index+=1 #
    return arr

'''
time complexity => O(n+r)
n for creating the counting array
r for the number of iteration in the second loop
'''