class Solution(object):

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def dfs(num, curStr, curNum, prev):
            if not num and curNum == target:
                ans.append(curStr)
                return
            for i in range(1, len(num) + 1):
                if i == 1 or (num[0] != '0'):
                    val = num[:i]
                    dfs(num[i:], curStr + '+' + val,
                        curNum + int(val), int(val))
                    dfs(num[i:], curStr + '-' + val,
                        curNum - int(val), -int(val))
                    dfs(num[i:], curStr + '*' + val, curNum -
                        prev + prev * int(val), prev * int(val))

        ans = []
        for i in range(1, len(num) + 1):
            if i == 1 or (num[0] != '0'):
                dfs(num[i:], num[:i], int(num[:i]), int(num[:i]))
        return ans
