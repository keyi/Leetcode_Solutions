class Solution(object):

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n))

# MTHOND 2 (TLE)


# class Solution(object):

#     def bulbSwitch(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         def isOn(n):
#             temp = 0
#             for i in range(2, n + 1):
#                 if n % i == 0:
#                     temp += 1
#             return temp % 2 == 0

#         ans = 1
#         for i in range(2, n):
#             ans += 1 if isOn(i) else 0
#         return ans
