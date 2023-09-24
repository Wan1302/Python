import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


def Hieuchinh(X):
  dl = X.copy(deep = False)
  cols = dl.columns.values
  for col in cols:
    mean = dl[col].mean()
    std = dl[col].std()
    dl[col] = (data[col] - mean) / std
  return dl


# Function to compute cost
def compute_cost(X, Y, w, b):
    m = len(Y)
    total_cost = 0
    for i in range(m):
        prediction = 0
        for j in range(len(X[i])):
            prediction += w[j] * X[i][j]
        prediction += b
        total_cost += (prediction - Y[i]) ** 2
    return total_cost / (2 * m)

# Function to compute w and b using gradient descent
def gradient_descent(X, Y, w, b, alpha, iterations):
    m = len(Y)
    num_features = len(w)
    Cost = []
    for i in range(iterations):
        delta_w = [0] * num_features
        delta_b = 0
        
        for j in range(m):
            prediction = 0
            # Compute y = w_i * x_i + b
            for k in range(num_features):
                prediction += w[k] * X[j][k]
            prediction += b
            
            error = prediction - Y[j]
            
            # Compute gradients
            for k in range(num_features):
                delta_w[k] += error * X[j][k]
            
            delta_b += error
        
        # Update w and b
        for k in range(num_features):
            w[k] -= alpha * delta_w[k]  / m
        
        b -= alpha * delta_b / m
        
        cost = compute_cost(X, Y, w, b)
        Cost.append(cost)
    
    return w, b, Cost

def Test(Z, T, w, b):
    a_dict = {}
    b_dict = {}
    c_dict = {}
    m = len(T)
    num_features = len(w)
    for i in range(m):
        prediction = 0
        error = 0
        for j in range(num_features):
            prediction += w[j] * Z[i][j]
        prediction += b
        error = (abs(prediction - T[i]) / T[i]) * 100
        if(error >= 0 and error <= 5):
            a_dict[i] = error
        elif(error >= 6 and error <= 10):
            b_dict[i] = error
        else:
            c_dict[i] = error
    return a_dict, b_dict, c_dict

data = pd.read_csv('Real estate.csv')
X = data.drop(['Y house price of unit area', 'No'], axis = 1)
Y = data["Y house price of unit area"]

X_train = X[:300]
X_test = X[300:]
Y_train = Y[:300]
Y_test = Y[300:]


Y_train = Y_train.to_numpy()
Y_test = Y_test.to_numpy()

X1 = Hieuchinh(X_train)
X_train = X1.to_numpy()

X2 = Hieuchinh(X_test)
X_test = X2.to_numpy()

iterations = 10000
alpha = 0.001
initial_w = np.array([random.uniform(0, 1) for _ in range(X_train.shape[1])])
initial_b = random.uniform(0, 1)

w, b, Error = gradient_descent(X_train, Y_train, initial_w, initial_b, alpha, iterations)

print("w:", w)
print("b:", b)
print("Cost after training:", compute_cost(X_train, Y_train, w, b))

plt.plot(Error)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.title('Function y = w1x1 + w2x2 + ... + w6x6 + b')
plt.grid(True)
plt.show()

a_dict, b_dict, c_dict = Test(X_test, Y_test, w, b)
print(f'a: {a_dict.keys()}, count: {len(a_dict)}')
print(f'b: {b_dict.keys()}, count: {len(b_dict)}')
print(f'c: {c_dict.keys()}, count: {len(c_dict)}')
