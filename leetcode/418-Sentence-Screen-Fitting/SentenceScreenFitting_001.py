class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        cnt = 0
        start = 0
        row_circ = len(''.join(sentence)) + len(sentence)
        nrc = (cols + 1) / row_circ
        cols = (cols + 1) % row_circ
        circle = []
        for i in range(rows):
            j = len(sentence[start])
            while j < cols:
                tmp = (start + 1) % len(sentence)
                if not tmp:
                    cnt += 1
                start = tmp
                j += 1 + len(sentence[start])
            circle.append(cnt)
            if not start:
                break
        ncircle = len(circle)
        cnt = nrc * rows
        cnt += rows/ncircle * circle[-1]
        cnt += circle[rows%ncircle - 1] if rows%ncircle > 0 else 0
        return cnt
