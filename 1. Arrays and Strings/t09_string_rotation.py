"""
String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl
using only one call to isSubstring (e.g.,"waterbottle" is a rotation of "erbottlewat").
"""


# isSubstring in python is 'in'

# doubling the string is linear with the length of the string
# Substring: the time complexity is O(N) on average,
# O(NM) worst case (N being the length of the longer string, M, the shorter string you search for)
def is_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False


print(is_rotation("waterbottle", "erbottlewat"))
