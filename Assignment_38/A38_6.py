import pandas as pd
import matplotlib.pyplot as plt


########################################################## 

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath)

print("Dataset loaded successfully")

# ##########################################################

plt.hist(df["StudyHours"],bins=10,color="skyblue",edgecolor="black")
plt.xlabel("Study Hours")
plt.ylabel("Frequency")

plt.title("Study Hours Distrubution")

plt.grid(alpha=0.3)
plt.show()

'''
    Explaination : the frqauncy of is 2,3,4 
    min frequncy is 2 and max is 4
'''