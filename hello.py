# a = 28.01234
# print('%.2f' % a)
# print(round(a, 2))
# print('{:.2f}'.format(a))

# b = 200
# c = 300
# b, c = c, b
# print(b, c)

# x, y, z = map(int, input("Nhap 3 so nguyen: ").split())
# print(x + y + z)

# from math import *
# print(isqrt(32))
# print(2**10)
# print(pow(27, 1/3))
# print(ceil(2.8))
# print(floor(2.8))
# print(factorial(3))
# print(gcd(25, 100))
# print(comb(25, 2)) #Tinh to hop
#abs max min

# a, b = 100, 200
# res = 'Python' if(a < b) else 'C++'
# print(res)


import numpy as np
from math import *
def my_sinh(x):
    y = (exp(x) - exp(-x)) / 2
    return y

def my_checker_board(n):
    a = np.zeros((n, n))  # Tạo một mảng n x n với giá trị ban đầu là 0
    for i in range(n):
        for j in range(n):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                a[i][j] = 1
    print(a)

def my_triangle(b, h):
    print(0.5*b*h)

def my_split_matrix(m):
    x = m.shape[1] // 2
    m1 = m[:, :x + 1]
    m2 = m[:, x + 1:]
    return [m1,m2]

def my_cylinder(r, h):
    s = float('{:.4f}'.format(2*pi*r**2 + 2*pi*r*h))
    v = float('{:.4f}'.format(pi*r**2*h))
    return [s, v]

def my_n_odds(m):
    count = 0
    for i in range(len(m)):
       if(m[i] % 2 != 0): count += 1
    return count 

def my_twos(x, y):
    a = np.full((x, y), 2)
    return a

def add_string(a1, a2):
    return a1 + a2


def greeting(name, age):
    greeting_str = f'Hi, my name is {name} and I am {int(age)} years old.'
    return greeting_str

def my_donut_area(r1, r2):
    area = np.pi * (r2**2 - r1**2)
    return area

def my_within_tolerance(A, a, tol):
    s = []
    for i in range(len(A)):
        if(abs(A[i] - a) < tol): s.append(A[i])
    return s

def bounding_array(A, top, bottom):
    s = []
    for i in range(len(A)):
        if(A[i] > bottom and A[i] < top): s.append(A[i])
        elif(A[i] >= top):
            A[i] = top
            s.append(A[i])
        else:
            A[i] = bottom
            s.append(A[i])
    return s

if __name__ == '__main__':
    print(bounding_array(np.arange(-5, 6, 1), 3, -3))
    a = ["One", "Two", "Three"]
    b = [1, 2, 3]

    for i, j in zip(a, b):
        print(i, j)