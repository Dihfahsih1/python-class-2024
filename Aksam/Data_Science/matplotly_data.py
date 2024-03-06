import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [9,4,7,3,6,5]

# plt.plot()

labels = ["A","B","C","D","E"]
sizes = [21,54,32,13,100]
plt.pie(sizes,labels=labels,autopct="%1.1f%%                                                                                                                                     ",startangle=140, colors=["red", "gold", "yellow", "green", "purple"])
plt.axis("equal")
plt.title("The pie Chart")
plt.show()