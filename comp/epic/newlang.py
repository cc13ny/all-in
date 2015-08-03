def evaluate(s):
    # should we consider cases like '1 - - 1'
    #
    # it's pretty complicated and inconcise so we should make it with clearer logic
    s = ''.join(s.split())
    res, i = 0, 0
    stack = []
    
    while i < len(s):
        if s[i].isdigit():
            num = ''
            while i <= len(s): # be careful about the case i == len(s)
                if i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                else:
                    stack.append(int(num))
                    if len(stack) == 2:
                        if sym == '*':
                            res = stack[0] * stack[1]
                        elif sym == '+':
                            res = stack[0] + stack[1]
                        else:
                            res = stack[0] - stack[1]
                        stack = [res]
                    break
        else:
            sym = s[i]
            i += 1
    return res
