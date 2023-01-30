#Number of bits in binary representaion of n
def numberOfBits(n):
    count=1
    while n>1: 
        count+=1 #increment count by 1 with each increment
        n=n//2 # halving the number with each itteration, So, with each iteration we are reducing the size
        #of the n 
    return count
 '''
 log n steps to reach 1
 '''
