"""
Given an array nums of n integers and replace every element with the least greater element on its right side in the array.

If there are no greater elements on the right side, replace it with -1.

Input Format:

The first line contains an integer n, denoting the number of elements in the array.
The second line contains n space-separated integers representing the elements of the array.
Output Format:

A single line containing nspace-separated integers, where each integer is the least greater element on the right side of each element in the array. If no such element exists, print -1.
Sample Input 1 :
n=15

[ 8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28 ] 
Output :
18 63 80 25 32 43 80 93 80 25 93 -1 28 -1 -1
Sample Input 2:
n=6

[ 2, 6, 9, 1, 3, 2 ] 
Output :
3 9 -1 2 -1 -1
Constraints:
1 <= N <= 10^5

1 <= A[i] <= 10^5
"""
class Solution:
    def findLeastGreater(self, n, arr):
        new_arr = [-1] * n
        for i in range(n):
            min_greater = float('inf')
            for j in range(i+1, n):
                if arr[j] > arr[i] and arr[j] < min_greater:
                    min_greater = arr[j]
            if min_greater != float('inf'):
                new_arr[i] = min_greater
        return new_arr
    

if __name__=="__main__":
    S = Solution()

    arr = [ 8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28 ]
    n = len(arr)
    out = S.findLeastGreater(n, arr)
    print(out)