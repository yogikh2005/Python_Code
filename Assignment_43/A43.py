from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    ############################################################################
    # Step 1 : load th dataset
    ############################################################################
    
    df = pd.read_csv("PlayPredictor.csv")

    ############################################################################
    # Step 2 : Data Anyalises(EDA)
    ############################################################################
    
    # drop first column
    df = df.drop(df.columns[0], axis=1)

    # create encoders
    weather_encoder = LabelEncoder()
    temp_encoder = LabelEncoder()
    play_encoder = LabelEncoder()

    # encode columns
    df['Whether'] = weather_encoder.fit_transform(df['Whether'])
    df['Temperature'] = temp_encoder.fit_transform(df['Temperature'])
    df['Play'] = play_encoder.fit_transform(df['Play'])

    print(df)
    print("Dataset shape :", df.shape)

    features = ["Whether", "Temperature"]

    X = df[features]
    Y = df["Play"]
   
    ############################################################################
    # Step 3 : Data Visulation
    ############################################################################
      
    plt.scatter(X['Whether'], X['Temperature'], c=Y)

    plt.xlabel("Weather")
    plt.ylabel("Temperature")
    plt.title("Dataset Visualization")

    #plt.show()

    ############################################################################################################
    # Step 4 : Split the dataset for training and testing
    ###########################################################################################################

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.3)

    print("X Shape :", X.shape)
    print("Y Shape :", Y.shape)
    print("X_train Shape :", X_train.shape)
    print("X_test Shape :", X_test.shape)
    print("Y_train Shape :", Y_train.shape)
    print("Y_test Shape :", Y_test.shape)

    ############################################################################
    # Step 5 : model create and train
    ############################################################################

    # model creation
    model = KNeighborsClassifier(n_neighbors=2)

    # train
    model.fit(X_train, Y_train)

    ############################################################################
    # Step 6 :  model testing
    ############################################################################

    # test sample

    Y_pred = model.predict(X_test)  

    decoded = play_encoder.inverse_transform(Y_pred)

    print("Encoded Prediction :", Y_pred)
    print("Actual :", Y_test)
    print("Decoded Prediction :", decoded)

    ############################################################################
    # Step 6 :  model performance
    ############################################################################

    accuracy=accuracy_score(Y_pred,Y_test)

    print("Model testing accuracy is : ",accuracy*100)

if __name__ == "__main__":
    main()

'''
 Explanation :
    
    K = 3 - > Accuracy : 88.88
    K = 2 - > Accuracy : 77.77
    K = 4 - > Accuracy : 55.55
    
'''
