input_string = "Tact Coa"
output_string = True

# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. +
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE.
# INPUT: TACT COA
# OUTPUT TRUE (BECAUSE ITS PERMUTATION TACO CAT IS A PALINDROME)

permutations = []


def is_palindrome_permutation(string):
    ## BRUTE FORCE APPROACH
    def compute_permutations(string, i=0):
        if i == len(string):
            permutations.append("".join(string))

        chars = list(string)
        for c in range(i, len(chars)):
            chars[i], chars[c] = chars[c], chars[i]
            compute_permutations(chars, i + 1)

    compute_permutations(string)
    print(permutations)
    for perm in permutations:
        perm = perm.replace(' ', '')
        if perm == perm[::-1]:
            return True
    return False


## IMPROVEMENT ON THE BRUTE FORCE APPROACH
def is_palindrome_permutation_improved(string):
    string = string.lower().replace(' ', '')

    # Complexity of compute recursion should be O(n!)
    def compute_permutations(string, i=0):
        if i == len(string):
            check_str = "".join(string)
            if check_str == check_str[::-1]:
                return True

        chars = list(string)
        for c in range(i, len(chars)):
            chars[i], chars[c] = chars[c], chars[i]
            found = compute_permutations(chars, i + 1)
            if found:
                return True

    if compute_permutations(string):
        return True
    return False


## IMPROVEMENT, WITH COUNT (O(N) with N = strength length)
def is_palindrome_permutation_count(string):
    # clean string
    string = string.lower().replace(' ', '')
    hash_count = {}
    for c in string:
        hash_count[c] = hash_count[c] + 1 if c in hash_count else 1

    # no more than one character MUST HAVE an odd count
    odd_count = 0
    for count in hash_count.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False

    return True


## IMPROVEMENT ON COUNT, CHECK WHILE POPULATING THE TABLE,
## WITH COUNT (O(N) with N = strength length)
"""
It's important to be very clear here that this is not necessarily more optimal. It has the same big O time and might even be slightly slower. We have eliminated a final iteration through the hash table, but now we have to run a few extra lines of code for each character in the string.
You should discuss this with your interviewer as an alternate, but not necessarily more optimal, solution.
"""


def is_palindrome_permutation_improvement(phrase):
    phrase = phrase.lower().replace(' ', '')
    table = {}
    count_odd = 0
    for c in phrase:
        if c in table:
            table[c] += 1
        else:
            table[c] = 1

        if table[c] % 2:
            count_odd += 1
        else:
            count_odd -= 1

    return count_odd <= 1


def is_palindrome_permutation_pythonic(phrase):
    from collections import Counter
    counter = Counter(phrase.lower().replace(' ', ''))
    return sum(val % 2 for val in counter.values()) <= 1


def is_palindrome_permutation_bit_vector(phrase):
    r = 0
    phrase = phrase.lower().replace(' ', '')
    for c in phrase:
        val = ord(c)  # ascii value
        mask = 1 << val  # 1 << n pushes a 1 up into bit number n, creating the bit pattern 1 followed by n zeros.
        if r & mask:
            r = r & ~mask  # ~ means -(value+1) i.e. 1000 -> -1001
        else:
            r = r | mask
    return (r - 1) & r == 0  # final result


res = is_palindrome_permutation_pythonic("Acto taco")
print(res)
