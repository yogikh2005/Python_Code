import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay

from sklearn.neighbors import KNeighborsClassifier

def main():

########################################################
# Step 1 : laod dataset
########################################################
    
    Border="-"*40

    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    df=pd.read_csv("WinePredictor.csv")

    print("Datase loaded")


########################################################
# Step 2 : Data Anyalises
########################################################

    print(Border)
    print("Step 2 : Data Anyalises")    
    print(Border)

    print("df shape : ",df.shape)
    print("Columns in dataset : ",list(df.columns))
    
    print("Null value count : ",df.isnull().sum())
        
    print("Class Distribution : ")
    print(df["Class"].value_counts())

    print("Statical Report of dataset : ")
    print(df.describe())

########################################################
# Step 3 : Decide the independent & dependent varible
########################################################

    print(Border)
    print("Step 3 : Decide the independent & dependent varible")    
    print(Border)

    feactures=[

        'Alcohol','Malic acid',
        'Ash','Alcalinity of ash',
        'Magnesium','Total phenols',
        'Flavanoids','Nonflavanoid phenols',
        'Proanthocyanins','Color intensity',
        'Hue','OD280/OD315 of diluted wines',
        'Proline'
    ]

    X=df[feactures]
    Y=df["Class"]

    print("X shape : ",X.shape)
    print("Y shape : ",Y.shape)

########################################################
# Step 4 : Data visulation
########################################################
  
    df.hist(figsize=(15,15), bins=19)
    plt.suptitle("Histograms of Wine Dataset Features")
    plt.show()

########################################################
# Step 5 : Split dataset for training & testing
########################################################
  
    
    print(Border)
    print("Step 5 : Split dataset for training & testing")    
    print(Border)

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.2)

    print("Data splting activity done")
    
    print("X shape : ",X.shape)
    print("Y shape : ",Y.shape)
    print("X_train shape : ", X_train.shape)
    print("X_test shape : ", X_test.shape)
    print("Y_train shape : ", Y_train.shape)
    print("Y_test shape : ", Y_test.shape)

############################################################################################################
    # Step 6 : Build the model
###########################################################################################################

    print(Border)
    print("Step 6: Build the model")    
    print(Border)

    model=DecisionTreeClassifier(   

        criterion="gini",
        max_depth=3,
        random_state=42
      )
    
    # model=KNeighborsClassifier(
    #       n_neighbors=3
    # )
    
    print("Model Build : ",model)

############################################################################################################
# Step 7 : Train the model
###########################################################################################################

    print(Border)
    print("Step 7 : Train the model")    
    print(Border)   

    model.fit(X_train,Y_train)

    print("Model traied successfully ")

############################################################################################################
# Step 8 : Evaluate the model
#########################################################################################################
    
    print(Border)
    print("Step 6 : Test the model")    
    print(Border)  

    y_pred=model.predict(X_test)

    print("Y_pred shape :" , y_pred.shape)

    print("Actual ans :")
    print(Y_test)

    print("Predicated ans :")
    print(y_pred)


############################################################################################################
    # Step 9 : Evaluate the model performance
###########################################################################################################

    print(Border)
    print("Step 9 : Evaluate the model performance")
    print(Border)

    accuracy=accuracy_score(Y_test,y_pred)
    print("Accuracy of model : ",accuracy*100)

    cm=confusion_matrix(Y_test,y_pred)
    print("confusion matrix : \n",cm)


    print("Classification report : ")
    print(classification_report(Y_test,y_pred))


############################################################################################################
    # Step 10 : Plot confusion matrix
###########################################################################################################

    print(Border)
    print("Step 10 : Plot confusion matrix")
    print(Border)

    data=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
    data.plot()

    plt.title("Confusion matrix if Iirs dataset")
    plt.show()


if __name__=="__main__":
        main()