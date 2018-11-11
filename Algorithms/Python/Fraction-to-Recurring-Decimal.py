class Solution(object):

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = '-' if numerator * denominator < 0 else ''
        num, denum = abs(numerator), abs(denominator)
        integer = flag + str(num // denum)
        if num % denum == 0:
            return integer
        decimal, remain = "", num % denum
        index, div, remainDic = 0, '', {}
        while True:
            if remain in remainDic:
                decimal = div[:remainDic[remain]] + \
                    '(' + div[remainDic[remain]:] + ')'
                break
            else:
                remainDic[remain] = index
                num = remain * 10
                remain = num % denum
                index += 1
                div += str(num // denum)
                if remain == 0:
                    decimal = div
                    break
        return integer + '.' + decimal
