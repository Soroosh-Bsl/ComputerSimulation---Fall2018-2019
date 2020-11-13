import math
from random import *
import sys

print("================================")
print("Question 1")
print("================================")

print("Enter number of LCGs (k):")
k = int(input())
print("Enter all X0 in one line separated with single space:\n for example next line shows x0_0 to x0_3:\n 2 3 4 5")
x_0 = list(map(int, input().split()))
print("Enter all a in one line separated with single space:\n for example next line shows a_0 to a_3:\n 2 3 4 5")
a = list(map(int, input().split()))
print("Enter all c in one line separated with single space:\n for example next line shows c_0 to c_3:\n 2 3 4 5")
c = list(map(int, input().split()))
print("Enter all m in one line separated with single space:\n for example next line shows m_0 to m_3:\n 2 3 4 5")
m = list(map(int, input().split()))
print("Enter number of required random numbers:")
n = int(input())


def LCG(seed, a, c, m, n):
    result = [(a * seed + c) % m]
    for i in range(1, n):
        result.append((a * result[len(result)-1] + c) % m)
    return result


def CLCG(k, n, x_0, a, c, m):
    LCG_inputs = []
    for i in range(k):
        LCG_inputs.append(LCG(x_0[i], a[i], c[i], m[i], n))
    Xs = []
    for i in range(n):
        random_i = 0
        for j in range(k):
            random_i += ((-1)**(j) * LCG_inputs[j][i]) % m[0]
        Xs.append(random_i % m[0])
    for i in range(n):
        if Xs[i] > 0:
            Xs[i] /= m[0]
        else:
            Xs[i] = (m[0] - 1)/m[0]
    return Xs


randoms = CLCG(k, n, x_0, a, c, m)
print("Uniform Random Numbers:")
print(randoms)


def F_inverse_exp(lambda_exp, u):
    return -1/lambda_exp * (math.log(1-u))


def F_inverse_tri(a, c, b, u):
    if u == 0:
        return a
    elif u == 1:
        return b
    elif math.sqrt(u*(b-a)*(b-c))+a <= c:
        return math.sqrt(u*(b-a)*(b-c))+a
    elif b-math.sqrt((b-a)*(b-c)*(1-u)) > c:
        return b-math.sqrt((b-a)*(b-c)*(1-u))


def exp_random(u, lambda_input):
    result = []
    for i in range(len(u)):
        result.append(F_inverse_exp(lambda_input, u[i]))
    return result


def tri_random(a, c, b, u):
    result = []
    for i in range(len(u)):
        result.append(F_inverse_tri(a, c, b, u[i]))
    return result


exp = exp_random(randoms, 2)
print("Exponential Random Numbers:")
print(exp)
tri = tri_random(0, 2, 4, randoms)
print("Triangular Random Numbers:")
print(tri)
