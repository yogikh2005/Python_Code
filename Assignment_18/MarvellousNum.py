def ChkPrime(No):
    flag=False
    for i in range(2,((No//2)+1)):
        if No%i==0:
            flag=True
            break
    return flag
