"""
Rohan loves 0, he has been assigned a task by his coach to check whether is it possible to find a subarray in the array nums, with sum 0 in it. Rohan thinks that this task is quite easy as he know the brute-force method, but his coach has strictly instructed to think of a optimized approach for the above problem as brute force will not work this time.

Hint: Prefix Sum Prefix Sum[i] is defined as the sum of all the values of the array up to index i.

PrefixSum[0] = nums[0];

PrefixSum[1] = nums[0]+nums[1];

PrefixSum[i] = nums[0]+nums[1]+nums[2]+........nums[i].

Sample Input:

7

1 4 -2 -2 5 -4 3

Sample Output:

Yes

Constraints :

1<=nums.length()<=10^4;

-10^4<=nums[i]<=10^4;
"""

class Solution:
    def is_zero(self, arr, N):
        prefix_sum_map = {}
        prefix_sum = 0
    
        for i in range(len(arr)):
            prefix_sum += arr[i]
        
            if prefix_sum == 0 or prefix_sum in prefix_sum_map:
                return "Yes"
        
            prefix_sum_map[prefix_sum] = i
    
        return "No"
            


if __name__=="__main__":
    print("Rohan Loves 0 (1) Problem")

    S = Solution()
    N = 7
    # arr = [10, 6, 32, 3980, -8, 39, 40, 51, 2, 4, 11]
    arr = [10, 6, 32, 3980, -8, 39, 40, 51, 2, 4, 11]
    out = S.is_zero(arr, N)
    print(out)