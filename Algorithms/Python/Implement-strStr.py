class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        slow, fast = 0, 1
        while slow <= fast <= len(haystack):
            while haystack[slow] != needle[0] and fast < len(haystack):
                slow += 1
                fast += 1
            while fast - slow < len(needle):
                fast += 1
            if haystack[slow:fast] == needle:
                return slow
            else:
                slow += 1
                fast += 1
        return -1


# METHOD 2
class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        h, n = len(haystack), len(needle)
        if h < n:
            return -1
        for i in range(h):
            if haystack[i:i + n] == needle:
                return i
        return -1
