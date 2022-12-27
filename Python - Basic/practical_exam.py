import pandas as pd
import math as math
import scipy
from scipy import stats
import numpy as np
from scipy.optimize import curve_fit
import random as r


# 2nd degree 6=======================================
x = np.array([16,18.5,22,27,32,37,42])
y = np.array([34,86.5,111.1,113.9,84.5,35.4,6.8])

def func(x, a, b, c):
    return a*x**2 + b*x + c


popt, pcov = curve_fit(func, x, y)

predicted = func(45, *popt)

print("The predicted number of births for a woman at age 45 using the 2nd order polynomial is:", predicted)


# 4th degree
def func1(x,a,b,c,d,e):
    return a*x**4+b*x**3+c*x**2+d*x+e

pop, pcov = curve_fit(func1, x, y)

predicted1 = func(45, *pop)

print("The predicted number of births for a woman at age 45 using the 4nd order polynomial is:", predicted1)



# correlation coefficient 7=======================================

x=(16,18.5,22,27,32,37,42)
y=(34,86.5,111.1,113.9,84.5,35.4,6.8)

#creating data frame and converting it into array
# df=pd.DataFrame({'x':x,'y':y})
# X=np.array(df['x'])
# Y=np.array(df['y'])

#calculating correlation coefficient
corr_coef=np.corrcoef(x,y)[0,1]
print("The correlation coefficient between X and Y is: ", corr_coef)


x = np.array([16, 18.5, 22, 27, 32, 37, 42])
y = np.array([34, 86.5, 111.1, 113.9, 84.5, 35.4, 6.8])

# Define a third order polynomial fit 
def f(x, A, B, C, D):
    return A*x**3 + B*x**2 + C*x + D

# Fit the function to the data
params, params_covariance = curve_fit(f, x, y)

A, B, C, D = params

print(f"A:{A}, B:{B}, C:{C}, D:{D}")

# Calculate the residuals
residuals = y - f(x, A, B, C, D)

print(residuals)



# Linear Regression 8=======================================

x = [0,5,10,15,20]
y = [100,200,450,950,2000]

slope, intercept, r, p,std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

rg = myfunc(25)

print(rg)


# probability 9=======================================

Head=0
Tail=0
Repetation = int(input("Enter the number of repetation: "))
for i in range(Repetation):
    cont = r.randint(0,1)
    if(cont==0):
        Head = Head + 1
    else:
        Tail = Tail + 1
print("Head: {} & Tail: {}".format(Head,Tail))


n = int(input("Enter the number of coin tossed: "))
r = int(input("Enter the number of heads to be appeared: "))
Prob = (math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))*math.pow(0.5,n)
print("Probability: ",Prob)




# binom 10=======================================
n = int(input("Enter a total chip: "))
g = int(input("Enter a good chip: "))

bad = n-g

p = g/n
q = 1-p

N = int(input("Enter a total chip: "))
x = int(input("Enter a good chip: "))


sum = 0
for i in range(x,N+1):
    prob = scipy.stats.binom.pmf(i, N, p)
    sum = sum + prob

print(sum)

sum1 = 0
for i in range(35,N+1):
    prob1 = scipy.stats.binom.pmf(i, N, p)
    sum1 = sum1 + prob1

print(sum1)

sum3 = 0
for i in range(35):
    prob3 = scipy.stats.binom.pmf(i, N, p)
    sum3 = sum3 + prob3

print(sum3)