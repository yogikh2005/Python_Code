import pandas as pd
import matplotlib.pyplot as plt


########################################################## 

# dataset load

Datasetpath="student_performance_ml.csv"

df=pd.read_csv(Datasetpath)

print("Dataset loaded successfully")


############################################################    

# Relation of Study Hours & Final Result 

plt.figure(figsize=(8,5))

plt.scatter(df["StudyHours"],df["FinalResult"],edgecolors="black",color="skyblue")
plt.xlabel("Study Hours")
plt.ylabel("Final Result")

plt.title("Relation of Study Hours & Final Result : ")
plt.grid(alpha=1)
plt.show()

'''
    Explanation : The study hours is must be need 4 or more so the final result is pass 
                  If the study hours is less than 4 hr so the final result is fail
'''


############################################################ 

# Relation of Attendance& Final Result 

plt.figure(figsize=(8,5))

plt.scatter(df["Attendance"],df["FinalResult"],edgecolors="black",color="skyblue")
plt.xlabel("Attendance")
plt.ylabel("Final Result")

plt.title("Relation of Attendance & Final Result : ")
plt.grid(alpha=0.5)
plt.show()


'''
    Explanation : The Attendance is more than 75 so the final result is pass 
                  If the Attendance is less than 75 hr so the final result is fail
'''