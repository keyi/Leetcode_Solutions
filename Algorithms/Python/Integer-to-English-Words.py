class Solution(object):

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def twoDigits(num):
            if num in dic:
                return dic[num]
            return dic[(num // 10) * 10] + ' ' + dic[num % 10]

        def threeDigits(num):
            s = ''
            if num // 100:
                s += (dic[num // 100] + ' Hundred')
            if num % 100:
                s += (' ' + twoDigits(num % 100))
            return s

        dic = {1: "One", 2: "Two", 3: "Three", 4: "Four",
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                  10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
                  20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
                  70: "Seventy", 80: "Eighty", 90: "Ninety"}
        unit = ["", "Thousand", "Million", "Billion"]

        if num == 0:
            return 'Zero'
        ans = []
        index = 0
        while num:
            if num % 1000:
                ans.append((threeDigits(num % 1000) +
                            ' ' + unit[index]).strip())
            num //= 1000
            index += 1

        return ' '.join(ans[::-1])
