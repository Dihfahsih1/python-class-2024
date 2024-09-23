import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv('C:/Users/Dell/Desktop/python-class-2024/charmi/MachineLearning/homeprices.csv')

import math
median_bedrooms = math.floor(df.bedrooms.median())

df.bedrooms = df.bedrooms.fillna(median_bedrooms)

reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']], df.price)


predicted_price = reg.predict([[3000,3,40]])
print(predicted_price)