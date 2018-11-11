import time
import random


#  Bulbble sort
def bubble_sort(nums):
    t = time.time()
    s = nums[:]
    for i in range(1, len(s)):
        for j in range(len(s) - i):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    print("Bubble sort costs %fs." % (time.time() - t))

    t = time.time()
    s = nums[:]
    for i in range(1, len(s)):
        flag = True
        for j in range(len(s) - i):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
                flag = False
        if flag:
            break
    print("Bubble sort(with flag) costs %fs." % (time.time() - t))


#  Selection sort
def selection_sort(nums):
    t = time.time()
    s = nums[:]
    for i in range(len(s)):
        idx = i
        for j in range(i + 1, len(s)):
            if s[j] < s[idx]:
                idx = j
        s[i], s[idx] = s[idx], s[i]
    print("Selection sort costs %fs." % (time.time() - t))


#  Insertion sort
def insertion_sort(nums):
    t = time.time()
    s = nums[:]
    for i in range(1, len(s)):
        idx = i
        temp = s[i]
        for j in range(i, 0, -1):
            if temp < s[j - 1]:
                s[j] = s[j - 1]
                idx = j - 1
            else:
                break
        s[idx] = temp
    print("Insertion sort costs %fs." % (time.time() - t))


#  Shell sort
def shell_sort(nums):
    t = time.time()
    s = nums[:]
    l = len(s)
    gap = l // 2
    while gap:
        for i in range(gap, l):
            idx = i
            temp = s[i]
            for j in range(i, 0, -gap):
                if temp < s[j - gap]:
                    s[j] = s[j - gap]
                    idx = j - gap
                else:
                    break
            s[idx] = temp
        gap //= 2
    print("Shell sort costs %fs." % (time.time() - t))


#  Merge sort
def merge_sort(nums):

    def merge(left, right):
        ll, lr = len(left), len(right)
        l, r, ans = 0, 0, []
        while l < ll and r < lr:
            if left[l] < right[r]:
                ans.append(left[l])
                l += 1
            else:
                ans.append(right[r])
                r += 1
        ans += left[l:]
        ans += right[r:]
        return ans

    def dac(s):
        if len(s) <= 1:
            return s
        left, right = dac(s[:len(s) // 2]), dac(s[len(s) // 2:])
        return merge(left, right)

    t = time.time()
    s = nums[:]
    s = dac(s)
    print("Merge sort costs %fs." % (time.time() - t))


#  Quick sort
def quick_sort(nums):

    def quick(left, right):
        if left >= right:
            return
        pivot = s[left]
        l, r = left, right
        while l < r:
            while l < r and s[r] >= pivot:
                r -= 1
            while l < r and s[l] <= pivot:
                l += 1
            s[l], s[r] = s[r], s[l]
        s[left], s[l] = s[l], s[left]
        quick(left, l - 1)
        quick(r + 1, right)

    t = time.time()
    s = nums[:]
    quick(0, len(s) - 1)
    print("Quick sort costs %fs." % (time.time() - t))


def quick_sort2(nums):

    def getPos(left, right):
        idx = left
        pivot = s[right]
        for i in range(left, right):
            if s[i] <= pivot:
                s[i], s[idx] = s[idx], s[i]
                idx += 1
        s[idx], s[right] = s[right], s[idx]
        return idx

    def quick(left, right):
        if left >= right:
            return s
        pos = getPos(left, right)
        quick(left, pos - 1)
        quick(pos + 1, right)
        return s

    t = time.time()
    s = nums[:]
    quick(0, len(s) - 1)
    print("Quick sort2 costs %fs." % (time.time() - t))


#  Heap sort
def heap_sort(nums):

    def max_heapify(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            else:
                if child + 1 <= end and s[child + 1] > s[child]:
                    child += 1
                if s[root] < s[child]:
                    s[root], s[child] = s[child], s[root]
                    root = child
                else:
                    break

    t = time.time()
    s = nums[:]
    l = len(s)
    mid = int(l // 2 - 1)  # the last parent node
    for i in reversed(range(mid)):  # Build max_heap
        max_heapify(i, l - 1)
    for i in reversed(range(l)):
        s[0], s[i] = s[i], s[0]
        max_heapify(0, i - 1)
    print("Heap sort costs %fs." % (time.time() - t))


def counting_sort():
    print "counting sort ..."
    print "-------"
    N, K = 15, 10
    num = [0] * N
    for i in range(N):
        num[i] = random.randint(0, K)
    print 'orignal', num
    bucket = [0] * (K + 1)
    for i in range(len(num)):
        bucket[num[i]] += 1
    for i in range(len(bucket) - 1):
        bucket[i + 1] += bucket[i]
    print 'bucket', bucket
    s, compare = [0] * (N + 1), [0] * (N + 1)
    for i in reversed(range(len(num))):
        temp = num[i]
        s[bucket[temp]] = num[i]
        compare[bucket[temp]] = i
        bucket[temp] -= 1
    print 'ans', s[1:]
    print 'compare', compare[1:]
    print "-------"


if __name__ == '__main__':
    with open('sample.txt', 'r') as f:
        nums = [int(x) for x in f.readlines()]
    bubble_sort(nums)
    selection_sort(nums)
    insertion_sort(nums)
    shell_sort(nums)
    merge_sort(nums)
    quick_sort(nums)
    quick_sort2(nums)
    heap_sort(nums)
    #  counting_sort()
