'''
Given n elements each of which has a weight and value. We have to find the maximum value that 
can be obtain by seelcting a subset of the element no more than the weight

'''
'''
Input: Weight, Value and Capacity
'''
def max_profit(weight, profits, capacity,idx=0):
    if idx== len(weight):
        return 0
    elif weight[idx]>capacity:
        return max_profit(weight,profits,capacity,idx+1)
    else:
        op1=max_profit(weight,profits,capacity,idx+1)
        op2=profits[idx]+max_profit(weight,profits,capacity-weight[idx],idx+1)
        return max(op1,op2)
w=8
dict={1:(2,10), 2:(3,20), 3:(4,40)}
profits=[x[1] for x in dict.values()]
capacity=[x[0] for x in dict.values()]
print(max_profit(capacity,profits,w))