"""
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
"""
encoded = [1,2,3]
first = 1
arr = [0] * (len(encoded) + 1)
arr[0] = first

for i in range(len(encoded)):
    arr[i+1] = encoded[i] ^ arr[i]

print(arr)


