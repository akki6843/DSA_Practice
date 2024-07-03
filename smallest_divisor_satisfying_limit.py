"""
Smallest Divisor Satisfying the Limit
Given an integer n, an array of integers nums, and an integer limit,
 we will choose any positive integer d, divide all the array elements by it,
   and sum up the value of each division into result. 
   Find the smallest d such that the result for it is less than or equal to limit.

Each result of the division is rounded to the nearest integer greater than or equal to that element.
 (For example: 7/3 = 3 and 10/2 = 5).

Input Format

1st Line contains a single interger n, size of the nums array.
2nd Line contains n space seperated integers denoting the nums array.
3rd Line contains a single interger limit.
Output Format:

Single Integer denoting the smallest possible divisor.
Example 1:

Input: n = 4, nums = [1,2,5,9], limit = 6

Output: 5

Explanation:

We can get a sum of 17 (1+2+5+9) if the d is 1.
 If the d is 4 we can get a sum of 7 (1+1+2+3) and 
 if the d is 5 the sum will be 5 (1+1+1+2).

Example 2:

Input:

n = 5, nums = [44,22,33,11,1], limit = 5
Output:
44

Constraints:

1 <= n <= 5 * 10^4

1 <= nums[i] <= 10^6

n <= threshold <= 10^6
"""

class Solution:
  def smallestDivisor(self, n, nums, limit):
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        if sum((num - 1) // mid + 1 for num in nums) > limit:
            left = mid + 1
        else:
            right = mid
    return left