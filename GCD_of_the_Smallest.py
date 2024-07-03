"""
GCD of the smallest
You have been given an array of size n. You need to perform certain operations on the 
array to reduce the size of the array to one according to the following rule:

1). Add two smallest numbers from the array and append the number back to the array.

2). The cost of doing the above operation is equal to GCD (Greatest Common Divisor) of 
the smallest two numbers in the array.

Return the total cost after the last number is left in the array.

Example:

Input : n = 5  ar =  [5,4,2,3,1]

Output:  8
Constraints:

1 <= n <= 1000

1 <= array[i] <= 1000
"""

class Solution:
  def getGCD(self,x,y):
    while(y):
      x, y = y, x % y
    return abs(x)
  
  def solve(self, ar):
    total = 0
    while len(ar)>1:
      ar.sort(reverse=True)
      n1 = ar.pop()
      n2 = ar.pop()
      ar.append(n1 + n2)
      total += self.getGCD(n1,n2)
      print(total)
    return total
  

ar = [5,4,2,3,1]
S = Solution()
print(S.solve(ar))