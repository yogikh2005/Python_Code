from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# step 1 : data
Study_hours = np.array([1,2,3,4,5]).reshape(-1,1)
Marks = np.array([50,55,60,65,70])

# step 2 : data visualization
plt.scatter(Study_hours, Marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# step 3 : model create
model = LinearRegression()

# step 4 : model train
model.fit(Study_hours, Marks)

# step 5 : model coefficient
print("Coefficient :", model.coef_)
print("Intercept :", model.intercept_)

# step 6 : prediction line
predicted = model.predict(Study_hours)

plt.scatter(Study_hours, Marks)
plt.plot(Study_hours, predicted)
plt.show()