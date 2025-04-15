"""Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1."""


# Performs a binary search on a sorted list nums to find the index of a given target value.
# If the target is found, it returns its index; otherwise, it returns -1.
def search(nums, target):
    count = len(nums)
    l = 0
    r = count - 1
    while r >= l:
        index = (l + r) // 2
        if target == nums[index]:
            return index
        elif target > nums[index]:
            l = index + 1
        else:
            r = index - 1
    return -1
