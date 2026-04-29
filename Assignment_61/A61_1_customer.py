
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Age , Monthly charges , Tenure , No of complaints , customer support calls
X = [
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
]

# 0 = customer will stay
# 1 = customer will leave
y = [
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
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

# new customer for the test :
new_x = [[46,1450,5,6,9]]
new_x_scaled = scaler.transform(new_x)

prediction = model.predict(new_x_scaled)

if prediction[0] == 1:
    print("Customer will leave")
else:
    print("Customer will stay")