def f_any(iter):
    for el in iter:
        if el:
            return True
    return False

# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(f_any(l))

# False since both are False
l = [0, False]
print(f_any(l))

# True since 5 is true
l = [0, False, 5]
print(f_any(l))

# False since iterable is empty
l = []
print(f_any(l))
