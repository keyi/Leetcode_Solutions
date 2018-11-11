class Solution(object):

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1, version2 = version1.split('.'), version2.split('.')
        l1, l2 = len(version1), len(version2)
        i, l = 0, min(l1, l2)
        while i < l:
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
            elif i == l - 1:
                c1 = sum([int(x) for x in version1[i:]])
                c2 = sum([int(x) for x in version2[i:]])
                if c1 == c2:
                    return 0
                else:
                    return 1 if c1 > c2 else -1
            i += 1
