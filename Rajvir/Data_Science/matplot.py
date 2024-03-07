#ploting with matplot>>
import numpy as np
import matplotlib.pyplot as plt 
x = [1,2,3,4,5,6]
y = [9,4,6,3,7,5]

 #plt.plot(x,y)

# plt.xlabel('X - axis')
# plt.ylabel('Y- axis')
# plt.title('simple line graph')

# plt.show()

#histogram 
data = np.random.random(1000)

# plt.hist(data,bins=100, color ="skyblue")
# plt.xlabel("values")
# plt.ylabel("frequency")
# plt.title("histogram")
# plt.grid(axis="y")

# plt.show()

#pie chart 
labels = ['A','B','C','D','E']
sizes = [1,2,3,4,5]

plt.pie(sizes, labels = labels, autopct='%1.1f%%',startangle=140, colors=['red','pink','lightgreen','skyblue','brown'])
plt.axis('equal')
plt.title("the pie chart")
plt.show()