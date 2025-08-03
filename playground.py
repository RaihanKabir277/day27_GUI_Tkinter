
# -------------- many positional arguments ---------

# def add(*args):
#     # print(args)
#     # print(args[0])
#     sum = 0
#     for n in args:
#         # print(n)
#         # print("+")
#         sum += n
#     return sum

# total = add(3,4,5,6)
# print(total)

# ---------- many keyword arguments ---------

# def calculate(**kwargs):
    # print(type(kwargs))
    # print(kwargs)
    # print(kwargs["add"]) # for fetch the argument item value
    # for key,value in kwargs.items():
    #     print(value)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=5)

