"""
Two heyCoach students have been assigned to solve certain coding problems for their upcoming tasks , the problems is represented with tme. he help of the problem’s number associated with it, both of them have a list of problems represented by an array of problem’s number(say arr1 and arr2), now as they have very limited time, they want to help each other by solving together. Return how many problems they have to solve together in order to save time.

Example 1
Input
 arr1= [1, 2, 3 , 5]
 arr2 =[7,6,5,8,9] 
Output
8
Example 2
Input
 arr1=[2,3]
 arr2 =[2,3]
Output
2
Constraints:
1<=arr1.length,arr2.length<=1000 For all 0<= i <arr1.length,arr2.length

1<=arr1[i],arr2[i]<=1000

    """

class Solution:
    def unionArray(self, arr1, arr2, n, m):
        s1 = set(arr1)
        s2 = set(arr2)
        union = s1.union(s2)
        return len(union)



if __name__ == "__main__":
    print("Union in Heycoach Problem")
    S = Solution()
    arr1= [1, 2, 3 , 5]
    arr2 =[7,6,5,8,9] 
    n = len(arr1)
    m = len(arr2)
    out = S.unionArray(arr1, arr2, n, m)
    print(out)

