nums = [
    0,
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    160,
    170,
    180,
    190,
    200,
    210,
    220,
    230,
    240,
    250,
    260,
    270,
    280,
    290,
    300,
    0,
]


# We use dictionary as hash map to store previous elements.
# Then,the current element is checked if it already exists in hash map.
def has_duplicate(nums):
    temp = {}
    for i in nums:
        if i in temp:
            return True
        temp[i] = str(i)
    return False


print(has_duplicate(nums))
