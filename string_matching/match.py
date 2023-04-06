def stringMatch(target,pattern):
    #list to store the matched index
    poslist=[]
    for i in range(len(target)-len(pattern)+1):
        matched=True
        j=0
        while j<len(pattern) and matched:
            # if the current char does not match change the boolean
            if target[i+j]!=pattern[j]:
                matched=False
            j+=1 
        if matched:
            poslist.append(i)
    return poslist


print(stringMatch("banana","an"))