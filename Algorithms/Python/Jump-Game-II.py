class Solution:
    # @param A, a list of integers
    # @return an integer

    def jump(self, A):
        last, cur, ans = 0, 0, 0
        for i in range(len(A)):
            if last < i:
                last = cur
                ans += 1
            cur = max(cur, A[i] + i)
        return ans
