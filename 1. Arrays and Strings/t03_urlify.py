# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string. (Note: If implementing in Java,
# please use a character array so that you can perform this operation in place.)

# EXAMPLE
# Input: "Mr John Smith", 13 Output: "Mr%20John%20Smith"


def urlify_pythonic(str):
    string_list = string_input.split(' ')
    return "%20".join(string_list)


def urlify_pythonic_replace(str):
    return string_input.replace(' ', '%20')


def urlify_algo(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable

    # there must be at least two trailing spaces for this algorithm to work
    if ord(string[-1]) != ord(string[-2]) != 32:
        return False

    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3: new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list[new_index:])


string_input = "Mr Joe"
res = urlify_algo(string_input, 6)
print(res)
