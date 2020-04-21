

def tribonacci(signature, n):
    # Clever way...
    Sum = signature[:n]
    for i in range(n - 3): Sum.append(sum(Sum[-3:]))
    return Sum

    # seq = []
#     # if n == 0:
#     #     return []
#     # elif n == 1:
#     #     seq.append(signature[n-1])
#     #     return seq
#     # else:
#     #     count = 3
#     #     a = signature[0]
#     #     b = signature[1]
#     #     c = signature[2]
#     #     while count < n:
#     #         z = a + b + c
#     #         a = b
#     #         b = c
#     #         c = z
#     #         count += 1
#     #         seq.append(z)
#     #     return signature + seq



print(tribonacci([1, 1, 1], 10))
