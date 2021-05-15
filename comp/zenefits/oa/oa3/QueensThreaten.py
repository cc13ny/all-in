def qt(a):
    res = 0
    n = len(a)
    ldial, rdial = {}, {}
    threat = []
    for i in range(n):
        j = a[i]
        threat.append(0)
        if i + j in ldial:
            threat[i] += 1
            pre = ldial[i + j][-1]
            threat[pre] += 1
            if threat[pre] == 4:
                return 4
            ldial[i + j].append(i)
        else:
            ldial[i + j] = [i]

        if i - j in rdial:
            threat[i] += 1
            pre = rdial[i - j][-1]
            threat[pre] += 1
            if threat[pre] == 4:
                return 4
            rdial[i - j].append(i)
        else:
            rdial[i - j] = [i]
    return max(threat)
