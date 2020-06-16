def f_all(iter):
    for el in iter:
        if not el:
            return False
    return True


# True: all values true
l = [1, 3, 4, 5]
print(f_all(l))

# False: all values false
l = [0, False]
print(f_all(l))

# False: one false value
l = [1, 3, 4, 0]
print(f_all(l))

# False: one true value
l = [0, False, 5]
print(f_all(l))

# True: empty iterable
l = []
print(f_all(l))
