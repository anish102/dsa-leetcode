"""Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j."""


# We use dictionary as hash map to store the difference between target and current element with the current index.
# We check if the current element already exists in the dictionary.
# If exists, we return the current index along with value(index) of key(difference) from the dictionary.
# Else we store the key values in dictionary and move to next element.
def two_sum(nums, target):
    temp = {}
    for i in range(len(nums)):
        if nums[i] in temp:
            return [temp[nums[i]], i]
        difference = target - nums[i]
        temp[difference] = i
    return []


nums = [3, 4, 5, 6, 7]
target = 10

print(two_sum(nums, target))
