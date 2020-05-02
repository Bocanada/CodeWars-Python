def array_diff(a, b):
    # your code here
    if not a:
        return []
    else:
        diff = [i for i in a + b if i not in b]
        return diff
