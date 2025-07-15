"""Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false."""


# We use two dictionary as hash map to store the character of the string and its count.
# Then, we compare if two dictionaries are equal or not.
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    temp1 = {}
    temp2 = {}
    for i in range(len(s)):
        temp1[s[i]] = temp1.get(s[i], 0) + 1
        temp2[t[i]] = temp2.get(t[i], 0) + 1
    return temp1 == temp2


s = "racecar"
t = "carrace"

print(is_anagram(s, t))
