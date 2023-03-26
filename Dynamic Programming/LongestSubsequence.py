'''
Given two words, we need to find the longest common subsequence
eg., seq1: absent
    seq2: best
    here the length of the longest subsequence is 3 (same order)--> 'bet' or 'bst' 
'''

def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    #if reached to the end
    if idx1==len(seq1) or idx2==len(seq2):
        return 0
    #if the chr matches
    elif seq1[idx1]==seq2[idx2]:
        return 1+ lcs_recursive(seq1,seq2,idx1+1,idx2+1)
    else:
        option1= lcs_recursive(seq1, seq2, idx1+1,idx2)
        option2= lcs_recursive(seq1,seq2,idx1,idx2+1)
        return max(option1,option2)
'''
Testing
O(2^(m+n))
'''
seq1='serendipitous'
seq2= 'precipitation'

print(lcs_recursive(seq1,seq2))
#output 7
''''
Improving the complexity using Memoization
'''
def lcs_memo(seq1,seq2):
    #keeping track of the already computed nodes
    memo={}
    def recurse(idx1=0,idx2=0):
        key=(idx1,idx2)
        if key in memo:
            return memo[key]
        elif idx1==len(seq1) or idx2==len(seq2):
            memo[key]=0
        elif seq1[idx1] == seq2[idx2]:
            memo[key]=1+recurse(idx1+1,idx2+1)
        else:
            memo[key]=max(recurse(idx1+1,idx2), recurse(idx1,idx2+1))
        return memo[key]
    return recurse(0,0)
print(lcs_memo(seq1,seq2))