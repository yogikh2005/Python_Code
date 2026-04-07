import numpy as np

data = [6,7,8,9,10,11,12]

mean = sum(data) / len(data)

print("Mean of data is : ",mean)

variance = sum((x - mean) ** 2 for x in data) / len(data)

std_dev = variance ** 0.5

print("Variance:", variance)
print("Standard Deviation:", std_dev)