import pandas as pd


##########################################################

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath)

print("Dataset loaded successfully")

############################################################
print("Average StudyHours : ",df["StudyHours"].mean())


############################################################

print("Average Attendance : ",df["Attendance"].mean())


###########################################################

print("Maximum PreviousScore : ",df["PreviousScore"].max())

##########################################################

print("Minimum SleepHours : ",df["SleepHours"].min())
