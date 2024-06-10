
class Solution:
    def solve(self, ar, m, n):
      #Write your code here
      cost = []
      # Check digonally if square matrix
      if m == n :
        total = 0
        for i in range(0,m):
          total += ar[i][i]
        cost.append(total)
      
      # Horizontly check
      total = 0
      for i in range(0,m):
        total += ar[i][0]
      for i in range(0,n):
        total += ar[m-1][i]
      total -= ar[m-1][0]
      cost.append(total)

      # Vertical Check
      total = 0
      for i in range(0,n):
        total += ar[0][i]
      for i in range(0,m):
        total += ar[i][n-1]
      total -= ar[0][n-1]
      cost.append(total)

      return min(cost)



if __name__ == "__main__" :
    ar = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    S = Solution()
    print(S.solve(ar, 3,3))
    