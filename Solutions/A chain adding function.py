class Add(int):
    def __call__(self, v):
        return Add(self + v)
