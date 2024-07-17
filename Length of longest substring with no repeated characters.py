"""
Length of longest substring with no repeated characters.
Determine the maximum length of a substring in string s that does not contain any repeated characters.

Sample Input:
Heycoachsuper30
Sample Output: 11
Constraints:

0 <= s.length <= 5 * 104

s consists of English letters, digits, symbols and spaces.
"""


class Solution:
   def longestUniqueSubsttr(self,s):
    n = len(s)
    i,j = 0,0
    max_len = 0
    char_set = set()
    while j<n:
        while s[j] in char_set:
           char_set.remove(s[i])
           i+=1
        char_set.add(s[j])
        max_len = max(max_len, j-i+1)
        j+=1
    return max_len

if __name__=="__main__":
   S = Solution()
   s = "Heycoachsuper30"

   out = S.longestUniqueSubsttr(s)
   print(f"Expected = 11 and outputed = {out}")
