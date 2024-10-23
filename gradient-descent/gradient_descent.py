import numpy as np

def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08

    for i in range(iterations):
        # intercept formula
        y_predict = m_curr * x + b_curr

        # MSE (Cost function)
        cost = (1/n) * sum([val**2 for val in (y-y_predict)])

        # MSE of m derivative
        md = (-2/n) * sum(x * (y - y_predict))

        # MSE of b derivative
        bd = (-2/n) * sum(y - y_predict)

        # slope m
        m_curr = m_curr - learning_rate * md

        # intercept b
        b_curr = b_curr - learning_rate * bd

        # Print every 1000 iterations
        if i % 1000 == 0:
            print(f"m = {m_curr}, b = {b_curr}, cost = {cost} iteration = {i}")

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x, y)