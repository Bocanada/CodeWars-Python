def namelist(names):
    # your code here
    namelst = [name['name'] for name in names]
    print(namelst)
    if len(namelst) <= 1:
        return ''.join(namelst)
    else:
        last_two = ' & '.join(namelst[-2:])
        first = [n + ',' for n in namelst[:-2]]
        first.append(last_two)
        return ' '.join(first)
