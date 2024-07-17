"""
Problem Statement:

Develop an algorithm to identify the shortest contiguous substring in string s that encompasses all the characters present in string t, considering duplicates as well. If no such substring can be found, the solution should return an empty string.

Note that the provided test cases will guarantee the presence of a single, unique solution.

Input :

s (String): The input string where the algorithm searches for the shortest contiguous substring.
t (String): The target string containing characters to be present in the substring.
Output : Return the shortest contiguous substring of s that encompasses all the characters present in t, considering duplicates.

Example :

s = "ADOBECODEBANC"
t = "ABC"
Output:

"BANC"
Constraints:

m == s.length

n == t.length

1 <= m, n <= 10^5

s and t consist of uppercase and lowercase English letters.
"""