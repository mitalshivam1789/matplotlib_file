import matplotlib.pyplot as plt

x=[2,4,6,8]
y=[2,4,9,4]
x2=[1,3,5,7]
y2=[2,5,10,3]
plt.bar(x,y,label = 'First line',color = 'r')
plt.bar(x2,y2,label = 'second line',color='c')
plt.xlabel('x values') # title to the x axis
plt.ylabel('y values')# title to the y axis
plt.title('interesting \n check it') # title to the graph
plt.legend()
plt.show()