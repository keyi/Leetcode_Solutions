# METHOD 1: O(logM+logN)


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n
        while start < end:
            mid = start + (end - start) // 2
            cur = matrix[mid // n][mid % n]
            if cur == target:
                return True
            elif cur < target:
                start = mid + 1
            else:
                end = mid - 1
        return start < m * n and matrix[start // n][start % n] == target


# METHOD 2: O(logM+N)


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        start, end = 0, len(matrix) - 1
        while start < end:
            mid = (start + end) // 2
            cur = matrix[mid][0]
            if cur == target:
                return True
            elif cur > target:
                end = mid - 1
            else:
                start = mid
            if start == end - 1:
                break
        if matrix[end][0] > target:
            return target in matrix[start]
        else:
            return target in matrix[end]


# METHOD 3: O(M+N)

class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            cur = matrix[i][j]
            if cur == target:
                return True
            elif cur > target:
                j -= 1
            else:
                i += 1
        return False
