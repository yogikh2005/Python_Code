import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,confusion_matrix,ConfusionMatrixDisplay,classification_report)

########################################################## 

# Step 1 : Load Dataset

##########################################################
Border="-"*40

print(Border)
print("Step 1 : Load Dataset")
print(Border)

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath) #  we load the datset from student_performance_ml.csv

print("Dataset loaded successfully")


############################################################    

# Step 2: Data Analysis(EDA)

############################################################ 

print(Border)
print("Step 2: Data Analysis(EDA)")
print(Border)

print("Shape of dataset : ",df.shape)          # we check shape of datset
print("Columns of dataset : ",df.columns)      # check columns info

print("Missing values : ", )
print(df.isnull().sum())  # check the null value present in dataset or not 

print("class ditribution : ")
print(df["FinalResult"].value_counts()) # depentdend varivale class value count

print("Statical report of dataset :")
print(df.describe())

#############################################################

# Step 3 : Decide Independent & Dependet Varible

#############################################################

print(Border)
print("Step 3 : Decide Independent & Dependet Varible")
print(Border)

feacture_cols=[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours" 
]                                       # decide the Independent varible

X=df[feacture_cols] 
Y=df["FinalResult"]   # decide the Dependet varible

print("X shape : ",X.shape)         # check shape of Independent varible
print("Y shape : ",Y.shape)        # check shape of Dependet varible

##############################################################

# Step 4 : Visualisation of dataset

print(Border)
print("Step 4 : Visualisation of dataset")
print(Border)

plt.figure(figsize=(7,5))

sns.scatterplot(
    x="StudyHours",
    y="Attendance",
    hue="FinalResult",
    data=df
)                                               # plot the scatterplot for studyhours vs Attendance with Finalresult

plt.title("StudyHours vs Attendance")
plt.show()

#########################################################

# Step 5 : Split the dataset for training and testing

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.2)  # split the datset in  X_train,X_test,Y_train,Y_test , splait data with 80:20
                                                                                    # random_state for the shuffel dataset
print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)
print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test.shape)

######################################################

# Step 6 : Build the model

print(Border)
print("Step 6 : Build the model")
print(Border)

model=DecisionTreeClassifier(               # create the model obj with max_depth=2,we use DecisionTreeClassifier
                                            # which supriviwed with classfication algo
    criterion="gini",
    max_depth=2,
    random_state=42
)
                                             
print("Model successfully created : ",model)

####################################################
    
# Step 7 : Train the model

print(Border)
print("Step 7 : Train the model")
print(Border)

model.fit(X_train,Y_train)                         # train the model

print("model training completed")

####################################################

# Step 8 : Evaluate the model

print(Border)
print("Step 8 : Evaluate the model")
print(Border)

Y_pred=model.predict(X_test)                                # test the model

print("Model evulation(Testing) completed")
print("Y_pred shape :" , Y_pred.shape)                      # displat shape of Y_pred

print("Predicated ans :")
print(Y_pred)

print("Actual ans :")
print(Y_test)

#####################################################

# Step 9 :  Evaluate the model performance

print(Border)
print("Step 9 : Evaluate the model performance : ")
print(Border)

accuracy=accuracy_score(Y_pred,Y_test)                          # calculate testing accuracy of the train model
print("Testing Accuracy of the model is : ",accuracy*100)       # display in percenatge

cm=confusion_matrix(Y_pred,Y_test)                             # display the confusion matrix of Y_pred & Y_test 
print("Confusion matrix : \n",cm)

print("Classification report : ")
print(classification_report(Y_test,Y_pred))      # display the testing report
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

print(Border)
print("Step 10: Plot confusion matrix")
print(Border)

data=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)  # plot confusion matrix 
data.plot()

plt.title("Confusion matrix Student dataset")
plt.show()


print(Border)