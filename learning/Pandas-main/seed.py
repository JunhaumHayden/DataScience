import numpy as np



if __name__ == '__main__':
    np.random.seed(42)
    a = np.random.uniform(0, 1, 5)
    print(a)
    np.random.seed(42)
    b = np.random.uniform(0, 1, 5)
    print(b)
    np.random.seed(41)
    c = np.random.uniform(0, 1, 5)
    print(c)