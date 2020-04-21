def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    wdict = dict([(a[1], a[0] + 1) for a in enumerate(alphabet)])

    numbers = list()
    for i in text.lower():
        if i not in wdict:
            continue
        else:
            newi = wdict[i]
            numbers.append(str(newi))
    return ' '.join(numbers)
