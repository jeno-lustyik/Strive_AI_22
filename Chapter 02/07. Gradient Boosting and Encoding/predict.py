from train import model

while True:

    age = int(input("How old are you? \n"))
    child = int(input("How many children do you have? \n"))
    smoke = bool(input("Do you smoke? \n"))
    '''
    Preprocess
    predict
    
    '''
    prediction = model.predict([[age, child, smoke]])
    print(prediction)
