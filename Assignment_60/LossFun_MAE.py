
def MAE(y_true,y_pred):
    
    n = len(y_true)
    total_error = 0

    for i in range(n):
        total_error += abs(y_true[i] - y_pred[i])

    return total_error / n

def main():
    y_true = [11,22,33]
    y_pred = [10,23,34]

    Loss = MAE(y_true,y_pred)
    print("Loss is the ",Loss)

if __name__=="__main__":
    main()