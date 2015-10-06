class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        tb = {}
        for a in A:
            if a not in tb:
                tb[a] = 1
            else:
                tb[a] += 1
        for b in B:
            if b not in tb:
                return False
            elif tb[b] == 1:
                del tb[b]
            else:
                tb[b] -= 1
        return True
