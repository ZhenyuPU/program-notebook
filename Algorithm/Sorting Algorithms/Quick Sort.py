'''
快速排序(Quicksort)，又称划分交换排序(partition-exchange sort)，
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

步骤为：

1.从数列中挑出一个元素，称为"基准"(pivot)，
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区(partition)操作。
3.递归地(recursive)把小于基准值元素的子数列和大于基准值元素的子数列排序。

递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总会结束，
因为有递归的弹出条件，另外开头排好后开头后面也会根据大于pivot数列排序的代码排好。
'''
def quick_sort(alist, start, end):
    if start >= end:
        return
    low = start
    high = end 
    pivot = alist[start]     # pivot
    while low < high:
        while alist[high] > pivot and low < high:    # 从右到左找到小于pivot的值的角标
            high -= 1
        alist[low] = alist[high]                     # 把这个值赋给low
        while alist[low] < pivot and low < high:     # 从左到右找到第一个大于pivot的值的角标
            low += 1
        alist[high] = alist[low]
    alist[low] = pivot                               # 循环结束，low与high相遇，把pivot的值赋给low处
    quick_sort(alist, start, low-1)                  # 小于pivot的数列排序
    quick_sort(alist, low+1, end)                    # 大于pivot的数列排序

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)