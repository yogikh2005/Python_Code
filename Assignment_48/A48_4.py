import math

# Given dataset
data = [
    [25, 20000],
    [30, 40000]
]

# Separate points
p1 = data[0]
p2 = data[1]

# Function to calculate Euclidean distance
def euclidean(a, b):
    return math.sqrt(sum((a[i] - b[i])**2 for i in range(len(a))))

# ---- Distance BEFORE scaling ----
dist_before = euclidean(p1, p2)

# ---- Feature Scaling (Standardization) ----

# Separate columns
col1 = [row[0] for row in data]
col2 = [row[1] for row in data]

# Mean
mean1 = sum(col1) / len(col1)
mean2 = sum(col2) / len(col2)

# Standard deviation
std1 = (sum((x - mean1)**2 for x in col1) / len(col1)) ** 0.5
std2 = (sum((x - mean2)**2 for x in col2) / len(col2)) ** 0.5

# Scale points
scaled = []
for x, y in data:
    z1 = (x - mean1) / std1
    z2 = (y - mean2) / std2
    scaled.append([z1, z2])

# Distance AFTER scaling
dist_after = euclidean(scaled[0], scaled[1])

# Results
print("Distance before scaling:", dist_before)
print("Distance after scaling:", dist_after)