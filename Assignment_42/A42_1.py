
def LinearRegration():
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]           # dataset

    X_bar=(sum(X)/len(X))   # X mean
    Y_bar=(sum(Y)/len(Y))   # Y mean

    print("X_bar : ",X_bar)

    print("Y_bar : ",Y_bar)
    # m = (summation(x-x_bar)*(y-y_bar)) / (summation(x-x_bar)**2)
    
    numerator=0
    denometer=0

    for i in range(len(X)):
        numerator=numerator+((X[i]-X_bar) * (Y[i]-Y_bar))
        denometer=denometer+((X[i]-X_bar)**2)

    m=numerator/denometer                        # m (slop)

    # C :  Y_bar = m * X_bar + C
    # C =  Y_bar - ( m * X_bar ) 
    
    C = Y_bar - (m * X_bar)   # C 
  
    # Y = mX_test + C
    X_test = 6

    Y_pred =  ( m * X_test ) + C

    return Y_pred

def main():
    Y_pred=LinearRegration()
    print("Predicted Y for X : ",Y_pred)

if __name__=="__main__":
    main()