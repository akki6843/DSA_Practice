s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
myDict = {}
for i in range(len(s)):
    myDict[indices[i]]=s[i]

indices.sort()
for i in indices:
    print(myDict[i], end="")