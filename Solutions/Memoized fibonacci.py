def fibonacci(n):
    memo = {0: 0, 1: 1}

    def fib(x):
        if x not in memo:
            memo[x] = fib(x - 1) + fib(x - 2)
        return memo[x]
    return fib(n)
