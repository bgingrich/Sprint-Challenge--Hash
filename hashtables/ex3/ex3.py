"""
Find the numbers that exist in all lists.

# Make the lists flat
# Count Dict
# Loop through and increment as keys appear in lists
# Return key whose value is equal to length of original
number of arrays

"""
def intersection(arrays):

    """
    YOUR CODE HERE
    """
    flattened_lists = [value for sublist in arrays for value in sublist]

    count_dict = dict()

    for num in flattened_lists:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    
    result = [value[0] for value in list(count_dict.items()) 
    if value[1] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
