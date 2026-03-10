from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# step 1 : data
Study_hours = np.array([1,2,3,4,5]).reshape(-1,1)
sleep_hour = np.array([7,6,7,6,8])
Marks = np.array([50,55,60,65,70])

# combine features
X = np.hstack((Study_hours, sleep_hour.reshape(-1,1)))

# step 2 : visualization (only 1 feature can be visualized easily)
plt.scatter(Study_hours.flatten(), Marks, label="Actual Data")

# step 3 & 4 : model
model = LinearRegression()
model.fit(X, Marks)

# step 5 : coefficients
print("Coefficients :", model.coef_)  # now 2 values
print("Intercept :", model.intercept_)

# step 6 : prediction
new_data = np.array([[6,7]])   # [study_hours, sleep_hours]
predicted = model.predict(new_data)
print("Predicted Marks:", predicted)

# step 7 : regression line (only for study_hours)
predicted_line = model.predict(X)
plt.plot(Study_hours.flatten(), predicted_line, label="Regression Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend()
plt.show()