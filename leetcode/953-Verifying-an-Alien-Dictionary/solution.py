class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        a_to_l = dict(zip(order, 'abcdefghijklmnopqrstuvwxyz'))

        def translate(w):
            nw = ''
            for c in w:
                nw += a_to_l[c]
            return nw

        prev = ''
        for w in words:
            curr = translate(w)
            if prev > curr:
                return False
            prev = curr
        return True
