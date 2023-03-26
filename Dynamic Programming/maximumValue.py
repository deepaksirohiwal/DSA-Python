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
'''
O(2^n)
'''
'''
Memoizaton
'''
def max_profit_memo(weight,profits,capacity):
    memo={}
    def recurse(capacity,idx):
        key=(capacity,idx)
        if key in memo:
            return memo[key]
        elif idx==len(weight):
            return 0
        elif weight[idx]>capacity:
            return recurse(capacity,idx+1)
        else:
            op1=recurse(capacity,idx+1)
            op2=profits[idx]+recurse(capacity-weight[idx],idx+1)
            return max(op1,op2)
    return recurse(capacity,0)
print(max_profit_memo(capacity,profits,w))


'''
Dynamic
'''
def max_profit_dp(weight, profits, capacity):
    n = len(weight)
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n)]
    
    def recurse(capacity,idx):
        if idx == n:
            return 0
        
        if memo[idx][capacity] != -1:
            return memo[idx][capacity]
        
        if weight[idx] > capacity:
            memo[idx][capacity] = recurse(capacity, idx + 1)
            return memo[idx][capacity]
        else:
            op1 = recurse(capacity, idx + 1)
            op2 = profits[idx] + recurse(capacity - weight[idx], idx + 1)
            memo[idx][capacity] = max(op1,op2)
            return memo[idx][capacity]
    
    return recurse(capacity,0)

print(max_profit_dp(capacity,profits,w))
