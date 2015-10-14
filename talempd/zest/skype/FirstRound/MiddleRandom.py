from random import shuffle

def midrand(sentence):
    words = sentence.split()
    newwords = [randomized(word) for word in words]
    newsentence = ' '.join(newwords)
    if sentence == newsentence:
        return "They can't be different"
    else:
        return newsentence

def randomized(word):
    if len(set(word[1:-1])) < 2:
        return word

    mid = range(1, len(word) - 1)
    pre = mid[:]
    while pre == mid:
        pre = mid[:]
        shuffle(mid)
        
    newword = word[0]
    for i in mid:
        newword += word[i]
    newword += word[-1]
    
    return newword

tests = []
tests.append("I love you so much")
tests.append("A fox runs so fast so it has to die in a extremely way")
tests.append("A")
for test in tests:
    print midrand(test)
 
