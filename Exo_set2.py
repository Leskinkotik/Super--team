# Python function to compute the symmetric difference between two sets

def symmetric_difference(set1, set2):
    """
    Calculate the symmetric difference between two sets.
    
    Parameters:
    set1 (set): A set of numbers.
    set2 (set): Another set of numbers.
    
    Returns:
    set: Symmetric difference between set1 and set2.
    """
    return set1 ^ set2  # Using the ^ operator for symmetric difference

# Example
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Call the function and print the result
sym_diff = symmetric_difference(set_a, set_b)
print("The symmetric difference between set_a and set_b is:", sym_diff)
