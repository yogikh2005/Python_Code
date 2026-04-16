import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay,classification_report, roc_curve, roc_auc_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

#-----------------------------------------------------------------
# Fucntion Name  : TrainBankmodel
# Description    : It does split X , Y , training 
# Paramaters     : title(str)
# Return         : None
# Date           : 15/04/2026
# Author         : Yogiraj Khaladkar
#------------------------------------------------------------------

def TrainBankmodel(df):
        
        DisplayInfo("Step 4: Separate independent and dependent variables")
        # split featcures S
        X = df.drop("y",axis=1)
        Y = df["y"]

        print("Feactures : ")
        print(X.head())

        print("Label : ")
        print(Y.head())

        print("Shape of X :",X.shape)
        print("Shape of Y :",Y.shape)

        DisplayInfo("Step 5: Split the dataset for testing & training")

        X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
        
        print("Shape of X_train :",X_train.shape)
        print("Shape of X_test :",X_test.shape)
        print("Shape of Y_train :",Y_train.shape)
        print("Shape of Y_test :",Y_test.shape)

        DisplayInfo("Step 6: Scale the data")
        scaler = StandardScaler()

        X_train = scaler.fit_transform(X_train)   # learn from train
        X_test = scaler.transform(X_test)   

        print("Scaled data successfully")
        
        DisplayInfo("Step 7: Train model")
        
        model=LogisticRegression()
        
        model.fit(X_train,Y_train)
        
        print("Model trained successfully\n")
        
        Y_pred=model.predict(X_test)

        DisplayInfo("Step 7 : Model Evaluation")

        accuracy = accuracy_score(Y_pred,Y_test)

        print("Accuracu is : ",accuracy*100)

        cm= confusion_matrix(Y_pred,Y_test)

        print("\nconfusion matrix : \n",cm)

        print("\nClassification report:")
        print(classification_report(Y_test,Y_pred))
        
        DisplayInfo("Step 8 : Visualize results")
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title("Confusion Matrix")
        plt.show()

        Y_prob = model.predict_proba(X_test)[:, 1] 

        fpr, tpr, _ = roc_curve(Y_test, Y_prob)
        auc = roc_auc_score(Y_test, Y_prob)
        print("AUC : ",auc)
        plt.plot(fpr, tpr, label=f"AUC = {auc:.2f}")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.legend()
        plt.show()

        DisplayInfo("End")

#-----------------------------------------------------------------
# Fucntion Name : DisplayInfo
# Description   : It display the formated title
# Paramaters    : title(str)
# Return        : None
# Date          : 15/04/2026
# Author        : Yogiraj Khaladkar
#------------------------------------------------------------------
def DisplayInfo(title):
    print("\n"+"="*70)
    print(title)
    print("="*70)

#-----------------------------------------------------------------
# Fucntion Name  : showData
# Description    : It shows basic information about the dataset
# Paramaters     : Dataset(df)
#                  df -> pandas dataframe object
#                  message -> Heading text to display
# Return         : None
# Date           : 15/04/2026
# Author         : Yogiraj Khaladkar
#------------------------------------------------------------------
def ShowData(df,message):
    DisplayInfo(message)

    print("\n First 5 rows of dataset")
    print(df.head)

    print("\n Shape of dataset")
    print(df.shape)

    print("\n Columns of dataset")
    print(df.columns.tolist())

    print("\n Statistics report")
    print(df.describe())

    print("\n Missing value in dataset")
    print(df.isnull().sum())

    sns.countplot(x='y', data=df)
    plt.title("Distribution of Outcome")
    plt.show()

    df.hist(figsize=(12,10))
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12,8))
    sns.boxplot(data=df)
    plt.xticks(rotation=45)
    plt.title("Boxplot for Outlier Detection")
    plt.show()
#-----------------------------------------------------------------
# Fucntion Name    : CleanBankData
# Description      : It does preprocessing
#                    It handle missing values
# Paramaters       : df -> Pandas dataframe
# Return           : df -> Clean Pandas dataframe
# Date             : 14/04/2026
# Author           : Yogiraj Khaladkar
#------------------------------------------------------------------
def CleanBankData(df):
    DisplayInfo("Step 2 : Original Data")
    print(df.head)

    # drop the column which value unknown
    df.drop(['contact','poutcome'], axis=1, inplace=True)

    print("After remove columns dataset")
    print(df.head)
    print(df.shape)

    # labal Encoding
    df['default'] = df['default'].map({'yes':1, 'no':0})
    df['housing'] = df['housing'].map({'yes':1, 'no':0})
    df['loan'] = df['loan'].map({'yes':1, 'no':0})
    df['y'] = df['y'].map({'yes':1, 'no':0})

    # One-Hot Encoding
    df = pd.get_dummies(df, columns=[
    'job', 'marital', 'education', 'month'
    ])

    # Handle balance columns 
    if "balance" in df.columns :
        print("\n balance columns before preprocessing")
        print(df["balance"].head(10))

        df['balance'] = df['balance'].replace(0, np.nan)

        # coerce invalied value gets converted as NAN
        df["balance"] = pd.to_numeric(df["balance"],errors="coerce")

        fare_median=df["balance"].median()
    
        df["balance"]=df["balance"].fillna(fare_median)

        print("Insulin columns after preprocessing")
        print(df["balance"].head(10))

        median = df["balance"].median()
    
        Q1 = df["balance"].quantile(0.25)
        Q3 = df["balance"].quantile(0.75)
        IQR = Q3 - Q1
        
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        
        df["balance"] = df["balance"].apply(lambda x: median if x < lower or x > upper else x)
    
        DisplayInfo("Step 3 : After EDA Dataset")
        print(df.head)
    return df

#-----------------------------------------------------------------
# Fucntion Name : BankLogisticRegression
# Description   : This is main pipeline controller
#                   It load the datset , show raw data
#                   It proprocess the dataset & train the model
# Paramaters    : Data path of datset file
# Return        : None
# Date          : 10/04/2026
# Author        : Yogiraj Khaladkar
#------------------------------------------------------------------
def BankLogisticRegression(Datapath):
    
    DisplayInfo("Step 1 : Loading the Dataset")
    
    df=pd.read_csv(Datapath,sep=";")

    ShowData(df,"Initial dataset")

    df=CleanBankData(df)

    TrainBankmodel(df)

#-----------------------------------------------------------------
# Fucntion Name  : main()
# Description    : Starting point of the application
# Paramaters     : NOne
# Return         : None
# Date           : 10/04/2026
# Author         : Yogiraj Khaladkar
#------------------------------------------------------------------

def main():
    BankLogisticRegression("bank-full.csv")

if __name__ =="__main__":
    main()