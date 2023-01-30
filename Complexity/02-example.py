#check whether a list contains duplicates
def noDuplicates(L):
    #iterating through each element 
    for i in range(len(L)):
        #holding the current i element, need to compare with the rest of the element 
        for j in range(len(L)):
            if L[i]==L[j]:
                #if found return flase
                return Flase
    return True

'''
* Nested loop scans all pairs of elements
* Worst case: no duplicates, both loops runs
* In a nested loop the time complexity is wual to the number of times the innermost statement is executed
* The number of time the inner loop is going to run is 
* (n-1)+(n-2)+...1=n(n-1)/2
* Overall time is O(n^2)
'''