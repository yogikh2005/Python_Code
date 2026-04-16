import pandas  as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    
    #----------------------------------------------
    # Step 1 : load the dataset
    #-----------------------------------------------
    print("Step 1 : load the datset")
    df =  pd.read_csv("student-mat.csv",sep=";")

    print("First few records")
    print(df.head())

    print("Shape of dataset : ",df.shape)

    print("Missing value :")
    print(df.isnull().sum())

    #----------------------------------------------
    # Step 2 : select the fectures 
    #-----------------------------------------------
    print("Step 2 : select the feactures")

    X=df[["G1","G2","G3","studytime","failures","absences"]]

    print("Selected feature : ")
    print(X.head())

    print("Shape of X : ",X.shape)


    #----------------------------------------------
    # Step 3 : sclae the data
    #-----------------------------------------------
    print("Step 3 : scale the date ")

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("Data after scalling : ")
    print(X_scaled[:5])

    #----------------------------------------------
    # Step 4 : use elbow method
    #-----------------------------------------------
    print("Step 4 : use elbow method ")

    WCSS = []
    for i in range(1,11):
        model =  KMeans(n_clusters = i ,random_state = 42 , n_init = 10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11),WCSS,marker ='o')
    plt.xlabel("Number of cluster")
    plt.ylabel("WCSS")
    plt.title("Elbow method")
    plt.grid(True)
    plt.show()

    #----------------------------------------------
    # Step 5: train the model
    #-----------------------------------------------
    print("Step 5 : train the model")
    model =  KMeans(n_clusters = 3 ,random_state = 42 , n_init = 10)
    cluster = model.fit_predict(X_scaled)

    df["cluster"] = cluster

    print("Dataset with cluster : \n")
    print(df.head(30))

if __name__ =="__main__":
    main()