# The Challenge: "The Social Bridge"
# Write a function called get_shared_interests that takes two lists of strings as input (e.g., interests of Person A and Person B).
# The function should:
#
# **bonus: Identify only the interests that both people share, using a set for an efficient comparison, or set functions
#
# Return a tuple containing:
# The sorted list of shared interests
# The integer count of how many interests they have in common
# Input:

# Output:
#   (['coding', 'hiking'], 2)

def find_common(person_a, person_b) -> tuple:
    set_a = set(person_a)
    set_b = set(person_b)
    common = tuple (set_a & set_b)
    common_len = len(common)
    return list (common),common_len

person_a = ["coding", "hiking", "cooking", "hiking"]
person_b = ["hiking", "gaming", "coding"]
print(find_common(person_a, person_b))
