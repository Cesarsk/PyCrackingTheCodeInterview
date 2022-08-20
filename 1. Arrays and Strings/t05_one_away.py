"""

There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character

Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE

pale,   ple     -> true
pales,  pale    -> true
pale,   bale    -> true
pale,   bake    -> false

"""


# O(N) algorithm
def are_one_edit_different(str1, str2):
    # at most 1 edit distant
    if abs(len(str1) - len(str2) > 1):
        return False

    # string_1 must be the shorter one
    string_1 = str1 if len(str1) < len(str2) else str2
    string_2 = str2 if len(str1) < len(str2) else str1

    edited = 0
    i, j = 0, 0

    while i < len(string_1) and j < len(string_2):
        if string_1[i] != string_2[j]:
            if edited:
                return False
            edited = True
            if len(string_1) == len(string_2):
                i += 1 # move shorter pointer
        else:
            i += 1  # if matching, move shorter pointer

        j += 1 # move longer pointer

    return True


print(are_one_edit_different("ale", "bale"))
