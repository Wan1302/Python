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
    dl[col] = (dl[col] - mean) / std
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

def Test(X_test, w, b):
    a = []
    m = X_test.shape[0]
    num_features = len(w)
    for i in range(m):
        prediction = 0
        for j in range(num_features):
            prediction += w[j] * X_test[i][j]
        prediction += b
        a.append(prediction)
    return a

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

Y_prediction = Test(X_test, w, b)
result = pd.DataFrame (
    {"Y_prediction" : Y_prediction, "Y_test" : Y_test, 
     "% Different" : (abs(Y_prediction - Y_test) / Y_test) * 100},
    index = range(1, Y_test.shape[0] + 1)
)
result

print("Number of tests with less than 5% difference: ", result['% Different'][result['% Different'] <= 5.0].count())
print("Number of tests with less than 10% difference: ", result['% Different'][result['% Different'] <= 10.0].count())
print("Number of tests with more than 10% difference: ", result['% Different'][result['% Different'] > 10.0].count())