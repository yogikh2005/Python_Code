import math

def Sigmoid(value):
    return 1 / (1 + math.exp(-value))

def Sigmoid_derivatioin(value):
    return value * (1- value)

# Input
x1 = 11.0
x2 = 21.0

# output
target = 1.0

# weights & bias
w1 = 0.2
w2 = 0.3
bias = 0.7

learning_rate = 0.1

print("Initial Values")
print("w1 :", w1)
print("w2 :", w2)
print("b  :", bias)

epochs = 15

for i in range(epochs+1):

    # Weighted sum
    z = (x1*w1)+(x2*w2)+bias

    output = Sigmoid(z)

    # loss
    loss = 0.5 *(target-output)**2

    # Derivatioin of loss to output
    d_out = output - target

    # Dervaition of loss to z
    d_out_z = Sigmoid_derivatioin(output)

    # chain rule
    d_out_dz = d_out - d_out_z

    # gradainets for bias & weights
    d_w1 = d_out_z * x1
    d_w2 = d_out_z * x2
    d_b = d_out_z

    # gradient descent

    w1 = w1 - (learning_rate * d_w1)
    w2 = w2 - (learning_rate * d_w2)
    bias = bias - (learning_rate * d_b)

    print("Epoch:", epochs)
    print("Weighted Sum (z):", round(z, 4))
    print("Predicted Output :", round(output, 4))
    print("Target Output    :", target)
    print("Loss             :", round(loss, 6))
    print("Gradient dL/dw1  :", round(d_w1, 6))
    print("Gradient dL/dw2  :", round(d_w2, 6))
    print("Gradient dL/db   :", round(d_b, 6))
    print("Updated w1       :", round(w1, 6))
    print("Updated w2       :", round(w2, 6))
    print("Updated b        :", round(bias, 6))
    print("-"*50)

print("Final Trained Values")
print("w1 =", round(w1, 6))
print("w2 =", round(w2, 6))
print("b  =", round(bias, 6))  