from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def main():

    ############################################################################
    # Step 1 : load th dataset
    ############################################################################
    
    df = pd.read_csv("Advertising.csv")

    ############################################################################
    # Step 2 : Data Anyalises(EDA)
    ############################################################################
    
    # drop first column
    df = df.drop(df.columns[0], axis=1)

    print(df)
    print("Dataset shape :", df.shape)

    features = ['TV','radio','newspaper']

    X = df[features]
    Y = df["sales"]
   
    ############################################################################
    # Step 3 : Data Visulation
    ############################################################################
      
    plt.scatter(df['TV'], df['sales'], color='red', label="TV")
    plt.scatter(df['radio'], df['sales'], color='blue', label="Radio")
    plt.scatter(df['newspaper'], df['sales'], color='green', label="Newspaper")

    plt.xlabel("Advertising Budget")
    plt.ylabel("Sales")

    plt.legend()
    plt.show()

    ############################################################################################################
    # Step 4 : Split the dataset for training and testing
    ###########################################################################################################

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.5)

    print("X Shape :", X.shape)
    print("Y Shape :", Y.shape)
    print("X_train Shape :", X_train.shape)
    print("X_test Shape :", X_test.shape)
    print("Y_train Shape :", Y_train.shape)
    print("Y_test Shape :", Y_test.shape)

    #############################################################################
    # Step 5 : model create and train
    #############################################################################

    # model creation
    model = LinearRegression()

    # train
    model.fit(X_train, Y_train)

    #############################################################################
    #  Step 6 :  model testing
    #############################################################################

    # test sample

    Y_pred = model.predict(X_test)  

    print("Prediction : ", Y_pred)
    print("Actual : ",Y_test)

    #############################################################################
    #  Step 6 :  model performance
    #############################################################################

    MSE=mean_squared_error(Y_test,Y_pred)

    print("Model MSE : ",MSE)

    r2_=r2_score(Y_test,Y_pred)

    print("R_Square : ",r2_)

    #############################################################################
    # Step 7 : model visualization
    #############################################################################

    plt.figure(figsize=(8,6))
 
    # scatter plot
    plt.scatter(Y_test, Y_pred, alpha=0.7, label="Predicted Points")

    # ideal prediction line
    plt.plot(
        [min(Y_test), max(Y_test)],
        [min(Y_test), max(Y_test)],
        color='red',
        linewidth=2,
        label="Ideal Prediction Line"
    )

    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Actual vs Predicted Sales")

    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()

