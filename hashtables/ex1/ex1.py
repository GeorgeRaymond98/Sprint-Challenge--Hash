def get_indices_of_item_weights(weights, length, limit):

    weight = dict()
    for i in range(0, length):
        weight[weights[i]] = i

    # Loop through weights to look for the solution
    for i in range(0, length):
        if limit - weights[i] in weight:
            weight_index1 = i
            weight_index2 = weight[limit - weights[i]]
            # if index weight 1 is less than index wight of 2 
            if weight_index1 < weight_index2:
                weight_index1, weight_index2 = weight_index2, weight_index1
            return (weight_index1, weight_index2)
    return None
