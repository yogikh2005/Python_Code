import pandas as pd


##########################################################

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath)

print("Dataset loaded successfully")

############################################################
row,col=df.shape

print("Total no number of student in dataset : ",row)


############################################################

print("Total no of count student Passed :",df[df["FinalResult"]==1].shape[0])


###########################################################

print("Total no of count student Fail :",df[df["FinalResult"]==0].shape[0])
