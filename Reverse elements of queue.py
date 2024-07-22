"""
Reverse elements of queue

You are given a queue and an integer 'k'. Your task is to reverse the order of first 'k' elements of queue.

Input Format:

First line contains of two integers denoting the size of array and the integer representing the number of elements that is to be reversed.

Second line contains the elements of the given queue.

Output format:

Return the updated queue.

Sample Input:

5 3

1 2 3 4 5

Sample Output:

3 2 1 4 5

Constraints:

1<=k<=10^6

1<=n<=10^6

1<=q[i]<=10^6 (elements of queue)
"""

from collections import deque

class Solution:
  def solve(self, q, k):
    queue = deque(q)
    stack = []
    for _ in range(k):
      if queue:
        stack.append(queue.popleft())
    while stack:
      queue.append(stack.pop())
    for _ in range(len(queue) - k):
        queue.append(queue.popleft())
    return queue

if __name__=="__main__":
  k = 3
  q = [1,2,3,4,5]
  S = Solution()
  out = S.solve(q,k)
  print(out)