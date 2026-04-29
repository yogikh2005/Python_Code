import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    return 1 / (1+math.exp(-z))

def neuron_forward(inputs,weights,bias,activation_func):

    print("inputs(x):",inputs)
    print("weights(w):",weights)
    print("bias(b):",bias)

    z = sum(w*x for w,x in zip(weights,inputs))+bias
    print("Summation(z = w.x + b):",z)

    y_hat = activation_func(z)
    print(f"Activation function : {activation_func.__name__}")
    print("Output(y^):",y_hat)

    return z , y_hat

def plot_sigmoid_relu():

    z_values = np.linspace(-10,10,200)

    sigmoid_values = 1/(1 + np.exp(-z_values))
   
    plt.figure(figsize=(8,5))

    plt.plot(z_values,sigmoid_values,label="sigmoid",linewidth=2,color="blue")
    
    plt.axhline(y=0,color="black",linewidth=0.5)
    plt.axhline(y=1,color="black",linewidth=0.5)
    plt.axvline(x=0,color ="gray",linestyle="--")

    plt.title("Sigmoid Activation Functions")
    plt.xlabel("Summation(z)",fontsize=14)
    plt.ylabel("Activation output",fontsize=14)

    plt.grid(True,linestyle="--",alpha=0.6)

    plt.legend()
    plt.show()
    
def main():
    inputs = [1.0, 2.0 , 3.0]
    weights = [0.6 ,0.4 ,-0.2]
    bias = 0.5
    
    z,y_hat = neuron_forward(inputs,weights,bias,sigmoid)

    plot_sigmoid_relu()

if __name__ =="__main__":
    main()