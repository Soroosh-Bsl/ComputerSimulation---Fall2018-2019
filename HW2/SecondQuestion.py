import math
from random import *

print("================================")
print("Question 2")
print("================================")
print("Enter lambda in one line separated with single space:")
lambdas = list(map(float, input().split()))
print("Enter starting time of Poisson distributions in one line separated with single space:")
Ts = list(map(float, input().split()))
print("Enter the end time:")
endTime = float(input())


def NSPP(lambdas, Ts, endTime):
    max_lambda = max(lambdas)
    t = 0
    arrivals = []
    while t < endTime:
        R = random()
        E = -1/max_lambda*math.log(R)
        t += E
        index = 0
        if t > endTime:
            break
        for i in range(len(Ts)):
            if Ts[i] >= t:
                index = i-1
                break
        if R < lambdas[index]/max_lambda:
            arrivals.append(t)
    return arrivals


x = NSPP(lambdas, Ts, endTime)
print("Generated Times :", x, sep="\n")
