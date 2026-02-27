import pandas as pd
import matplotlib.pyplot as plt


########################################################## 

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath)

print("Dataset loaded successfully")

############################################################   1


print("Count FinalResult : ", df["FinalResult"].value_counts())


############################################################  2

counts = df["FinalResult"].value_counts()
percentages = (counts / counts.sum()) * 100
print(percentages)

''' The dataset is imbalenced the ratio of label is 1.5 so imbalenced
     The ratio is 1:1 is balenced
                  Ratio <= 1.5 is mid imbalenced
                  Ratio > 2 is clear imbalenced
                  Ratio > 5 is strong imbalenced

                  
     '''
