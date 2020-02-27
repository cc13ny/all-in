'''
    Time: 2020/02/26 19:50
    Location: New York City
    Author: Chi

    Brief Explanation:
    1. helper variables
       1.1 visited:         a dict used to record visited any transformed word
       1.2 visited_count:   the number of visited words
    2. two shortcuts to return the result immediately
       2.1 when the endWord is found
       2.2 visited_count is equal to the number of transformed words, and the endWord is not found
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = {}
        visited_count = 0
        for word in wordList:
            visited[word] = False

        q = [beginWord]
        new_q = []

        res = 2
        while len(q) > 0:
            word = q.pop()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in visited and not visited[new_word]:
                        if new_word == endWord:
                            return res
                        visited_count += 1
                        if visited_count == len(wordList):
                            return 0

                        visited[new_word] = True
                        new_q.append(new_word)
            if len(q) == 0:
                q, new_q = new_q, []
                res += 1
        return 0