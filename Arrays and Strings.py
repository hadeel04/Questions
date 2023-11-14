# Function to reverse a string

def reverse(string):
    string = string[::-1]
    return string

#-------------------------------------------
# Function to find max and min in array

def max_min(list):
    Max = max(list)
    Min = min(list)
    return Max,Min

#-------------------------------------------
# Function to remove duplicates from a sorted array

def remove_duplicates(lst):
    res = list(dict.fromkeys(lst))
    return res

