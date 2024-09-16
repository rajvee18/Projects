import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.045
    

    for i in range(iterations):

        y_predicted = m_curr*x + b_curr
        
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr =m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        

        print(f"m {m_curr}, b {b_curr}, iteration {i}, cost {cost}")

    return m_curr,b_curr
    







        
