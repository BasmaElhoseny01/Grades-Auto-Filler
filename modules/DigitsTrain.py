# from sklearn.datasets import fetch_openml, load_digits
# import matplotlib
# import matplotlib.pyplot as plt

from modules.utils import *

# def DigitKNN():
#     mnist = fetch_openml("mnist_784") #load_digits()

#     # checking the column names and preprocessing target values in standard format
#     mnist.keys()
#     mnist.target = mnist.target.astype(np.int8)
#     #Determining independent and dependent variable and finding the shape
#     x = np.array(mnist.data)
#     y = np.array(mnist.target)
#     x.shape, y.shape
#     #output ((70000, 784), (70000,))
#     # shuffling the values of x and y
#     si = np.random.permutation(x.shape[0])
#     x = x[si]
#     y = y[si]



#     some_digit = x[12]
#     some_digit_image = some_digit.reshape(28, 28)
#     plt.imshow(some_digit_image, cmap=matplotlib.cm.binary)
#     plt.axis("off")
#     plt.show()


#     #slicing data
#     trainx = x[:2000]
#     trainy = y[:2000]
#     #Inserting trainy in trainx
#     train = np.insert(trainx, 784, trainy, axis = 1)
#     prediction = predict_classification(train, train[1244], 4)
#     prediction
#     #Output 8.0


# def predict_classification(train, test_row, num):
#     Neighbors = Get_Neighbors(train, test_row, num)
#     Classes = []
#     for i in Neighbors:
#         Classes.append(i[-1])
#     prediction = max(Classes, key= Classes.count)
#     return prediction


# def Get_Neighbors(train, test_row, num):
    
#     distance = list() # []
#     data = []
#     for i in train:
#        dist = Euclidean_distance(test_row, i)
#        distance.append(dist)
#        data.append(i)

#     distance = np.array(distance)
#     data = np.array(data)
#     #Finding the index in ascending order
#     index_dist = distance.argsort()
#     #Arranging data according to index
#     data = data[index_dist]
#     #slicing k value from number of data
#     neighbors = data[:num]
    
#     return neighbors

# def Euclidean_distance(row1, row2):
#     distance = 0
#     for i in range(len(row1)-1):
#         distance += (row1[i] — row2[i])**2
#     return math.sqrt(distance)

def DigitTraining():

    One,Two,Three,Four,Five,Six,Seven,Eight,Nine=TrainedNumbers()
    x_train=np.concatenate((One,Two,Three,Four,Five,Six,Seven,Eight,Nine), axis=0)
    y_train=np.concatenate(([1]*np.shape(One)[0]
    ,[2]*np.shape(Two)[0]
    ,[3]*np.shape(Three)[0]
    ,[4]*np.shape(Four)[0]
    ,[5]*np.shape(Five)[0]
    ,[6]*np.shape(Six)[0]
    ,[7]*np.shape(Seven)[0]
    ,[8]*np.shape(Eight)[0]
    ,[9]*np.shape(Nine)[0]
    ), axis=0)

    Digitsmodel = svm.SVC()
    Digitsmodel.fit(x_train,y_train)
    return Digitsmodel

    
def TrainedNumbers():
    #######################################################Zero##########################################3
    directory='./Data Set/Training Set/numbers/0'
    Zero=[]
    #Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f):
            print(f)
            image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1=HogFun(image)
            Zero.append(fd_1)


    #######################################################One##########################################3
    directory='./Data Set/Training Set/numbers/1'
    One=[]
    #Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f):
            print(f)
            image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1=HogFun(image)
            One.append(fd_1)



#######################################################Two##########################################3
    directory='./Data Set/Training Set/numbers/2'
    Two=[]
    #Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f):
            print(f)
            image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1=HogFun(image)
            Two.append(fd_1)



#######################################################Three##########################################3
    directory='./Data Set/Training Set/numbers/3'
    Three=[]
    #Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f):
            print(f)
            image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1=HogFun(image)
            Three.append(fd_1)

#######################################################Four##########################################3
    directory='./Data Set/Training Set/numbers/4'
    Four=[]
    #Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f):
            print(f)
            image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1=HogFun(image)
            Four.append(fd_1)

    #######################################################Five##########################################3
    directory='./Data Set/Training Set/numbers/5'
    Five=[]
    #Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f):
            print(f)
            image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1=HogFun(image)
            Five.append(fd_1)

#######################################################Six##########################################3
    directory='./Data Set/Training Set/numbers/6'
    Six=[]
    #Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f):
            print(f)
            image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1=HogFun(image)
            Six.append(fd_1)

    #######################################################Seven##########################################3
    directory='./Data Set/Training Set/numbers/7'
    Seven=[]
    #Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f):
            print(f)
            image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1=HogFun(image)
            Seven.append(fd_1)


    #######################################################Eight##########################################3
    directory='./Data Set/Training Set/numbers/8'
    Eight=[]
    #Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f):
            print(f)
            image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1=HogFun(image)
            Eight.append(fd_1)
    #######################################################Nine##########################################3
    directory='./Data Set/Training Set/numbers/9'
    Nine=[]
    #Iterate over files in this Diretory
    for filename in os.listdir(directory):
        f=os.path.join(directory,filename)
        if os.path.isfile(f):
            print(f)
            image=cv2.imread(f, cv2.IMREAD_GRAYSCALE)
            # show_images([image],['asdf'])
            fd_1, hog_image_1=HogFun(image)
            Nine.append(fd_1)
    return One,Two,Three,Four,Five,Six,Seven,Eight,Nine