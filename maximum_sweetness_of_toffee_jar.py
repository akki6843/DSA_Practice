"""
Maximum Sweetness of Toffee Jar
You are given an integer n, an array of positive integers price where price[i] denotes the price of the ith toffee and a positive integer k.

The store sells jars of k distinct toffees. The sweetness of a toffee jar is the smallest absolute difference of the prices of any two toffees in the jar.

Return the maximum sweetness of a toffee jar.

Input Format
1st Line contains a single interger n, size of the price array.
2nd Line contains the price array, denoting price of ith toffee.
3rd Line contains a single interger k, denoting the number of disctict toffees in each jar.
Output Format
Single Integer denoting the maximum possible sweetness.

Input:
n = 6, price = [13,5,1,8,21,2], k = 3
Output:
8

`Explanation:
Choosing the toffees with the prices [13, 5, 21].
The sweetness of the toffee jar is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
It can be proven that 8 is the maximum sweetness that can be achieved.
Example 2
Input:
n = 3, price = [1,3,1], k = 2
Output:
2

Explanation:
Choose the toffees with the prices [1, 3].
The sweetness of the toffee jar is: min(|1 - 3|) = min(2) = 2.
It can be proven that 2 is the maximum sweetness that can be achieved.
Constraints
2 <= k <= n <= 10^5

1 <= price[i] <= 10^9
"""
class Solution:
  def maximumSweetness(self, n, price, k):
    price.sort(reverse=True)
    diffs = []
    for i in range(n-k+1):
      diff = abs(price[i + k - 1] - price[i])
      diffs.append(diff)
    diffs.sort()
    return max(diffs[:k]), diffs
  
if __name__=="__main__":
  print("Hello")
#   n = 6
#   price = [13,5,1,8,21,2]
#   k = 3

#   n = 6
#   price = [13,5,1,8,21,2]
#   k = 4

# #   n = 3
# #   price = [1,3,1]
# #   k = 2  

#   S = Solution()
#   out = S.maximumSweetness(n,price, k)
#   print(out)
a = 2.5
print(ceil(a))