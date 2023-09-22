# x, y, z = map(int, input().split())
# print(f'{x}i + {y}j + {z}k')

# def vector_representation(v):
#     components = ['i', 'j', 'k']
#     return ' + '.join(f'{v[i]}{components[i]}' for i in range(len(v)))

# print(vector_representation([2, 3, 4]))

# def Tinh(a, b):
#     return [i + j for i, j in zip(a, b)]
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(Tinh(a, b))


# def Tinh1(x, a):
#     return [x*i for i in a]
# x = 3
# a = [1, 2, 3]
# print(Tinh1(x, a))

from math import *
import numpy as np
# def Tinh2(a, b):
#     return sum(i*j for i,j in zip(a, b))

# a = [1,2,3]
# b = [4,5,6]
# print(Tinh2(a, b))

# def Tinh3(a, b):
#     return [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*b)] for A_row in a]

# a = np.array([[1,2], [3,4]])
# b = np.array([[2,0], [1,3]])
# print(Tinh3(a, b))

# def Transpose(a):
#     for i in a.shape[0]:
#         for j in a.shape[1]:
#             a[i][j] = a[j][i]

#     return a

# print(Transpose([[1, 2, 3], [4, 5, 6]]))

def compute_cost (X, Y, w, b):
    m = len(Y)
    total_cost = 0
    for x, y in zip(X, Y):
        prediction = w * x + b
        total_cost += (prediction - y) ** 2
    return total_cost / (2 * m)

def gradient_descent (X, Y, w, b, alpha, iterations):
    m = len(Y)
    
    for i in range(iterations):
        delta_w, delta_b = 0, 0
        for x, y in zip(X, Y):
            prediction = w * x + b
            delta_b += (prediction - y)
            delta_w += (prediction - y) * x
        
        b -= alpha * delta_b / m
        w -= alpha * delta_w / m
        print(f'Lan hieu chinh thu {i + 1} co b bang {b}, co w bang {w}, co sai so bang {compute_cost(X, Y, w, b)}')
    
    return w, b

# Example usage:
X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

alpha = 0.01
iterations = 1000
initial_w, initial_b = 0, 0

w, b = gradient_descent(X, Y, initial_w, initial_b, alpha, iterations)

print("w:", w)
print("b:", b)
print("Cost after training:", compute_cost(X, Y, w, b))

