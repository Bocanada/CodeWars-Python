class Memoize:

    def __init__(self, n):
        self.n = n
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.n(*args)
            print(self.memo[args])
        return self.memo[args]


@Memoize
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
