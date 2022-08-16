# Check Permutation: given two strings, write a method to decide if one is a permutation of the other.

value_a = "abcd"
value_b = "bdac"
value_c = "debc"


# this should be o(n)
def check_permutation_pythonic(string_a, string_b):
    return all([a in string_b for a in string_a])


def check_permutation_pythonic_counter(string_a, string_b):
    from collections import Counter
    return Counter(string_a) == Counter(string_b)


def check_permutation_by_sort(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    string_a, string_b = sorted(string_a), sorted(string_b)
    for i in range(len(string_a)):
        if string_a[i] != string_b[i]:
            return False
    return True


def check_permutation_by_count(string_a, string_b):
    if len(string_a) != len(string_b):
        return False

    counter = [0] * 256
    for c in string_a:
        counter[ord(c)] += 1
    for c in string_b:
        if counter[ord(c)] == 0:
            return False
    return True


# this is at most o(n)
def check_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False

    for a in string_a:
        if a not in string_b:
            return False

    return True


res = check_permutation_by_sort(value_a, value_b)
print(res)
