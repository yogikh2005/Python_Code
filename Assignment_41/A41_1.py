import math

def Euclideandistance(P1,P2):
    return math.sqrt(((P1['X']-P2['X'])**2)+((P1['Y']-P2['Y'])**2))

def UserInput():
    New_Point={}
    New_Point['X']=int(input("Enter X cordinate : "))
    New_Point['Y']=int(input("Enter Y cordinate : "))
    return New_Point

def KNNX():

    Data=[{'point ':'A','X':1,'Y':2,'Label':'Red'},
          {'point ':'B','X':2,'Y':3,'Label':'Red'},
          {'point ':'C','X':3,'Y':1,'Label':'Blue'},
          {'point ':'D','X':6,'Y':5,'Label':'Blue'}]     # create dataset
    
    New_Point=UserInput()                                # user input
    
    for p in Data:
        p["distance"]=Euclideandistance(New_Point,p)    # calculate the distance
    
    Sorted_data=sorted(Data,key=lambda x : x['distance'] )     # sort the distance

    K=3                                                 # hyperparameter

    Nerest_data=Sorted_data[:K]                         # find nerest ponits

    voting={}
    for p in Nerest_data:                              # voting
        label=p['Label']
        voting[label]=voting.get(label,0)+1
    
    Predicted_class=max(voting,key=voting.get)        # max key count 
    
    return Predicted_class      # Result

def  main():

    Predicted_class=KNNX()
    print("Predicted Result : ",Predicted_class)  

if __name__=="__main__":
    main()