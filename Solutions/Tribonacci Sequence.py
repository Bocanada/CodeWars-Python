

def tribonacci(signature, n):
    seq = []
    if n == 0:
        return []
    elif n == 1:
        seq.append(signature[n-1])
        return seq
    else:
        count = 3
        a = signature[0]
        b = signature[1]
        c = signature[2]
        while count < n:
            z = a + b + c
            a = b
            b = c
            c = z
            count += 1
            seq.append(z)
        return signature + seq


print(tribonacci([6, 7, 13], 2))
