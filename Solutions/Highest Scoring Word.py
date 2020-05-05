def high(x: str):
    # Code here
    di = []
    sd = list(map(list, x.split()))
    for c in sd:
        nums = sum(list(map(lambda v: ord(v) - 96, c)))
        di.append([nums, ''.join(c)])
    return max(di)[1]
