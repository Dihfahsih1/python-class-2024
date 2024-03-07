import matplotlib.pyplot as plt 
import numpy as np

#ploting a simple line graph
x = [1,2,3,4,5,6]
y = [6,7,8,9,10,20]

# plt.plot(x,y)

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple line graph")

# plt.show()


#bar graph

categories = ["A", "B", "C", "D", "E"]
values = [1,2,3,4,5]

# plt.bar(categories, values, color= 'grey')
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.title("A bar graph")
# plt.grid(axis='y')

# plt.show()

#histogram

# data = np.random.random(1000)
# plt.hist(data, bins=100, color='skyblue')
# plt.xlabel("Values")
# plt.ylabel("Frequency")
# plt.title("The histogram")
# plt.grid(axis='y')

# plt.show()

#pie chart

lables= ["A", "B", "C", "D", "E"]
sizes = [5,6,7,4,3]

plt.pie(sizes, lables=lables, autopct='%1.1f%%', startangle=140, colors=['red', 'green', 'blue', 'yellow', 'purple'])
plt.axis('equal')
plt.title("The pie chart")

plt.show()