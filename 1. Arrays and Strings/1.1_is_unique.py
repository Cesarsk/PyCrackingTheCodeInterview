# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

value_unique = "abcdef"
value_not_unique = "ciao a tutti"


# # # # # # # # # # # # #
# from slowest to fastest
# # # # # # # # # # # # #

# todo study
def is_unique_bit_vector(input_string):
    if len(input_string) > 128:
        return False

    checker = 0
    for c in input_string:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        print(checker)
        checker |= 1 << val
    return True


def is_unique_algorithmic(input_string):
    if len(input_string) > 128:
        return False

    char_set = [False] * 128  # creates 128 elements in a list
    for char in input_string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True


def is_unique_using_set(input_string):
    character_seen = set()
    for char in input_string:
        if char in character_seen:
            return False
        character_seen.add(char)
    return True


def is_unique_hash_table(input_string):
    hash_table = {}

    for c in input_string:
        if c in hash_table:
            return False
        hash_table[c] = 1
    return True


# O(N logN)
def is_unique_sorting(input_string):
    sorted_string = sorted(input_string)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True


def is_unique_pythonic(input_string):
    return len(set(input_string)) == len(input_string)
