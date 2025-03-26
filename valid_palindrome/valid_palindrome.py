"""Given a string s, return true if it is a palindrome, otherwise return false."""


# Uses two pointers (l and r) to scan the string from both ends.
# Skips non-alphanumeric characters and compares the characters at the current positions, ignoring case.
def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


# checks if a character is alphanumeric (either a letter or a digit).
def alphaNum(c):
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )


print(isPalindrome("c!at t _ac"))
