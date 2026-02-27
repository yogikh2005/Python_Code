import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

########################################################## 

# dataset load

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath)

print("Dataset loaded successfully")


############################################################    

plt.figure(figsize=(8,6))

sns.boxplot(data=df,x="Attendance")

plt.title('Attendance Report')

plt.grid(True)
plt.show()

'''
    Explanation : No any outlayer present in the dataset
'''
