"""
Count Occurences of Anagrams
Raman is a keen observer, he can easily see the
 jumbled words so one day one of his friend challenged
   him to count the occurrences of all the anagrams of string C in
     a given string S. Raman accepted the challenge but
       he is facing some problems in it . Can you help them ?

Input:

S=fororfrdofr  
C=for   
Output: 3

Input :

 S=aabaabaa  
 C=aaba  
Output: 4

1<=s.length, c.length<=10^3
"""
class Solution:
    def get_freq(self, sub_s):
        my_dict = {}
        for i in sub_s:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        return my_dict
    def count_anagrams(self, s, c):
        k = len(c)
        n = len(s)
        i,j=0,0
        count = 0
        c_freq_dict = self.get_freq(c)
        while j<n:
            if (j-i+1) == k:
                sub_str = s[i:j+1]
                sub_str_freq_dict = self.get_freq(sub_str)
                if c_freq_dict == sub_str_freq_dict:
                    count +=1
                i+=1
            j+=1
        return count


if __name__=="__main__":
    S = Solution()
    s="fororfrdofr" 
    c="for"
    out = S.count_anagrams(s,c)
    print(out)

