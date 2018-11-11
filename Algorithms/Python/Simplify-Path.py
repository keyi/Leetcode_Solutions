class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        stack = []
        for x in path:
            if x == '' or x == '.':
                pass
            elif x == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return '/' + '/'.join(stack)
