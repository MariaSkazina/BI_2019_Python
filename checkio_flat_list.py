def flat_list(array):
    flat = []
    for i in array:
        if isinstance(i, list): flat += flat_list(i)
        else: flat.append(i)
    return flat
