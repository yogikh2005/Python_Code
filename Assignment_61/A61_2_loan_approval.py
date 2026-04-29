
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Income , Credict score , Loan Amount , Exsting EMI , Employment Status 
X = [
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
]

# 0 = Not Stable
# 1 = Stable
y = [
    0, 1, 1, 0, 1,
    1, 0, 1, 0, 1
]

# split the dataset

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# stadard scaling 
scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

# model creation

model = MLPClassifier(
    hidden_layer_sizes=(2,2),
    activation='relu',
    solver='lbfgs',
    max_iter=50
)

# model train 
model.fit(x_train_scaled,y_train)

# model predecition
y_pred = model.predict(x_test_scaled)

# model evaluation

print("Model accuraccy : ",accuracy_score(y_test,y_pred))
print("Classification report :\n",classification_report(y_test,y_pred))
print("confusion matrix :\n",confusion_matrix(y_test,y_pred))

# new employee for the test :
new_x = [[55000,720,400000,10000,1]]
new_x_scaled = scaler.transform(new_x)

prediction = model.predict(new_x_scaled)

if prediction[0] == 1:
    print("Predication : Loan Approved")
else:
    print("Predication : Loan Not Approved")