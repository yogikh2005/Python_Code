from math import exp

def sigmoid(x):
    return 1/(1+exp(-x))

def Single_neuron(x1,x2,w1,w2,bias):

    z = ((x1*w1)+(x2*w2)+bias)
    print("z : ",z)

    return sigmoid(z)

def main():

    x1 = 2
    x2 = 3
    w1 = 0.4
    w2 = 0.6
    bias = 0.5

    print("x1 : ",x1)
    print("x2 : ",x2)
    print("w1 : ",w1)
    print("w2 : ",w2)
    print("bias : ",bias)


    Res = Single_neuron(x1,x2,w1,w2,bias)
    print("Final output is : ",Res)

if __name__=="__main__":
    main()  

'''
Explanation :
        the sigmoid function which the genrate the output between the 0 to 1.
        

'''