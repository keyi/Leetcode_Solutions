class Solution(object):

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def encodeSTR(substr):
            count = 0
            for x in substr:
                count += c[x]
                count <<= 2
            return count

        c = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        ans, dic = [], {}

        for i in range(9, len(s)):
            substr = s[i - 9:i + 1]
            num = encodeSTR(substr)
            if num not in dic:
                dic[num] = 1
            else:
                if dic[num] == 1:
                    ans.append(substr)
                dic[num] += 1
        return ans
