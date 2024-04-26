from threading import *
import numpy as np

def show():
    print("This is a child thread")
def delayed():
    print("Thread after 3 seconds")

t = Thread(target = show())
t.start()
print('This is a parent thread')

a = np.array([1, 2, 3])
print(a.itemsize)

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

print(x + y)
print(np.add(x, y))

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x + y)
print(np.add(x, y))
