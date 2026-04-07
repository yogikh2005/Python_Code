# Given dataset
data = [
    [25, 20000],
    [30, 40000],
    [35, 80000]
]

# Separate columns
col1 = [row[0] for row in data]
col2 = [row[1] for row in data]

# Function to calculate mean
def mean(lst):
    return sum(lst) / len(lst)

# Function to calculate standard deviation
def std(lst, m):
    return (sum((x - m) ** 2 for x in lst) / len(lst)) ** 0.5

# Calculate mean and std for each column
mean1 = mean(col1)
mean2 = mean(col2)

std1 = std(col1, mean1)
std2 = std(col2, mean2)

# Standardize data
scaled_data = []
for x, y in data:
    z1 = (x - mean1) / std1
    z2 = (y - mean2) / std2
    scaled_data.append([z1, z2])

# Print results
print("Mean:", [mean1, mean2])
print("Standard Deviation:", [std1, std2])
print("Scaled Dataset:")
for row in scaled_data:
    print(row)