from sklearn.metrics import classification_report

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

print("Classification report :\n",classification_report(actual,predicted))