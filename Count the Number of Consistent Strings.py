allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]

allow_collection = set(allowed)

for word in words:
    print(word, set(word), set(word).issubset(allow_collection))