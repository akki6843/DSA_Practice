"""

Same Frequency
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
Output:

False
"""

def check_same_frequency(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    
    f_l1 = {}
    f_l2 = {}

    for i in s1:
        f_l1[i] = list1.count(i)
    
    for i in s2:
        f_l2[i] = list2.count(i)
    
    return f_l1 == f_l2


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

a = check_same_frequency(list1, list2)

print(a)