import numpy as np
import matplotlib.pyplot as plt
from numpy.random import RandomState

x=np.linspace(1,20,100)

np.random.seed(42)
y=[]
for i in x:
    if i<5:
        y.append(0)
    elif 5<i<7.5:
        lab=np.random.randint(2)
        y.append(lab)
    elif 7.5<i<12.5:
        y.append(1)
    elif 12.5<i<15:
        lab=np.random.randint(2)
        y.append(lab)
    else:
        y.append(0)
y=np.array(y)

plt.scatter(x, y, c ="blue", s = 2)
plt.xlabel("x")
plt.ylabel("y")

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 100000
    n = len(x)
    learning_rate = 0.0002
    

    for i in range(iterations):

        y_predicted = m_curr*x + b_curr
        
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr =m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        

    print(f"m {m_curr}, b {b_curr}, iteration {i}, cost {cost}")

    return m_curr,b_curr,cost



m,b,cost = gradient_descent(x,y)
plt.scatter(x, y, c ="blue", s = 2)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,m*x+b)


mean = np.mean(x)
std = np.std(x)
var = std**2

y_ = np.exp((-1*(m*x+b-mean)**2)/(2*var))/((2*np.pi*var)**0.5)
plt.scatter(x,np.exp((-1*(m*x+b-mean)**2)/(2*var))/((2*np.pi*var)**0.5),color='red')
plt.scatter(x,y)


import numpy as np

# Assuming x, y, mean, and var are defined elsewhere in the code
# Initialize m and b
m=0
b=0

def gaussian_nll(b, m):
    pred_y = (np.exp((-1 * (m * x + b - mean)**2) / (2 * var))) / ((2 * np.pi * var)**0.5)  # Gaussian model
    # Negative log-likelihood for Gaussian distribution
    loss = 0.5 * np.sum(np.log(2 * np.pi * var) + ((y - pred_y)**2) / var)
    return loss

iterations = 5000
learning_rate = 0.001

for i in range(iterations):
    y_pred = (np.exp((-1 * (m * x + b - mean)**2) / (2 * var))) / ((2 * np.pi * var)**0.5)
    md = np.sum((y - y_pred) * (x * (m * x + b - mean)) / var)
    bd = np.sum((y - y_pred) * ((m * x + b - mean)) / var)

    b = b - learning_rate * bd
    m = m - learning_rate * md
    loss = gaussian_nll(b, m)

    if i%2==0:
        print(loss)

print(f'm {m}, b {b}, loss {loss}')

plt.scatter(x,np.exp((-1*(m*x+b-mean)**2)/(2*var))/((2*np.pi*var)**0.5),color='red')
plt.scatter(x,y)

plt.show()