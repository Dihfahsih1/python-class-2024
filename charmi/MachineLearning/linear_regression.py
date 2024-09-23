import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Load the dataset
df = pd.read_csv("C:/Users/Dell/Desktop/python-class-2024/charmi/MachineLearning/home_price.csv")

# Scatter plot of the data
plt.xlabel("Area (sq ft)")
plt.ylabel("Price (US$)")
plt.scatter(df.area, df.price, color='red', marker='+')

# Fit the linear regression model
reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)          #area is an independent variable while price is a dependent variable

# Predict the price for 3300 sq ft area
predicted_price = reg.predict([[3300]])

# Plot the regression line
plt.plot(df.area, reg.predict(df[['area']]), color='blue')
plt.show()

# Print the predicted price
print(f"The predicted price for a 3300 sq ft area is: {predicted_price[0]}")
