import numpy as np

image = np.array([
    [0 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0],
    [1 ,1 ,1 ,1 ,1],
    [0 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0],
])

print("Original image : \n",image)

kernal = np.array( [
    [-1 , -1 , -1],
    [0 , 0 , 0],
    [1 , 1 , 1]
])

print("\nKernal : \n",kernal)

feactuer_map = np.zeros((3,3))

# travel kernal on image
print("\nStep wise calculation:\n")
cnt = 1
for i in range(3):
    for j in range(3):

        portion = image[i:i+3,j:j+3]

        res = np.sum(portion * kernal)

        print(f"\nStep {cnt}:")
        print("\nImage Region : \n",portion)
        print("\nKernal : \n",kernal)
        print(f"\nResult of Multiplication : {res}\n")

        feactuer_map[i][j] = res
        cnt+=1
        print("-"*30)   
         
print("\nFeactures Map :\n",feactuer_map)    