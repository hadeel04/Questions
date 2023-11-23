# function  to calculate the factorial of a number using recursion.

def factorial(n):
    if n == 1 or n == 0:
        return 1

    else:
        return n * factorial(n - 1)

# --------------------------------------------------------------------
# function  to generate all permutations of a string using recursion.

def Permutations(str):

    if len(str) == 1:
        return [str]

    permutations = []
    for i in range(len(str)):
        first_letter = str[i]
        remaining_letters = str[:i] + str[i + 1:]
        permutations_Of_remaining_letters = Permutations(remaining_letters)
        for permutation in permutations_Of_remaining_letters:
            permutations.append(first_letter + permutation)

    return permutations


