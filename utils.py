def indexes(arr, value):
    returns = []
    for i in range(len(arr)):
        if arr[i] == value:
            returns.append(i)
    return returns

def minNonZero(arr):
    minn = float("inf")
    for i in arr:
        if i < minn and i != 0:
            minn = i
    return int(minn)