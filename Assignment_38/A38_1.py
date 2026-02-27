import pandas as pd


##########################################################

Datasetpath="student_performance_ml.csv"

Data=pd.read_csv(Datasetpath)

print("Dataset loaded successfully ")

############################################################

print("First five")

print(Data.head())

###########################################################

print("Last Reacords")

print(Data.tail())

##########################################################

row,col=Data.shape

print("No of columns in Dataset :",col)

print("No of Row in dataset : ",row)

##########################################################

print("List colunms in Dataset ",list(Data.columns))

########################################################

print("Datatype of Colums  : \n",Data.dtypes)
