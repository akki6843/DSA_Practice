"""
LongestSubStringWith K unique charachters
Given a string S and an integer K, find the length of the longest substring of S that contains exactly K unique characters. If no such substring exists, return -1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function longestKSubstr() which takes the string S and an integer K as input and returns the length of the longest substring with exactly K distinct characters. If there is no substring with exactly K distinct characters then return -1.
Input:

A string S containing lowercase letters.
An integer K, the number of unique characters required in the substring.
Output:

The length of the longest substring with exactly K unique characters.
Constraints:

1<=length of S<=10^6
0<= K<= 26
Examples:

Input:
S = "aabacbebebe", K = 3

Output:
7

Explanation:
The longest substring with exactly 3 distinct characters is "cbebebe".
"""
class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        i, j = 0, 0
        max_length = 0
        char_count = {}
        sub_str = "" # if you want the string as output populate this code
        while j < n:
            if s[j] in char_count:
                char_count[s[j]] += 1
            else :
                char_count[s[j]] = 1
            
            while len(char_count) > k:
                char_count[s[i]] -=1
                if char_count[s[i]] == 0:
                    del char_count[s[i]]
                i +=1
            if j-i+1 > max_length:
                max_length = j -i +1
                sub_str = s[i:j+1]
            j +=1
        return max_length


if __name__=="__main__":
   print("Hello")
   s = "aabacbebebe"
   K = 5
   S = Solution()
   out = S.longestKSubstr(s,K)
   print(out)



