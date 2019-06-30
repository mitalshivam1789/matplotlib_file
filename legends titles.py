import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[2,4,9,4]
x2=[1,2,3,4]
y2=[2,5,10,3]
plt.plot(x,y,label = 'First line')
plt.plot(x2,y2,label = 'second line')
plt.xlabel('x values') # title to the x axis
plt.ylabel('y values')# title to the y axis
plt.title('interesting \n check it') # title to the graph
plt.legend()
plt.show()