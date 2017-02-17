#!/bin/py
import numpy as np
from sktensor import matrix, ndinput

R = ndinput.convert_to_tensor('trip advisor/test.csv',0)

N = len(R)
M = len(R[0])
K = 10

P = np.random.rand(N,K)
Q = np.random.rand(M,K)

nP, nQ, e, step = matrix.matrix_factorization(R, P, Q, K, steps=20, alpha=0.01, beta=0.001, conv=0.2)
print np.shape
print nQ.shape
nR = np.dot(nP,nQ.T)
print(nR.shape)
print "error" ,e
print "step", step

def mean_absolute_error(P, T):
    """DONE.
    Return the mean absolute error of the predictions.
    """
    return np.abs(P - T).mean()

print mean_absolute_error(R,nR)