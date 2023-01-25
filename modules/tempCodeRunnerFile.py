# Train Classifier on the Digits from 0-9
# def DigitTraining():

#     One, Two, Three, Four, Five, Six, Seven, Eight, Nine = TrainedNumbers()
#     x_train = np.concatenate(
#         (One, Two, Three, Four, Five, Six, Seven, Eight, Nine), axis=0)
#     y_train = np.concatenate(([1]*np.shape(One)[0], [2]*np.shape(Two)[0], [3]*np.shape(Three)[0], [4]*np.shape(Four)[0], [5]*np.shape(Five)[0], [6]*np.shape(Six)[0], [7]*np.shape(Seven)[0], [8]*np.shape(Eight)[0], [9]*np.shape(Nine)[0]
#                               ), axis=0)

#     neigh = KNeighborsClassifier(n_neighbors=3)
#     neigh.fit(x_train, y_train)
#     # Digitsmodel = svm.SVC()
#     # Digitsmodel.fit(x_train,y_train)
#     return neigh


# def TrainedNumbers():
#     # Zero##########################################3
#     absolute_path = os.path.dirname(__file__)
#     relative_path = "Data set/Training Set/numbers/0"
#     directory = os.path.join(absolute_path, relative_path)
#     # directory = '/home/mustafa_hamzawy/Desktop/final 2/Grades-Auto-Filler/Data set/Training Set/numbers/0'
#     Zero = []
#     # Iterate over files in this Diretory
#     for filename in os.listdir(directory):
#         f = os.path.join(directory, filename)
#         if os.path.isfile(f):
#             print(f)
#             image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
#             # show_images([image],['asdf'])
#             fd_1, hog_image_1 = HogFun(image)
#             Zero.ap