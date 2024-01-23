def all_together(*args):
    for i in args:
        yield from i

objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))