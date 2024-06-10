arr = [-4,-3,-2,-1,4,3,2]
arr = [0] + arr
out = []
temp = 0
for i in arr:
    temp += i 
    print(temp)
    out.append(temp)

print(f"Max is {max(out)}")


