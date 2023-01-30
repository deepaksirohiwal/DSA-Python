#finding the maximum element in a list
def maxElement(L):
    maxval=L[0] #let the first element is the maximum in the list
    for i in range(len(L)): #iterating through the list
        if L[i]>maxval: #if the current number is greater than the maxval, replace maxval with it
            maxval=L[i]
    return (maxval) #return the maximum number in the list

'''
* Single loop scans all elements
* Always takes n steps
* Overall time is O(n)
'''