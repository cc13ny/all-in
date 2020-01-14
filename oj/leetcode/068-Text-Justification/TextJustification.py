class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def format(wds, L):
            wdslen =  len(''.join(wds))
            l = len(wds) - 1
            res = ''
            step = (L - wdslen) / l if l else L - len(wds[0]) - 1
            diff = (L - wdslen) %  l if l else 1 
            blanks = [' ' * (step+1)] * diff + [' ' * step] * (l - diff)
            for i in range(len(blanks)):
                res += wds[i] + blanks[i]
            res += wds[-1] if l else ''
            return res
            
        lines = []
        res = []
        tmp = 0
        for i in range(len(words)):
            word = words[i]
            if tmp and tmp + len(word) < maxWidth:
                lines[-1].append(word)
                tmp += len(word) + 1
            else:
                tmp = 0
                lines.append([])
                lines[-1].append(word)
                tmp = len(word)
        for l in lines:
            res.append(format(l, maxWidth))
        if len(res):
            res[-1] = ' '.join(res[-1].split())
            res[-1] = res[-1] + (maxWidth - len(res[-1])) * ' '
        return res
