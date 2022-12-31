from modules.utils import HogFun
def SymbolValue(cell,SVM):
  #Getting HOG of the Cell

  fd_pred_11, hog_image_pred_11=HogFun(cell)
  # Send cell to the Model
  Symbol=SVM.predict([fd_pred_11])
  print(Symbol)

  return getCorrectNumber(Symbol)


def DigitValue(cell,SVM):
    fd_pred_11, hog_image_pred_11=HogFun(cell)

    # Send cell to the Model
    Digit=SVM.predict([fd_pred_11])
    print(Digit)
    return Digit

#Calculate The Points Coresspondinf to this Symbol
def getCorrectNumber(text):
    if(text == 'Square'):
        return 0
    elif(text == 'Tick'):
        return 5
    elif(text == 'Question'):
        return -1
    elif(text == '1_hor'):
        return 5-1
    elif(text == '2_hor'):
        return 5-2
    elif(text == '3_hor'):
        return 5-3
    elif(text == '4_hor'):
        return 5-4
    elif(text == '5_hor'):
        return 5-5
    elif(text == '1_ver'):
        return 1
    elif(text == '2_ver'):
        return 2
    elif(text == '3_ver'):
        return 3
    elif(text == '4_ver'):
        return 4
    elif(text == '5_ver'):
        return 5
    return -5