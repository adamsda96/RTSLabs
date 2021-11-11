
# Finds the the count of values above and below the comparison value
def above_below(in_list: list, comp_val: int) -> dict:
    # Initialize all variables
    below: int
    above: int
    result: dict

    # Tries to find the values above and below the comparison value however if the value is not contained in the list
    # The function will go to the except statement
    try:
        below = in_list.index(comp_val)  # Finds the index of the comparison value also the count of below elements
        above = len(in_list) - below - 1  # Above is count of all other elements minus the comparison value

    # If comparison value is not in list set below and above to None
    except ValueError:
        print("comparison value not in list")
        below = None
        above = None

    result = {"above": above, "below": below}  # Sets values in dictionary

    return result


# Rotate string
def string_rotation(in_string: str, rotation: int) -> str:
    # Initialize variables
    length: int
    adj_rotation: int
    result: str

    length = len(in_string)
    adj_rotation = length - (rotation % length)  # Adjust rotation if ration >= length of string

    result = in_string[adj_rotation:length] + in_string[0:adj_rotation]  # Ending of string + beginning split by rotation

    return result


if __name__ == '__main__':
    print(above_below([1, 2, 3, 4, 5, 6], 0))
    print(string_rotation('MyString', 190156))
