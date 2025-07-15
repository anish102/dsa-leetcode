"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
"""


# Checks if brackets in a string are balanced by using a dictionary to match opening and closing brackets.
# Uses a list to track unmatched opening brackets and pops them when a corresponding closing bracket is found.
# Returns True if all brackets are matched, otherwise False.
def is_valid(s):
    pair = {"[": "]", "{": "}", "(": ")"}
    res = []
    for i in s:
        if i in pair:
            res.append(i)
        elif res and i == pair.get(res[-1]):
            res.pop()
        else:
            return False
    return True if not res else False


print(is_valid("[{}]"))
