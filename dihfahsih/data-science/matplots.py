import matplotlib.pyplot as plt
import numpy as np
# x=[1,2,3,4,5,6]
# y=[9,4,7,3,6,5]

# plt.plot(x,y)

# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple line graph')

# plt.show()

#bar graph 

# categories=['A','B','C','D','E']
# values=[5,6,8,3,5]

# plt.bar(categories, values, color='grey')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('A bar graph')
# plt.grid(axis='y')

# plt.show()

#histogram
# data = np.random.random(1000)

# plt.hist(data,bins=100, color='skyblue')
# plt.xlabel("Values")
# plt.ylabel('Frequency')
# plt.title('The hsitogram')
# plt.grid(axis='y')

# plt.show()

#pie chart
labels=['A','B','C','D','E']
sizes = [50,60,80,3,5]

plt.pie(sizes,labels=labels,autopct='%1.2f%%',startangle=10, colors=['red','gold','yellow','skyblue','lightblue'])
plt.axis('equal')
plt.title("The Pie Chart")
plt.show()