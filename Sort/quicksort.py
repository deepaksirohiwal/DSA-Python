def quicksort(sequence):#this will take a list of unordered sequence
    #if the length is 1 or smaller than 1
    if len(sequence)<=1:
        return sequence
    else:
        #will take the last element from the sequence and store in the pivot
        pivot=sequence.pop()
    items_greater=[]
    items_smaller=[]
    for item in sequence:
        #if the current item is greater than the pivot move it to the right
        if item> pivot:
            items_greater.append(item)
        #else move it to the left
        else:
            items_smaller.append(item)

    return quicksort(items_smaller)+[pivot]+quicksort(items_greater)

'''
if the pivot is the median
O(nlog(n))
if the pivot is maximum or minimum
O(n^2)

Already sorted:worst case!!
'''