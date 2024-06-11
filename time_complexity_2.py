class Solution:
    def __init__(self):
        self.cnt = 0

    def print(self):
        self.cnt += 1

    def solve(self, n):
      #Write your code here;
      for i in range(n, 0, n//2):
        for j in range(0, i):
          self.print()




s = Solution()
print(s.solve(10))