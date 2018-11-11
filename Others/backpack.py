class Goods(object):

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

# METHOD 1: Time(M*N), Space(M*N)


class Solution1(object):

    def package(self, goods, w):
        ans = [[0 for _ in range(w + 1)] for _ in range(len(goods) + 1)]
        for i in range(1, len(goods) + 1):
            for j in range(1, w + 1):
                ans[i][j] = ans[i - 1][j]
                if goods[i - 1].weight <= j:
                    ans[i][j] = max(ans[i][j], ans[i - 1]
                                    [j - goods[i - 1].weight] + goods[i - 1].value)
            # print ans[i]
        return ans[-1][-1]

# METHOD 2: Time(M*N), Space(N)  -- Dynamic Array


class Solution2(object):

    def package(self, goods, w):
        prev = [0 for _ in range(w + 1)]
        cur = [0 for _ in range(w + 1)]
        for i in range(1, len(goods) + 1):
            for j in range(1, w + 1):
                cur[j] = prev[j]
                if goods[i - 1].weight <= j:
                    cur[j] = max(
                        cur[j], prev[j - goods[i - 1].weight] + goods[i - 1].value)
            prev = [x for x in cur]
            # print cur
        return cur[-1]


if __name__ == "__main__":
    goods = [[3, 11], [5, 28], [1, 6], [9, 49], [7, 35]]
    goods = [Goods(x[0], x[1]) for x in goods]
    w = 10
    print(Solution1().package(goods, w))
    print(Solution2().package(goods, w))
