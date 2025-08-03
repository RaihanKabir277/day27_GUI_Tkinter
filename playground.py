
# -------------- many positional arguments ---------

def add(*args):
    # print(args)
    # print(args[0])
    sum = 0
    for n in args:
        # print(n)
        # print("+")
        sum += n
    return sum

total = add(3,4,5,6)
print(total)


