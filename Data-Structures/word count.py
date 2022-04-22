def wordcount(words):
    count = {}
    words = words.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    print(count)


wordcount("a b c d a b")
