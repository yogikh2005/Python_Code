import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score)

########################################################## 

# Step 1: dataset load

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath)

print("Dataset loaded successfully")


############################################################    

# Step 2: Data Analysis(EDA)

print("Shape of dataset : ",df.shape)
print("Columns of dataset : ",df.columns)

print("Missing values : ", )
print(df.isnull().sum())

print("class ditribution : ")
print(df["FinalResult"].value_counts())

print("Statical report of dataset :")
print(df.describe())

#############################################################

# Step 3 : Decide Independent & Dependet Varible

print("Decide Independent & Dependet Varible")

feacture_cols=[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X=df[feacture_cols]
Y=df["FinalResult"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

##############################################################

# Step 4 : Visualisation of dataset

print("Visualisation of dataset")

plt.figure(figsize=(7,5))

sns.scatterplot(
    x="StudyHours",
    y="Attendance",
    hue="FinalResult",
    data=df
)

plt.title("StudyHours vs Attendance")
plt.show()

#########################################################

# Step 5 : Split the dataset for training and testing


print("Split the dataset for training and testing")


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.2)

print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)
print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test.shape)

######################################################

# Step 6 : Build the model

print("Build the model")

model=DecisionTreeClassifier(
    criterion="gini",
    max_depth=2,
    random_state=42
)

print("Model successfully created : ",model)

####################################################
    
# Step 7 : Train the model

print("Train the model")

model.fit(X_train,Y_train)

print("model training completed")

####################################################

# Step 8 : Evaluate the model

print("Evaluate the model")

Y_pred=model.predict(X_test)

print("Model evulation(Testing) completed")
print("Y_pred shape :" , Y_pred.shape)

print("Predicated ans :")
print(Y_pred)

print("Actual ans :")
print(Y_test)

#####################################################

# Step 9 :  Evaluate the model performance

print("Evaluate the model performance : ")

accuracy=accuracy_score(Y_pred,Y_test)
print("Accuracy of the model is : ",accuracy*100)
