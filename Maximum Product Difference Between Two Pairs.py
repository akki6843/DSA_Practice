"""
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

 

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
Example 2:

Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.
 

Constraints:

4 <= nums.length <= 104
1 <= nums[i] <= 104
"""

class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = -1
        for j in range(high):
            if arr[j]<pivot:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
    
    def quick(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick(arr, low, pi-1)
            self.quick(arr, pi+1, high)
    def maxProductDifference(self, nums):
        self.quick(nums, 0, len(nums)-1)
        return (nums[-1] * nums[-2]) - (nums[0]*nums[1])

if __name__=="__main__":
    nums = [5,6,2,7,4]
    S = Solution()
    out = S.maxProductDifference(nums)
    print(out)