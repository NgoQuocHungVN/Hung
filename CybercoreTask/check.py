from __future__ import division, print_function, unicode_literals
import csv
import numpy as np

X = []
y = []
with open('predict.csv') as csvDataFile:
    file = csv.reader(csvDataFile)
    file.next();
    for row in file:
        X.append(row[1])
    X = np.array(X, dtype=float).T

with open('realpredict.csv') as Datafile:
    realfile = csv.reader(Datafile)
    realfile.next();
    for realrow in realfile:
        y.append(realrow[1])
    y = np.array(y, dtype = float).T

count = 0
error = 0
while count < len(X):
        error += abs(X[count] -y[count])
        count += 1
print('sum of error = ', error)
print('average of error = ', error/ len(X))


