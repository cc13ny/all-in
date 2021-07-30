'''
No Backtracking, DFS or BFS, but just move forward/ Iterative
'''

num2letter = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class SolutionIterative:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = [""]
        for d in digits:
            idx = int(d) - 2

            tmp = []
            for letters_comb in res:
                for c in num2letter[idx]:
                    tmp.append(letters_comb + c)
            res = tmp
        return res


'''
Recursive
'''

class SolutionRecursive:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        idx = int(digits[-1]) - 2

        prev_letter_combs = self.letterCombinations(digits[:-1])

        if prev_letter_combs:
            res = [comb + c for c in num2letter[idx] for comb in prev_letter_combs]
        else:
            res = list(num2letter[idx])

        return res