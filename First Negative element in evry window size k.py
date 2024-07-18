"""
First Negative element in evry window size k
In the town of Kanpur, where technology intertwined with everyday life, lived a young programmer named Nitin. One sunny afternoon, while strolling through the local park, she stumbled upon an antique book filled with intricate coding riddles.
Determined to crack the enigma, Nitin found a puzzling task: to locate the first negative integer within every subarray of window size k in a given sequence(say arr) of size N . Help Nitin in solving this task.

Example:

Input:

k= 3
arr={12, -1, -7, 8, -15, 30, 16, 28}  
Output:

-1 -1 -7 -15 -15 0 
Constraints:

1 <= N <= 10^5
10^5 <= A[i] <= 10^5
1 <= K <= N
"""
class Solution:
   def print_first_negative_integer(self, arr, k):
    n = len(arr)
    i, j = 0,0
    out = []
    negs = []
    while j<n:
       if arr[j]<0:
         negs.append(arr[j])
       if (j-i+1) == k:
          if len(negs)==0:
            out.append(0)
          else:
            out.append(negs[0])
          if arr[i] in negs:
            negs.pop(0)
          i+=1
       j+=1
    return out 


            
  

if __name__=="__main__":
   S = Solution()
   k= 3
   arr=[12, -1, -7, 8, -15, 30, 16, 28]

   out = S.print_first_negative_integer(arr, k)
   print(out)

