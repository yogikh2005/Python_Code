import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer

#-----------------------------------------------------------------
# Fucntion Name  : TrainFakeNewsmodel
# Description    : It does split X , Y , training 
# Paramaters     : title(str)
# Return         : None
# Date           : 15/04/2026
# Author         : Yogiraj Khaladkar
#------------------------------------------------------------------
def TrainFakeNewsmodel(df):
        
        DisplayInfo("Step 5: Separate independent and dependent variables")
        # split featcures S
        X = X = df['title'].fillna('') + " " + df['text'].fillna('')
        Y = df["label"]

        print("Feactures : ")
        print(X.head())

        print("Label : ")
        print(Y.head())

        print("Shape of X :",X.shape)
        print("Shape of Y :",Y.shape)

        DisplayInfo("Step 6: Split the dataset for testing & training")

        X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
        
        print("Shape of X_train :",X_train.shape)
        print("Shape of X_test :",X_test.shape)
        print("Shape of Y_train :",Y_train.shape)
        print("Shape of Y_test :",Y_test.shape)

        DisplayInfo("Step 7 : Feacture Extraction")

        tfidf = TfidfVectorizer(stop_words='english')
        X_train_tfidf = tfidf.fit_transform(X_train) # Learn and transform
        X_test_tfidf = tfidf.transform(X_test)           

        print("Feacture extraction successfully")

        print("Shape of X_train_tfidf :",X_train_tfidf.shape)
        print("Shape of X_test_tfidf :",X_test_tfidf.shape)

        DisplayInfo("Step 8: Train model")
        
        # base model create
        model_lr = LogisticRegression(max_iter=1000)
        model_dt = DecisionTreeClassifier(random_state=42)

        #soft voting classification

        soft_model = VotingClassifier(
            estimators = [
                ('lr',model_lr),
                ('dt',model_dt)
            ],
            voting = "soft"
        )

        #hard voting classification

        hard_model = VotingClassifier(
            estimators = [
                ('lr',model_lr),
                ('dt',model_dt)
            ],
            voting = "hard"
        )

        soft_model.fit(X_train_tfidf,Y_train)

        hard_model.fit(X_train_tfidf,Y_train)

        print("Model trained successfully \n")

        DisplayInfo("Step 9 : Model Evaluation ")
        DisplayInfo("soft vodting model")

        pred_soft = soft_model.predict(X_test_tfidf)

        acc_soft = accuracy_score(Y_test, pred_soft)

        print("soft voting accuary : ",acc_soft*100)
        
        cm = confusion_matrix(Y_test, pred_soft)

        print("\nconfusion matrix soft voting model : \n",cm)

        print("\nClassification report soft voting model :")
        print(classification_report(Y_test,pred_soft))
        
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title("Confusion Matrix soft voting model")
        plt.show()

        DisplayInfo("hard vodting model")

        pred_hard = hard_model.predict(X_test_tfidf)

        acc_hard = accuracy_score(Y_test,pred_hard)

        print("hard voting accuary : ",acc_hard*100)
        
        cm = confusion_matrix(Y_test,pred_hard)
        
        print("\nconfusion matrix hard vodting model : \n",cm)

        print("\nClassification report hard vodting model :")
        print(classification_report(Y_test,pred_hard))
        
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title("Confusion Matrix hard voting model")
        plt.show()

        DisplayInfo("End")


#-----------------------------------------------------------------
# Fucntion Name  : showData
# Description    : It shows basic information about the dataset
# Paramaters     : Dataset(df)
#                  df -> pandas dataframe object
#                  message -> Heading text to display
# Return         : None
# Date           : 16/04/2026
# Author         : Yogiraj Khaladkar
#------------------------------------------------------------------
def ShowData(df,message):
    DisplayInfo(message)

    print("\n First 5 rows of dataset")
    print(df.head())

    print("\n Shape of dataset")
    print(df.shape)

    print("\n Columns of dataset")
    print(df.columns.tolist())

    print("\n Statistics report")
    print(df.describe())

    print("\n Missing value in dataset")
    print(df.isnull().sum())

    sns.countplot(x='label', data=df)
    plt.title("Distribution of Outcome")
    plt.show()
  
#-----------------------------------------------------------------
# Fucntion Name    : CleanFakeNewsData
# Description      : It does preprocessing
#                    It remove the colunms
# Paramaters       : df -> Pandas dataframe
# Return           : df -> Clean Pandas dataframe
# Date             : 16/04/2026
# Author           : Yogiraj Khaladkar
#------------------------------------------------------------------
def CleanFakeNewsData(df):

    DisplayInfo("Step 3 : Original Data")
    print(df.head())

    # drop the column which value unknown
    df.drop(['subject','date'], axis=1, inplace=True)

    print("\nAfter remove columns dataset")
    print(df.head())
    print(df.shape)

    # label encoding
    df['label'] = df["label"].map({"Fake":0,"True":1})

    DisplayInfo("Step 4 : After EDA Dataset")
    print(df.head())

    return df

#-----------------------------------------------------------------
# Fucntion Name : ConcatDataset
# Description   : It concat 2 dataset in 1 , aslo add label
# Paramaters    : Fdf ,Tdf
#               : Fdf - fake news dataset
#               : Tdf - true news dataset
# Return        : df - dataframe
# Date          : 16/04/2026
# Author        : Yogiraj Khaladkar
#------------------------------------------------------------------
def ConcatDataset(Fdf,Tdf):

    Fdf['label'] = "Fake" 
    Tdf['label'] = "True" 

    df = pd.concat([Fdf,Tdf],ignore_index=True)

    return df

#-----------------------------------------------------------------
# Fucntion Name : DisplayInfo
# Description   : It display the formated title
# Paramaters    : title(str)
# Return        : None
# Date          : 16/04/2026
# Author        : Yogiraj Khaladkar
#------------------------------------------------------------------
def DisplayInfo(title):
    print("\n"+"="*70)
    print(title)
    print("="*70)

#-----------------------------------------------------------------
# Fucntion Name : FakeNewsClassificatioin
# Description   : This is main pipeline controller
#                   It load the datset , show raw data
#                   It proprocess the dataset & train the model
# Paramaters    : Data path of datset file
# Return        : None
# Date          : 16/04/2026
# Author        : Yogiraj Khaladkar
#------------------------------------------------------------------
def FakeNewsClassificatioin(Datapath1,Datapath2):
    
    DisplayInfo("Step 1 : Loading the Dataset")
    
    Fdf = pd.read_csv(Datapath1)
    Tdf = pd.read_csv(Datapath2)
    DisplayInfo("Step 2 : Concat the Dataset")

    df = ConcatDataset(Fdf,Tdf)

    ShowData(df,"Initial dataset")

    df=CleanFakeNewsData(df)

    TrainFakeNewsmodel(df)

#-----------------------------------------------------------------
# Fucntion Name  : main()
# Description    : Starting point of the application
# Paramaters     : NOne
# Return         : None
# Date           : 16/04/2026
# Author         : Yogiraj Khaladkar
#------------------------------------------------------------------
def main():
    FakeNewsClassificatioin("Fake.csv","True.csv")

if __name__ =="__main__":
    main()