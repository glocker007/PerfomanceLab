import sys
numFile = sys.argv[1]
with open(numFile, "r") as f:
    nums = [int(line.rstrip("\n")) for line in f]
print(nums)
def quickselect_median(lst):
    if len(lst) % 2 == 1:
        return quickselect(lst, len(lst) // 2)
    else:
        return 0.5 * (quickselect(lst, len(lst) // 2 - 1) + 
                      quickselect(lst, len(lst) // 2))

def quickselect(lst, k):
    if len(lst) == 1:
        return lst[0]

    pivot = lst[len(lst) // 2]

    lows = [el for el in lst if el < pivot]
    highs = [el for el in lst if el > pivot]
    pivots = [el for el in lst if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

median = quickselect_median(nums)
print(int(sum(abs(median - n) for n in nums)))
    