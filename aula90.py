import sys
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
generator = (n for n in range (1000000))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))

print(next(generator))

print(next(generator))

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

    


