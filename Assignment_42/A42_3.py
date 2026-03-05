import matplotlib.pyplot as plt
from numpy import linspace

def LinearRegration():
    X = [1,2,3,4,5]
    Y = [20000,25000,30000,35000,40000]           # dataset

    X_bar = (sum(X)/len(X))   # X mean
    Y_bar = (sum(Y)/len(Y))   # Y mean

    print("X_bar : ",X_bar)

    print("Y_bar : ",Y_bar)
    # m = (summation(x-x_bar)*(y-y_bar)) / (summation(x-x_bar)**2)
    
    numerator = 0
    denometer = 0

    for i in range(len(X)):
        numerator = numerator+((X[i]-X_bar) * (Y[i]-Y_bar))
        denometer = denometer+((X[i]-X_bar)**2)

    m = numerator/denometer                        # m (slop)

    print("m(slop) : ",m)

    # C :  Y_bar = m * X_bar + C
    # C =  Y_bar - ( m * X_bar ) 
    
    C = Y_bar - (m * X_bar)   # C 
    
    print("C : ",C)
    # Y = mX_test + C
    X_test = 5

    print(f"Line equation : Y = {m}X + {C}")

    Y_pred = []
    for i in X:
        Y_pred.append(( m * i ) + C)

    print("Predicted Y for X : ",Y_pred)

    # R_Square = summ((Y_prid-Y_bar)**2) / summ((Y-Y_bar)**2)

    numerator = 0
    denometer = 0

    for i in range(len(Y_pred)):
        numerator = numerator + ((Y_pred[i] - Y_bar)**2)
        denometer = denometer + ((Y[i] - Y_bar)**2)

    R_Square = numerator/denometer

    print("R_Square : ",R_Square)

    # MSE = summ((y-y_prid)** 2) / N

    numerator = 0

    for i in range(len(Y_pred)):
        numerator = numerator +(( Y[i] - Y_pred[i])**2)
    
    MSE= numerator / len(X)

    print("MSE : ",MSE)   

    X_test=6
    Y_pred=( m * X_test ) + C

    print(f"Predicted  Salary for {X_test} Years Exaperience : {Y_pred}")


    x=linspace(1,6,len(X))
    y=C+m*x

    plt.plot(x,y,color='g',label="Regression Line")
    plt.scatter(X,Y,color="r",label="Scatter plot")

    plt.scatter(X_test,Y_pred,color="b",label="Predicted")

    plt.xlabel("X : Indepedednt varible Experience")
    plt.ylabel("Y : Depedednt varible Salary")

    plt.legend()
    plt.show()

def main():
    LinearRegration()
  

if __name__=="__main__":
    main()