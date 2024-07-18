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
class Solution:
    def minWindow(self, s, t):
        t_count = {}
        for i in set(t):
            t_count[i] = t.count(i)
        required_chars = len(t_count)
        window_count = {}

        i,j = 0,0
        formed_chars = 0
        n = len(s)
        min_len = 10e5
        min_win = ""
        while j<n:
            if s[j] in window_count:
                window_count[s[j]] += 1
            else:
                window_count[s[j]] = 1
            if s[j] in t_count and window_count[s[j]] == t_count[s[j]]:
                formed_chars +=1
            
            while i<=j and formed_chars == required_chars:
                if j-i+1<min_len:
                    min_len = j-i+1
                    min_win = s[i:j+1]
                window_count[s[i]] -=1
                if s[i] in t_count and window_count[s[i]]<t_count[s[i]]:
                    formed_chars -= 1
                i+=1
            j+=1
        return min_win


if __name__=="__main__":
    print("Hello")
    # S = Solution()

    # s = "ADOBECODEBANC"
    # t = "ABC"

    # out = S.minWindow(s,t)
    # print(out)
