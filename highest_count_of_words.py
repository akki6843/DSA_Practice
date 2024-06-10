sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

for s in sentences:
    print(len(s.split()))


print(list(map(lambda x:len(x.split()), sentences)))