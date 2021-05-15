def bulbSwitch(n):
    res = 1
    primes = []
    for j in range(2, n + 1):
        m = j / 2
        case = 0
        for p in primes:
            cnt = 0
            if p > m:
                break
            elif j % p == 0:
                case = 1
                while t % p == 0:
                    t /= p
                    cnt += 1
                if cnt % 2 == 1:
                    case = 2
                    break
        if case == 0:
            primes.append(j)
        if case == 1:
            res += 1
    return res
