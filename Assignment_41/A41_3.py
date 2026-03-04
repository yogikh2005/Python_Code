import math

def Euclideandistance(P1,P2):
    return math.sqrt(((P1['StudyHours']-P2['StudyHours'])**2)+((P1['Attendance']-P2['Attendance'])**2))

def UserInput():
    New_Point={}
    New_Point['StudyHours']=int(input("Enter Study Hours : "))
    New_Point['Attendance']=int(input("Enter Attendance : "))
    return New_Point

def KNNX():

    Data=[{'StudyHours':2,'Attendance':60,'Result':'Fail'},
          {'StudyHours':5,'Attendance':80,'Result':'Pass'},
          {'StudyHours':6,'Attendance':85,'Result':'Pass'},
          {'StudyHours':1,'Attendance':50,'Result':'Fail'},]     # create dataset
    
    New_Point=UserInput()                                # user input
    
    for p in Data:
        p["distance"]=Euclideandistance(New_Point,p)    # calculate the distance
    
    Sorted_data=sorted(Data,key=lambda x : x['distance'] )     # sort the distance

    K=3                                               # hyperparameter

    Nerest_data=Sorted_data[:K]                         # find nerest ponits
        
    voting={}
    for p in Nerest_data:                              # voting
        label=p['Result']
        voting[label]=voting.get(label,0)+1
    
    Predicted_class=max(voting,key=voting.get)        # max key count 
    
    return Predicted_class      # Result

def  main():

    Predicted_class=KNNX()
    print("Predicted Result : ",Predicted_class)  
    
if __name__=="__main__":
    main()

