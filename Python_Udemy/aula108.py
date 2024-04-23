# count é um iterador sem fim (itertools)
from itertools import count

c1 = count()

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))

