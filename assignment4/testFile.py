import numpy as np

a = np.arange(9).reshape(3, 3)

b = np.nditer(a)

c = np.pad(a, [(1,1), (1,1)], 'edge')

print(a)
print(c)

d = a[1:,2:]
#print(d)

"""
it = np.nditer(a, flags=['multi_index'])
while not it.finished:
    #print("%d <%s>" % (it[0], it.multi_index), end=' ')
    #print(it.multi_index[0] - 1, it.multi_index[1] - 1, it.multi_index[2] -1)
    print(it.multi_index[0], it.multi_index[1])
    it.iternext()

"""
