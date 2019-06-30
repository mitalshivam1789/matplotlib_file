import matplotlib.pyplot as plt

x=[1,2,3,4,5,8]
y = [3,5,2,8,5,3]
plt.scatter(x,y, label='skitscat',color = 'c',marker = 'c',s = 500)
plt.xlabel('x values') # title to the x axis
plt.ylabel('y values')# title to the y axis
plt.title('interesting \n check it') # title to the graph
#plt.legend()
plt.show()
