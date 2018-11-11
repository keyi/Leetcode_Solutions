class Solution(object):

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def addSpace(i, n, spaceNum):
            if i < n:
                return (spaceNum // n + int(i < spaceNum % n))
            else:
                return 0

        def connect(begin, end, lineLength):
            s = ''
            if begin == end - 1:
                s += (words[begin] + " " * (maxWidth - lineLength))
            else:
                n = end - begin
                for i in range(n):
                    s += words[begin + i]
                    s += ' ' * addSpace(i, n - 1, maxWidth - lineLength)
            ans.append(s)

        if not words or maxWidth == 0:
            return ['']
        ans = []
        begin, lineLength, l = 0, 0, len(words)
        for i, x in enumerate(words):
            if lineLength + len(x) + (i - begin) > maxWidth:
                connect(begin, i, lineLength)
                begin, lineLength = i, 0
            lineLength += len(x)
        lastline = ' '.join(words[begin:l])
        lastline += (" " * (maxWidth - len(lastline)))
        ans.append(lastline)
        return ans
