import numpy as np
from math import *

#Ham tinh Error
def Error(y_thuc, y_dudoan):
    return np.sum((y_thuc - y_dudoan)**2) / len(y_thuc)

#Ham tinh Gradient
def Gradient(X, Y, w, b):
    n = len(X)
    y_dudoan = w*X + b
    gradient_w = (-2/n)*np.sum(X*(Y - y_dudoan))
    gradient_b = (-2/n)*np.sum(Y - y_dudoan)
    return gradient_w, gradient_b

#Ham tinh he so toi uu
def Gradient_descent(X, Y, learning_rate, iterations):
    #Khoi tao gia tri ban dau cua w, b 
    w = optimal_w = 2
    b = optimal_b = 0.5
    Sai_so = 0.0
    error = []
    for i in range(iterations):
        grd_w, grd_b = Gradient(X, Y, w, b)
        w -= learning_rate*grd_w
        b -= learning_rate*grd_b
        z = Error(Y, w*X + b)
        if(i == 0 or Sai_so > z):
            Sai_so = z
            optimal_w = w
            optimal_b = b
        error.append(z)
        print(f'Lan hieu chinh thu {i + 1} co w = {w}, b = {b}, sai so = {z}')
    return optimal_w, optimal_b, error

#He so hoc va so lan hieu chinh
learning_rate = 0.1 
iterations = 10

#Bo du lieu dau vao
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 3.5, 6, 10.5, 15])

if __name__ == '__main__':
    optimal_w, optimal_b, error = Gradient_descent(X, Y, learning_rate, iterations)
    print(f'Gia tri toi uu cho w la {optimal_w}')
    print(f'Gia tri toi uu cho b la {optimal_b}')

