"""
Unraveling Clues with Professor
Professor Prateek from HeyCoach coding academy in Bangalore challenges Varshil to find all indices where a given pattern appears within a given text. Both text and pattern consist of lowercase alphabetical characters.
The goal is to identify the starting indices in the text where the complete pattern is found.

Input Format:

The first line contains the string text, consisting of lowercase alphabetical characters (1 <= |text| <= 10^5).
The second line contains the string pattern, consisting of lowercase alphabetical characters (1 <= |pattern| <= 10^5).
Output Format:

A list of integers separated by spaces, representing the starting indices of the text where the pattern appears in its entirety.
Constraints:

1 <= |text| <= 10^5
1 <= |pattern| <= 10^5
The text and pattern consist only of lowercase alphabetical characters.
Example:

Input:
text = "ababcabab"
pattern = "ab"
Output:
0 2 5 7
Explanation:

The pattern "ab" appears at indices 0, 2, 5, and 7 within the text.
"""
class Solution:
  def findPatternIndices(self, text, pattern):
    n = len(text)
    p_n = len(pattern)
    i,j = 0,0
    out = []
    while j < n:
      j = i + p_n
      sub_str = text[i:j]
      if pattern == sub_str:
        out.append(str(i))
      i += 1
    return " ".join(out)


if __name__=="__main__":
  print("Hello")

  inp = "ababcababc ab"
  t, p = inp.split(" ")
  print(t,p)
  S = Solution()
  out = S.findPatternIndices(t,p)
  print(out)
