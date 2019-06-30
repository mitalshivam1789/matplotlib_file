import matplotlib.pyplot as plt
import numpy as np

# Part 1 --------------------
# using csv file
'''
import csv

x =[]
y = []
with open('example','r') as csvfile:
    plots = csv.reader(csvfile,delimiter = ',')# by which it is sepreated like it can be : . in our case it is ,
    for row in plots: # all rows and data is seperated by ,
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label = 'Loaded from file!')
'''



#Part 2 ---------------
# using numpy
x, y = np.loadtxt('example',delimiter=',',unpack = True)
plt.plot(x,y, label = "from loaded file")
# ------------------------

plt.xlabel('x')
plt.ylabel('y')
plt.title('studying matplotlib')
plt.legend()
plt.show()