import pandas as pd
import matplotlib.pyplot as plt


########################################################## 

# dataset load

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath)

print("Dataset loaded successfully")


############################################################    

# Relation of Study Hours & Final Result 

pass_students = df[df['FinalResult'] == 1]
fail_students = df[df['FinalResult'] == 0]

# Create scatter plot
plt.figure(figsize=(8,6))

plt.scatter(pass_students['StudyHours'], 
            pass_students['PreviousScore'], 
            color='green', 
            label='Pass')

plt.scatter(fail_students['StudyHours'], 
            fail_students['PreviousScore'], 
            color='red', 
            label='Fail')

plt.xlabel('Study Hours')
plt.ylabel('Previous Score')
plt.title('Study Hours vs Previous Score')
plt.legend()
plt.grid(True)

plt.show()

'''
    Explanation : The study hours is must be need 4 or more and privious score is grater than 55 then final result is pass 
                  The study hours is must be need 4 or more and privious score is less than 55 then final result is pass 
'''
