def code(*args, **kwargs):
    print(args, kwargs)
    a = args
    print(a)
    return a

a = {
    'a': 5,
    'b': 6,
    'c': 'a+b'
}

b = code(a)
print(b)