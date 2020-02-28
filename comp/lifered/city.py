def city(T):
    # build adjacency list
    adj = [[] for i in range(len(T))]
    root = 0
    for i in range(len(T)):
        t = T[i]
        if i == t:
            root = i
            continue

        adj[i].append(t)
        adj[t].append(i)

    # bfs
    q = [root]
    visited = [False for i in range(len(T))]
    visited[root] = True
    lst = []
    while q != []:
        lst.append(q)
        
        nq = []
        for node in q:
            for nbr in adj[node]:
                if not visited[nbr]:
                    nq.append(nbr)
                    visited[nbr] = True
        q = nq
    return lst[1:]
