import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,confusion_matrix,ConfusionMatrixDisplay,classification_report)

########################################################## 

# Step 1 : Load Dataset  

print("Step 1 : Load Dataset")

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath)

print("Dataset loaded successfully")


############################################################    

# Step 2: Data Analysis(EDA)
print("Step 2: Data Analysis(EDA)")

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

print("Step 3 : Decide Independent & Dependet Varible")

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

print("Step 4 : Visualisation of dataset")

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


print("Step 5 : Split the dataset for training and testing")


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.2)

print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)
print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test.shape)

######################################################

# Step 6 : Build the model

print("Step 6 : Build the model")

model=DecisionTreeClassifier(
    criterion="gini",
    random_state=42
)

print("Model successfully created : ",model)

####################################################
    
# Step 7 : Train the model

print("Step 7 : Train the model")

model.fit(X_train,Y_train)

print("model training completed")

####################################################

# Step 8 : Evaluate the model

print("Step 8 : Evaluate the model")

Y_pred=model.predict(X_test)

print("Model evulation(Testing) completed")
print("Y_pred shape :" , Y_pred.shape)

print("Predicated ans :")
print(Y_pred)

print("Actual ans :")
print(Y_test)

#####################################################

# Step 9 :  Evaluate the model performance

print("Step 9 : Evaluate the model performance : ")

accuracy=accuracy_score(Y_pred,Y_test)
print("Testing Accuracy of the model is : ",accuracy*100)

cm=confusion_matrix(Y_pred,Y_test)
print("Confusion matrix : \n",cm)

print("Classification report : ")
print(classification_report(Y_test,Y_pred))

'''
    fail - 0(positive class)
    pass - 1(negative class)
    
    Explanation : 

    True Positive : Student actaul fail , but model predict fail then TP
    
    True Negative : Student actaul pass , but model predict pass then TN

    False Positive : Student actual pass , but model predict fail then FP

    False Negative : Student actual fail , but model predict pass then FN

'''
##########################################################

#  Step 10 : Plot confusion matrix

print("Step 10: Plot confusion matrix")

data=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
data.plot()

plt.title("Confusion matrix Student dataset")
plt.show()


#########################################################

print("Evaluate the model below case")

Y_pred=model.predict([[6,85,66,7,7]])

print("Predicated ans :")
print(Y_pred) # 1

'''
Explanation :
pass = 1
fail = 0
            If we test model below data
             StuStudyHours = 6
             Attendance = 85
             PreviousScore = 66
             AssignmentsCompleted =7
             SleepHours = 7

             finalResult is 1 i.e pass
'''