
from modules.utils import *


def SVMTraining():
    # Get Xtrain
    # Get Y train
    Tick, QuestionMark, Square, Horizontal, Vertical = TrainedData()
    x_train = np.concatenate((Tick, QuestionMark, Square, Horizontal[0], Horizontal[1], Horizontal[2],
                             Horizontal[3], Vertical[0], Vertical[1], Vertical[2], Vertical[3], Vertical[4]), axis=0)
    y_train = np.concatenate((["Tick"]*np.shape(Tick)[0], ["Question"]*np.shape(QuestionMark)[0], ["Square"]*np.shape(Square)[0], ["1_hor"]*np.shape(Horizontal[0])[0], ["2_hor"]*np.shape(Horizontal[1])[0], ["3_hor"]*np.shape(Horizontal[2])[0], ["4_hor"]*np.shape(Horizontal[3])[0]        # ,["5_hor"]*np.shape(Horizontal[4])[0]
                              , ["1_ver"]*np.shape(Vertical[0])[0], ["2_ver"]*np.shape(Vertical[1])[0], ["3_ver"]*np.shape(Vertical[2])[0], ["4_ver"]*np.shape(Vertical[3])[0], ["5_ver"]*np.shape(Vertical[4])[0]
                              ), axis=0)
    model = trainModel(x_train, y_train)
    return model


def trainModel(x_train, y_train):
    model = svm.SVC()
    model.fit(x_train, y_train)
    return model


def TrainedData():
    # Tick##########################################3
    directory = './Data Set/Training Set/Tick'
    Tick = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Tick.append(fd_1)

    # ??##########################################3
    directory = './Data Set/Training Set/QuestionMark'
    QuestionMark = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            # image=cv2.imread(f,1)
            # show_images([image],['asdf'])
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            QuestionMark.append(fd_1)

    # Square##########################################3
    directory = './Data Set/Training Set/Square'
    Square = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            # image=cv2.imread(f,1)
            # show_images([image],['asdf'])
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            Square.append(fd_1)

    # Horizontal##########################################3
    # 1
    directory = './Data Set/Training Set/Horizontal/1'
    Horizontal_1 = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            # image=cv2.imread(f,1)
            # show_images([image],['asdf'])
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            Horizontal_1.append(fd_1)

    # 2
    directory = './Data Set/Training Set/Horizontal/2'
    Horizontal_2 = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            # image=cv2.imread(f,1)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            Horizontal_2.append(fd_1)

    # 3
    directory = './Data Set/Training Set/Horizontal/3'
    Horizontal_3 = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            Horizontal_3.append(fd_1)

    # 4
    directory = './Data Set/Training Set/Horizontal/4'
    Horizontal_4 = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            Horizontal_4.append(fd_1)

    # #5
    # directory='./Data Set/Training Set/Horizontal/5'
    # Horizontal_5=[]
    # #Iterate over files in this Diretory
    # for filename in os.listdir(directory):
    #     f=os.path.join(directory,filename)
    #     if os.path.isfile(f):
    #         print(f)
    #         # image=cv2.imread(f,1)
    #         # show_images([image],['asdf'])
    #         image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
    #         fd_1, hog_image_1=HogFun(image)
    #         Horizontal_5.append(fd_1)

    # Vertical##########################################3
    # 1
    directory = './Data Set/Training Set/Vertical/1'
    Vertical_1 = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            # image=cv2.imread(f,1)
            # show_images([image],['asdf'])
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            Vertical_1.append(fd_1)

    # 2
    directory = './Data Set/Training Set/Vertical/2'
    Vertical_2 = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            # image=cv2.imread(f,1)
            # show_images([image],['asdf'])
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            Vertical_2.append(fd_1)

    # 3
    directory = './Data Set/Training Set/Vertical/3'
    Vertical_3 = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            Vertical_3.append(fd_1)

    # 4
    directory = './Data Set/Training Set/Vertical/4'
    Vertical_4 = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            Vertical_4.append(fd_1)

    # 5
    directory = './Data Set/Training Set/Vertical/5'
    Vertical_5 = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            fd_1, hog_image_1 = HogFun(image)
            Vertical_5.append(fd_1)

    ############################### Numbers#####################
    # #1
    # directory='./Data Set/Training Set/numbers/1/'
    # One=[]
    # #Iterate over files in this Diretory
    # for filename in os.listdir(directory):
    #     f=os.path.join(directory,filename)
    #     if os.path.isfile(f):
    #         print(f)
    #         # image=cv2.imread(f,1)
    #         # show_images([image],['asdf'])
    #         fd_1, hog_image_1=HogFun(f)
    #         One.append(fd_1)

    Vertical = [Vertical_1, Vertical_2, Vertical_3, Vertical_4, Vertical_5]
    Horizontal = [Horizontal_1, Horizontal_2, Horizontal_3, Horizontal_4]

    print(np.shape(Vertical))
    print(np.shape(Horizontal))

    # Horizontal=[Horizontal_1,Horizontal_2,Horizontal_3,Horizontal_4,Horizontal_5]

    return Tick, QuestionMark, Square, Horizontal, Vertical
