nums = [1]

n = len(nums)
left_sum = []
right_sum = []
out = []
for i in range(n):
    left_sum.append(sum(nums[:i]))

for j in range(n,0,-1):
    right_sum.append(sum(nums[j:]))


right_sum.reverse()
print(f"Left_Sum ={left_sum} \nRight_Sum = {right_sum} ")


for i, j in zip(left_sum, right_sum):
    out.append(abs(i-j))

print(out)
