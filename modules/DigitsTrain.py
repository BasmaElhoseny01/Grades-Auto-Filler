from modules.utils import *

from sklearn.neighbors import KNeighborsClassifier


def DigitTraining():

    One, Two, Three, Four, Five, Six, Seven, Eight, Nine = TrainedNumbers()
    x_train = np.concatenate(
        (One, Two, Three, Four, Five, Six, Seven, Eight, Nine), axis=0)
    y_train = np.concatenate(([1]*np.shape(One)[0], [2]*np.shape(Two)[0], [3]*np.shape(Three)[0], [4]*np.shape(Four)[0], [5]*np.shape(Five)[0], [6]*np.shape(Six)[0], [7]*np.shape(Seven)[0], [8]*np.shape(Eight)[0], [9]*np.shape(Nine)[0]
                              ), axis=0)

    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(x_train, y_train)
    # Digitsmodel = svm.SVC()
    # Digitsmodel.fit(x_train,y_train)
    return neigh


def TrainedNumbers():
    # Zero##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/0'
    Zero = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Zero.append(fd_1)

    # One##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/1'
    One = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            One.append(fd_1)


# Two##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/2'
    Two = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Two.append(fd_1)


# Three##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/3'
    Three = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Three.append(fd_1)

# Four##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/4'
    Four = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Four.append(fd_1)

    # Five##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/5'
    Five = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Five.append(fd_1)

# Six##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/6'
    Six = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Six.append(fd_1)

    # Seven##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/7'
    Seven = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Seven.append(fd_1)

    # Eight##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/8'
    Eight = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Eight.append(fd_1)
    # Nine##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/9'
    Nine = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Nine.append(fd_1)
    return One, Two, Three, Four, Five, Six, Seven, Eight, Nine


def CodeTraining():

    One, Two, Three, Four, Five, Six, Seven, Eight, Nine = TrainedCodes()
    x_train = np.concatenate((One, Two, Three,
                              # Four,
                              Five, Six, Seven, Eight
                             # ,Nine
                              ), axis=0)

    y_train = np.concatenate(([1]*np.shape(One)[0], [2]*np.shape(Two)[0], [3]*np.shape(Three)[0]                              # ,[4]*np.shape(Four)[0]
                              , [5]*np.shape(Five)[0], [6]*np.shape(Six)[0], [7]*np.shape(Seven)[0], [8]*np.shape(Eight)[0]
                              # ,[9]*np.shape(Nine)[0]
                              ), axis=0)

    Digitsmodel = svm.SVC()
    Digitsmodel.fit(x_train, y_train)
    return Digitsmodel


def TrainedCodes():
    # Zero##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/Code/0'
    Zero = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Zero.append(fd_1)

    # One##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/Code/1'
    One = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            One.append(fd_1)


# Two##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/Code/2'
    Two = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Two.append(fd_1)


# Three##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/Code/3'
    Three = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Three.append(fd_1)

# Four##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/Code/4'
    Four = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Four.append(fd_1)

    # Five##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/Code/5'
    Five = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Five.append(fd_1)

# Six##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/Code/6'
    Six = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Six.append(fd_1)

    # Seven##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/Code/7'
    Seven = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Seven.append(fd_1)

    # Eight##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/Code/8'
    Eight = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Eight.append(fd_1)
    # Nine##########################################3
    directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/Code/9'
    Nine = []
    # Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1 = HogFun(image)
            Nine.append(fd_1)
    return One, Two, Three, Four, Five, Six, Seven, Eight, Nine
