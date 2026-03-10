from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# step 1 : data
Study_hours = np.array([1,2,3,4,5]).reshape(-1,1)
Marks = np.array([50,55,60,65,70])

# step 2 : visualization
plt.scatter(Study_hours.flatten(), Marks, label="Actual Data")

# step 3 & 4 : model
model = LinearRegression()
model.fit(Study_hours, Marks)

# step 5 : coefficients
print("Coefficient :", model.coef_)
print("Intercept :", model.intercept_)

# step 6 : prediction
new_hours = np.array([[6]])   
predicted = model.predict(new_hours)
print("Predicted Marks for 6 hours:", predicted)

# step 7 : regression line
predicted_line = model.predict(Study_hours)

plt.plot(Study_hours.flatten(), predicted_line, label="Regression Line")
plt.scatter(new_hours.flatten(), predicted, label="Predicted Point")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend() 
plt.show()