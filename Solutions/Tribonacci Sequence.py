def Tribonacci(signature, n):
    summa = signature[:n]
    for i in range(n - 3):
        summa.append(sum(summa[-3:]))
    return summa
