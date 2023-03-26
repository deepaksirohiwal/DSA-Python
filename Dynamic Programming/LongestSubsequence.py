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

'''
O(m*n)
'''

'''
Dynamic programming
1. create a table of (n1+1)*(n2+1) and initialize it with 0 where n1 and n2 are the length 
    of the sequence.
    table[i][j] represents the largest common subsequence of seq[:i] and seq[:j].
2. If seq1[i]==seq2[j] then update the table 
    table[i+1][j+1]=1+table[i][j]
3. If seq1[i]!=seq2[j] then update the table
    max of the diagonal
    table[i+1][j+1]=max(table[i][j+1],table[i+1][j])
'''
def lsc_dp(seq1,seq2):
    n1,n2=len(seq1), len(seq2)
    #creating a matrix of size n1+1*n2*1
    table=[[0 for x in range(n2+1)] for x in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i]==seq2[j]:
                table[i+1][j+1]=1+table[i][j]
            else:
                table[i+1][j+1]=max(table[i][j+1],table[i+1][j])
    #return the last element of the matrix
    return table[-1][-1]
s='axc'
t='ahbgdc'
print(lsc_dp(s,t))