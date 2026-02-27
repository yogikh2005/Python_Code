import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

########################################################## 

# dataset load

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath)

print("Dataset loaded successfully")


############################################################    

# Relation of Study Hours & Final Result 
jitter = np.random.normal(0, 0.02, size=len(df))
plt.figure(figsize=(8,5))

plt.scatter(df["AssignmentsCompleted"],df["FinalResult"]+jitter,edgecolors="black",color="skyblue")
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result(Pass =1 ,Fail=0)")

plt.title("Relation of Assignments Completed & Final Result : ")
plt.grid(alpha=1)
plt.show()

'''
    Explanation : The Assignments Completed is 5 or  more so the final result is pass 
                  If The Assignments Completed is less tah or equal 5 so the final result is fail
'''

