'''
插入排序(Insertion Sort)是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
'''
def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]


alist = [54,26,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)