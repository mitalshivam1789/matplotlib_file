import matplotlib.pyplot as plt

population_ages = [11,22,4,76,54,77,65,73,61,29,49,59,36,45,34,44,32,30,25,5,35,40,55,50,60]
#ids=[x for x in range(len(population_ages))]
bins =[0,10,20,30,40,50,60,70,80]
plt.hist(population_ages,bins,histtype = 'bar',rwidth = 0.6)
plt.xlabel('x values') # title to the x axis
plt.ylabel('y values')# title to the y axis
plt.title('interesting \n check it') # title to the graph
#plt.legend()
plt.show()
