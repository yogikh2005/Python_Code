import numpy as np


feactuer_map = np.array(
    [
        [3, 3, 3],
        [0, 0, 0],
        [-3, -3, -3]
    ]
)
print("\nOriginal feacture map:\n",feactuer_map)

output = np.zeros((2,2))

relu_output = np.maximum(0,feactuer_map)

print("\nAfter ReLU feacture map:\n",relu_output)

cnt = 1
for i in range(2):
    for j in range(2):

        portion = relu_output[i:i+2,j:j+2]

        res = np.max(portion)

        print(f"\nStep {cnt}:")

        print("\nfeactuer_map Region : \n",portion)
        print(f"\nResult of Max pooling : {res}\n")

        output[i][j] = res
        cnt+=1
        print("-"*30)    

print("\nMax pooling output  :\n",output) 

