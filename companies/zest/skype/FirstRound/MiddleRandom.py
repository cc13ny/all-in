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
    while True:
        pre = mid[:]
        shuffle(mid)
        isdiff = False
        for j in range(len(mid)):
            if word[pre[j]] != word[mid[j]]:
                isdiff = True
                break
        if isdiff:
            break
  
    newword = word[0]
    for i in mid:
        newword += word[i]
    newword += word[-1]
    
    return newword

def main():
    tests = []
    tests.append("A")
    tests.append("I eat apple")
    tests.append("A fox runs so fast that it suddenly die")
    for test in tests:
        print test
        print midrand(test)
        print

if __name__ == "__main__":
    main()
