from __future__ import division, print_function, unicode_literals
import csv
import numpy as np
import matplotlib.pyplot as plt

X = []
with open('test.csv') as csvDataFile:
    file = csv.reader(csvDataFile)
    file.next();
    for row in file:
        X.append(row[0])

X = np.array(X, dtype=float).T

w_0 = -0.107265464301
w_1 = 1.00065638186

with open('predict.csv',"wb") as output :
    writer = csv.writer(output)
    writer.writerow(['X', 'y'])
    for x0 in X:
        y0= w_0 + w_1*x0
        writer.writerow([x0, y0])

plt.plot(x0, y0)
plt.plot(X,w_1*X+w_0)
plt.axis([0, 100, 0, 100])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
