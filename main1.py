import numpy as np
from math import *

#Ham tinh Error
def Error(y_thuc, y_dudoan):
    return (1/(2*len(y_thuc)))*np.sum((y_thuc - y_dudoan)**2)

#Ham tinh Gradient
def Gradient(X, Y, w, b):
    y_dudoan = w*X + b
    gradient_w = (-1)*np.sum(X*(Y - y_dudoan))
    gradient_b = (-1)*np.sum(Y - y_dudoan)
    return gradient_w, gradient_b

#Ham tinh he so toi uu
def Gradient_descent(X, Y, learning_rate, iterations):
    m = len(Y)
    #Khoi tao gia tri ban dau cua w, b 
    w, b = 0, 0
    error = []
    for i in range(iterations):
        grd_w, grd_b = 0, 0
        grd_w, grd_b = Gradient(X, Y, w, b)
        w -= learning_rate*grd_w / m
        b -= learning_rate*grd_b / m
        z = Error(Y, w*X + b)
        error.append(z)
        print(f'Lan hieu chinh thu {i + 1} co w = {w}, b = {b}, sai so = {z}')
    return w, b, error

#He so hoc va so lan hieu chinh
learning_rate = 0.01 
iterations = 1000

#Bo du lieu dau vao
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 5, 4, 5])

if __name__ == '__main__':
    optimal_w, optimal_b, error = Gradient_descent(X, Y, learning_rate, iterations)
    print(f'Gia tri toi uu cho w la {optimal_w}')
    print(f'Gia tri toi uu cho b la {optimal_b}')

