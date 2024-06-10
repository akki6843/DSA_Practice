
class Solution:
    def is_looping_number(self, n):
      visited = set()
      while n != 1 and n not in visited:
        visited.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
      return n == 1


if __name__ == "__main__" :
   S = Solution()
   print(S.is_looping_number(23))
   print(S.is_looping_number(4))