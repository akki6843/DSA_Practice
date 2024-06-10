n = [2,3,5,1,3]

max_now = max(n)

give_extra = lambda x : x+3

with_extra = list(map(give_extra, n))

is_highest = lambda x : x>=max_now

out = list(map(is_highest, with_extra))
print(out)