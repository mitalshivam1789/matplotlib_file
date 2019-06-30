import matplotlib.pyplot as plt

days =[1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','b','r']
plt.pie(slices,
        labels = activities,
        colors = cols,
        startangle= 90,
        shadow = True,
        explode = (0,0.1,0,0.3),
        autopct ='%1.1f%%'
        )
#plt.stackplot(days,sleeping,eating,working,playing,colors = ['m','c','r','k'])
#plt.xlabel('x values') # title to the x axis
#plt.ylabel('y values')# title to the y axis
plt.title('interesting \n check it') # title to the graph

#plt.legend()
plt.show()
# we can't have labels in stackplot