#!/bin/py
import numpy as np
from sktensor import ndinput, dtensor, cp_als, tucker

T = ndinput.convert_to_tensor('movies/test.csv',0)
T = dtensor(T)
#print T
#P, fit, itr, exectimes = cp_als(T, 3, init='nvecs', fit_method='full', conv=1.00E-07, max_iter=500)
print T.shape
#print fit
#print itr
#print exectimes
core, P, fit, itr, exectimes = tucker.hooi(T, T.shape, init='random', conv=1.00E-06, maxIter = 500)
print "fit", fit
print "itr", itr
totaltime = 0
for time in exectimes:
	totaltime += time

print "totaltime", totaltime
# For Tucker
core -= np.min(core)
core /= np.max(core)
core *= 5-1
core += 1

# For CP
#P = P.toarray()
#P -= np.min(P)
#P /= np.max(P)
#P *= 5-1
#P += 1

#print P.min
#P = P.toarray()
# normalize the input, in place 
#P -= np.min(P)
#P /= np.max(P)

# Convert the 0-1 range into a value in the right range.
#P *= 5 - 1
#P += 1

def mean_absolute_error(P, T):
    """DONE.
    Return the mean absolute error of the predictions.
    """
    return np.abs(P - T).mean()

print mean_absolute_error(core,T)