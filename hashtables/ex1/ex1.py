



def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    weight_dict = dict()

    for i in range(0, length):
        weight_dict[weights[i]] = i
        
    for i in range(0, length):
        if limit - weights[i] in weight_dict:
            weight_index1 = i
            weight_index2 = weight_dict[limit - weights[i]]
            if weight_index1 < weight_index2:
                weight_index1, weight_index2 = weight_index2, weight_index1
            return (weight_index1, weight_index2)

    return None
