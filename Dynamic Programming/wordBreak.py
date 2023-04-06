'''
word='apple'
list=['ap','pple','app','apl','appl','le','ple']
we need to find the set of words from the list which can make up the required word
'''

#brute force algo
def constructWord(word,wordList,idx=0):
    if word=="":
        return [[]]
    result=[]
    for i in range(len(word)):#iterate over the length of the word
        prefix,suffix=word[:i+1],word[i+1:]
        if prefix in wordList:
            sublists=constructWord(suffix,wordList)
            for sublist in sublists:
                result.append([prefix]+sublist)
    return result
print(constructWord('apple', ['ap', 'pple', 'app', 'apl', 'appl', 'le', 'ple'])) #returns [['ap', 'ple'], ['app', 'le']]
