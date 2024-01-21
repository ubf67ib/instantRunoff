def indexes(arr, value):
    returns = []
    for i in range(len(arr)):
        if arr[i] == value:
            returns.append(i)
    return returns
