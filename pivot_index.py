arr = [-1,-1,-1,0,1,1]

def get_pivot(arr):
    for i in range(len(arr)):
        print(i,sum(arr[:i]), sum(arr[i+1:]), sum(arr[:i])==sum(arr[i+1:]))
        if sum(arr[:i])==sum(arr[i+1:]):
            return i
    return -1


print(get_pivot(arr))