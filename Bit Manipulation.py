# function  to check if a given number is even or odd using bit manipulation.

def even_or_odd(n):

    if (n & 1) == 1:
        return "odd"
    else:
        return "even"

#-------------------------------------------------------------------------------
# function to find the number of set bits in a given integer using bit .

def  number_of_set_bits(n):

    count = 0
    while (n):
        count += n & 1
        n >>= 1

    return count


