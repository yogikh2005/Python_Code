import numpy as np


matrix = np.array(
    [
        [6,4],
        [8,6]
    ]
)
print("\nOriginal matrix map:\n",matrix)

flattern_output = matrix.flatten()

print("\nFlattern output :\n",flattern_output)

weight = np.array([0.3, 0.4, 0.5, 0.6])
bias = 0.5

print("\nweight :" ,weight)
print("\nbias :",bias)

z = np.sum(flattern_output * weight)+bias

output = max(0,z)

print("\nFinal output is : ",output)

