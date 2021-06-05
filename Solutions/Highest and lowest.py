def high_and_low(numbers: str) -> str:
    int_nums = [int(x) for x in numbers.split()]
    return f'{max(int_nums)} {min(int_nums)}'