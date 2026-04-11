import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,confusion_matrix,ConfusionMatrixDisplay,classification_report)
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

#-----------------------------------------------------------------
# Fucntion Name  : TrainDiabetesmodel
# Description    : It does split X , Y , training 
# Paramaters     : title(str)
# Return         : None
# Date           : 10/04/2026
# Author         : Yogiraj Khaladkar
#------------------------------------------------------------------

def TrainDiabetesmodel(df):
        # split featcures S
        X = df.drop("Outcome",axis=1)
        Y = df["Outcome"]

        print("Feactures : ")
        print(X.head())

        print("Label : ")
        print(Y.head())

        print("Shape of X :",X.shape)
        print("Shape of Y :",Y.shape)

        X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

        print("Shape of X_train :",X_train.shape)
        print("Shape of X_test :",X_test.shape)
        print("Shape of Y_train :",Y_train.shape)
        print("Shape of Y_test :",Y_test.shape)

        model=DecisionTreeClassifier(criterion="gini",random_state=42,max_depth=2)

        model.fit(X_train,Y_train)

        print("Model trained successfully")

        Y_pred=model.predict(X_test)

        accuracy = accuracy_score(Y_pred,Y_test)

        print("Accuracu is : ",accuracy)

        print(Y_pred)

        cm= confusion_matrix(Y_pred,Y_test)

        print("confusion matrix : \n",cm)

        print("Classification report:")
        print(classification_report(Y_test,Y_pred))

        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title("Confusion Matrix")
        plt.show()

        result_df = X_test.copy()

        # Add columns
        result_df['Actual'] = Y_test
        result_df['Predicted'] = Y_pred

        # Save to CSV
        result_df.to_csv("final_diabetes_predictions.csv", index=False)
#-----------------------------------------------------------------
# Fucntion Name : DisplayInfo
# Description   : It display the formated title
# Paramaters    : title(str)
# Return        : None
# Date          : 10/04/2026
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
# Date           : 10/04/2026
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

    sns.countplot(x='Outcome', data=df)
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
# Fucntion Name : CleanDiabetesData
# Description : It does preprocessing
#               It handle missing values
# Paramaters : df -> Pandas dataframe
# Return :     df -> Clean Pandas dataframe
# Date : 10/04/2026
# Author : Yogiraj Khaladkar
#------------------------------------------------------------------
def CleanDiabetesData(df):
    DisplayInfo("Step 2 : Original Data")
    print(df.head)


    # Handle SkinThickness columns

    if "SkinThickness" in df.columns:
        print("SkinThickness columns before filling missing value :")
        print(df["SkinThickness"].head(10))

        # replace the zero with nan
        df['SkinThickness'] = df['SkinThickness'].replace(0, np.nan)

        # coerce invalied value gets converted as NAN
        df["SkinThickness"] = pd.to_numeric(df["SkinThickness"],errors="coerce")

        SkinThickness_median=df["SkinThickness"].median()
        
        # Replace missing value
        df["SkinThickness"]=df["SkinThickness"].fillna(SkinThickness_median)

        print("SkinThickness columns after preprocessing")
        print(df["SkinThickness"].head(10))


    # Handle Insulin columns 
    if "Insulin" in df.columns :
        print("\n Insulin columns before preprocessing")
        print(df["Insulin"].head(10))

        df['Insulin'] = df['Insulin'].replace(0, np.nan)

        # coerce invalied value gets converted as NAN
        df["Insulin"] = pd.to_numeric(df["Insulin"],errors="coerce")

        fare_median=df["Insulin"].median()
    
        df["Insulin"]=df["Insulin"].fillna(fare_median)

        print("Insulin columns after preprocessing")
        print(df["Insulin"].head(10))

        median = df["Insulin"].median()
    
        Q1 = df["Insulin"].quantile(0.25)
        Q3 = df["Insulin"].quantile(0.75)
        IQR = Q3 - Q1
        
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        
        df["Insulin"] = df["Insulin"].apply(lambda x: median if x < lower or x > upper else x)
    if "BMI" in df.columns:
        print("BMI before preprocessing:")
        print(df["BMI"].head(10))

        # Replace invalid zeros with NaN
        df["BMI"] = df["BMI"].replace(0, np.nan)

        # Convert to numeric (coerce errors)
        df["BMI"] = pd.to_numeric(df["BMI"], errors="coerce")

        # Median imputation
        bmi_median = df["BMI"].median()
        df["BMI"] = df["BMI"].fillna(bmi_median)

        print("BMI after preprocessing:")
        print(df["BMI"].head(10))

    if "BloodPressure" in df.columns:
        print("BloodPressure before preprocessing:")
        print(df["BloodPressure"].head(10))

        df["BloodPressure"] = df["BloodPressure"].replace(0, np.nan)
        df["BloodPressure"] = pd.to_numeric(df["BloodPressure"], errors="coerce")

        bp_median = df["BloodPressure"].median()
        df["BloodPressure"] = df["BloodPressure"].fillna(bp_median)

        print("BloodPressure after preprocessing:")
        print(df["BloodPressure"].head(10))

    if "Glucose" in df.columns:
        print("Glucose before preprocessing:")
        print(df["Glucose"].head(10))

        df["Glucose"] = df["Glucose"].replace(0, np.nan)
        df["Glucose"] = pd.to_numeric(df["Glucose"], errors="coerce")

        glucose_median = df["Glucose"].median()
        df["Glucose"] = df["Glucose"].fillna(glucose_median)

        print("Glucose after preprocessing:")
        print(df["Glucose"].head(10))

    

    return df

#-----------------------------------------------------------------
# Fucntion Name : DiabetesLogistic
# Description   : This is main pipeline controller
#                   It load the datset , show raw data
#                   It proprocess the dataset & train the model
# Paramaters    : Data path of datset file
# Return        : None
# Date          : 10/04/2026
# Author        : Yogiraj Khaladkar
#------------------------------------------------------------------
def DiabetesLogistic(Datapath):
    
    DisplayInfo("Step 1 : Loading the Dataset")
    
    df=pd.read_csv(Datapath)

    ShowData(df,"Initial dataset")

    df=CleanDiabetesData(df)

    TrainDiabetesmodel(df)

#-----------------------------------------------------------------
# Fucntion Name  : main()
# Description    : Starting point of the application
# Paramaters     : NOne
# Return         : None
# Date           : 10/04/2026
# Author         : Yogiraj Khaladkar
#------------------------------------------------------------------

def main():
    DiabetesLogistic("diabetes.csv")

if __name__ =="__main__":
    main()