import numpy as np
# This script calculates the sum of an array and modifies its elements
x = [0,1,2,3,4,5,6,7,8,9,10]
y = []

def function(index):
    return (index + 3) / 2

def numpy_function():
    x_np = np.array(x)
    y_np = x_np + 3 / 2
    return y_np

if __name__ == '__main__':
    print(sum(x))

    for i in x:
        y.append(function(i))
    print(y)
    print(numpy_function())

    x_ = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_ = x_ + 3 / 2
    print(y_)