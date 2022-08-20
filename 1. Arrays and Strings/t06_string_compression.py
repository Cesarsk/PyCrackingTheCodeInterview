"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters.

For example, the string aabcccccaaa would become a2blc5a3.

If the "compressed" string would not become smaller than the original string,
your method should return the original string.

You can assume the string has only uppercase and lowercase letters (a - z).
"""


# Complexity: O(p + k^2) where p is the length of the string and k the number of character sequences
def string_compression(value):
    count = 0
    res = ""

    for i in range(1, len(value)):
        if value[i] == value[i - 1]:
            count += 1
        else:
            res = f"{res}{value[i - 1]}{count}"
            if i == len(value) - 1:
                res = f"{res}{value[-1]}{1}"
            count = 0

    return res if len(res) < len(value) else value


res = string_compression("aaaaabbbbbbbc")
print(res)
