import pandas as pd

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
        print(f'Iteration {i + 1}: w = {w}, b = {b}, Cost = {cost}')
    
    return w, b


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
    
# X = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10]]
# Y = [2, 4, 5, 4, 5]

data = pd.read_csv('Real estate.csv')

X = data.iloc[:300, 1:-1] #Lay tat ca cac cot tru cot cuoi
Y = data.iloc[:300, -1] #Lay cot cuoi
Z = data.iloc[300:, 1:-1]
T = data.iloc[300: , -1]

X = X.to_numpy()
Y = Y.to_numpy()
Z = Z.to_numpy()
T = T.to_numpy()

alpha = 1e-7
iterations = 10000
initial_w = [0, 0, 0, 0, 0, 0]  # Initialize weights for each feature
initial_b = 0

w, b = gradient_descent(X, Y, initial_w, initial_b, alpha, iterations)

print("w:", w)
print("b:", b)
print("Cost after training:", compute_cost(X, Y, w, b))


a_dict, b_dict, c_dict = Test(Z, T, w, b)
print(f'a: {a_dict.keys()}, count: {len(a_dict)}')
print(f'b: {b_dict.keys()}, count: {len(b_dict)}')
print(f'c: {c_dict.keys()}, count: {len(c_dict)}')





