def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]

    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

print(quick_sort([1,3,2,4,5,6,7]))

'''
   캡스톤
   소공
   알고리즘
'''