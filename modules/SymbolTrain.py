from modules.utils import *


def SVMTraining():
    return


def trainModel(x_train,y_train):
    model = svm.SVC()
    model.fit(x_train,y_train)
    return model



def getCorrectNumber(test,text):
    if(text == 'Square'):
        return -2
    elif(test == 'Tick'):
        return -3
    elif(test == 'dash'):
        return -4
    elif(test == 'Question'):
        return -1
    elif(test == '1_hor'):
        return 5-1
    elif(test == '2_hor'):
        return 5-2
    elif(test == '3_hor'):
        return 5-3
    elif(test == '4_hor'):
        return 5-4
    elif(test == '5_hor'):
        return 5-5
    elif(test == '1_ver'):
        return 1
    elif(test == '2_ver'):
        return 2
    elif(test == '3_ver'):
        return 3
    elif(test == '4_ver'):
        return 4
    elif(test == '5_ver'):
        return 5
    return -5


def HogFun(img_1):
    resized_img_1 = resize(img_1, (128*4, 64*4))
    # plt.axis("off")
    # plt.imshow(resized_img)
    # print(resized_img.shape)


    #creating hog features
    fd_1, hog_image_1 = hog(resized_img_1, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2, 2), visualize=True, multichannel=False)
    show_images([img_1,resized_img_1,hog_image_1],["Gray","Resized","hog_image"])
    # Fd Faeture
#     print(np.shape(fd_1))
    return fd_1,hog_image_1

    


def TrainedData():
    Tick=[]
    fd_1, hog_image_1=HogFun('./Data set/Training Set/Tick/710.jpg')
    Tick.append(fd_1)

    fd_2, hog_image_2=HogFun('./Data set/Training Set/Tick/810.jpg')
    Tick.append(fd_2)

    fd_3, hog_image_3=HogFun('./Data set/Training Set/Tick/011.jpg')
    Tick.append(fd_3)

    fd_4, hog_image_4=HogFun('./Data set/Training Set/Tick/110.jpg')
    Tick.append(fd_4)

    fd_5, hog_image_5=HogFun('./Data set/Training Set/Tick/210.jpg')
    Tick.append(fd_5)

    fd_6, hog_image_6=HogFun('./Data set/Training Set/Tick/310.jpg')
    Tick.append(fd_6)

    fd_7, hog_image_7=HogFun('./Data set/Training Set/Tick/510.jpg')
    Tick.append(fd_7)

    fd_8, hog_image_8=HogFun('./Data set/Training Set/Tick/610.jpg')
    Tick.append(fd_8)



    QuestionMark=[]
    fd_1, hog_image_1=HogFun('./Data set/Training Set/Question/310.jpg')
    QuestionMark.append(fd_1)

    fd_2, hog_image_2=HogFun('./Data set/Training Set/Question/1210.jpg')
    QuestionMark.append(fd_2)

    fd_3, hog_image_3=HogFun('./Data set/Training Set/Question/1310.jpg')
    QuestionMark.append(fd_3)

    fd_4, hog_image_4=HogFun('./Data set/Training Set/Question/1710.jpg')
    QuestionMark.append(fd_4)


    fd_5, hog_image_5=HogFun('./Data set/Training Set/Question/120.jpg')
    QuestionMark.append(fd_5)

    fd_6, hog_image_6=HogFun('./Data set/Training Set/Question/220.jpg')
    QuestionMark.append(fd_6)


    fd_7, hog_image_7=HogFun('./Data set/Training Set/Question/320.jpg')
    QuestionMark.append(fd_7)

    fd_8, hog_image_8=HogFun('./Data set/Training Set/Question/420.jpg')
    QuestionMark.append(fd_8)


    fd_9, hog_image_9=HogFun('./Data set/Training Set/Question/520.jpg')
    QuestionMark.append(fd_9)



    Square=[]
    fd_1, hog_image_1=HogFun('./Data set/Training Set/Square/210.jpg')
    Square.append(fd_1)

    fd_2, hog_image_2=HogFun('./Data set/Training Set/Square/410.jpg')
    Square.append(fd_2)

    fd_3, hog_image_3=HogFun('./Data set/Training Set/Square/1410.jpg')
    Square.append(fd_3)

    fd_4, hog_image_4=HogFun('./Data set/Training Set/Square/1510.jpg')
    Square.append(fd_4)


    fd_5, hog_image_5=HogFun('./Data set/Training Set/Square/120.jpg')
    Square.append(fd_5)



    fd_6, hog_image_6=HogFun('./Data set/Training Set/Square/220.jpg')
    Square.append(fd_6)


    fd_7, hog_image_7=HogFun('./Data set/Training Set/Square/420.jpg')
    Square.append(fd_7)


    fd_8, hog_image_8=HogFun('./Data set/Training Set/Square/620.jpg')
    Square.append(fd_8)


    fd_9, hog_image_9=HogFun('./Data set/Training Set/Square/820.jpg')
    Square.append(fd_9)


    Horizontal=[]
    fd_1, hog_image_1=HogFun('./Data set/Training Set/Horizontal/110.jpg')
    Horizontal.append(fd_1)

    fd_2, hog_image_2=HogFun('./Data set/Training Set/Horizontal/210.jpg')
    Horizontal.append(fd_2)

    fd_3, hog_image_3=HogFun('./Data set/Training Set/Horizontal/300.jpg')
    Horizontal.append(fd_3)

    fd_4, hog_image_4=HogFun('./Data set/Training Set/Horizontal/510.jpg')
    Horizontal.append(fd_4)


    fd_5, hog_image_5=HogFun('./Data set/Training Set/Horizontal/630.jpg')
    Horizontal.append(fd_5)



    fd_6, hog_image_6=HogFun('./Data set/Training Set/Horizontal/631.jpg')
    Horizontal.append(fd_6)


    fd_7, hog_image_7=HogFun('./Data set/Training Set/Horizontal/810.jpg')
    Horizontal.append(fd_7)


    fd_8, hog_image_8=HogFun('./Data set/Training Set/Horizontal/922.jpg')
    Horizontal.append(fd_8)


    fd_9, hog_image_9=HogFun('./Data set/Training Set/Horizontal/1100.jpg')
    Horizontal.append(fd_9)

    fd_10, hog_image_10=HogFun('./Data set/Training Set/Horizontal/1110.jpg')
    Horizontal.append(fd_10)

    fd_11, hog_image_11=HogFun('./Data set/Training Set/Horizontal/1131.jpg')
    Horizontal.append(fd_11)

    fd_12, hog_image_12=HogFun('./Data set/Training Set/Horizontal/1210.jpg')
    Horizontal.append(fd_12)

    fd_13, hog_image_13=HogFun('./Data set/Training Set/Horizontal/5101.jpg')
    Horizontal.append(fd_13)


    Vertical=[]
    fd_1, hog_image_1=HogFun('./Data set/Training Set/Vertical/010.jpg')
    Vertical.append(fd_1)

    fd_2, hog_image_2=HogFun('./Data set/Training Set/Vertical/011.jpg')
    Vertical.append(fd_2)

    fd_3, hog_image_3=HogFun('./Data set/Training Set/Vertical/12ff.jpg')
    Vertical.append(fd_3)

    fd_4, hog_image_4=HogFun('./Data set/Training Set/Vertical/0101.jpg')
    Vertical.append(fd_4)

    fd_5, hog_image_5=HogFun('./Data set/Training Set/Vertical/110.jpg')
    Vertical.append(fd_5)

    fd_6, hog_image_6=HogFun('./Data set/Training Set/Vertical/310.jpg')
    Vertical.append(fd_6)

    fd_7, hog_image_7=HogFun('./Data set/Training Set/Vertical/333.jpg')
    Vertical.append(fd_7)

    fd_8, hog_image_8=HogFun('./Data set/Training Set/Vertical/400.jpg')
    Vertical.append(fd_8)

    fd_9, hog_image_9=HogFun('./Data set/Training Set/Vertical/400d.jpg')
    Vertical.append(fd_9)

    fd_10, hog_image_10=HogFun('./Data set/Training Set/Vertical/410.jpg')
    Vertical.append(fd_10)

    fd_11, hog_image_11=HogFun('./Data set/Training Set/Vertical/610.jpg')
    Vertical.append(fd_11)

    fd_12, hog_image_12=HogFun('./Data set/Training Set/Vertical/910.jpg')
    Vertical.append(fd_12)

    fd_13, hog_image_13=HogFun('./Data set/Training Set/Vertical/1010.jpg')
    Vertical.append(fd_13)

    fd_14, hog_image_14=HogFun('./Data set/Training Set/Vertical/1110.jpg')
    Vertical.append(fd_14)

    fd_15, hog_image_15=HogFun('./Data set/Training Set/Vertical/1200.jpg')
    Vertical.append(fd_15)

    fd_16, hog_image_16=HogFun('./Data set/Training Set/Vertical/1234.jpg')
    Vertical.append(fd_16)

    fd_17, hog_image_17=HogFun('./Data set/Training Set/Vertical/1510.jpg')
    Vertical.append(fd_17)

    fd_18, hog_image_18=HogFun('./Data set/Training Set/Vertical/1610.jpg')
    Vertical.append(fd_18)

    fd_19, hog_image_19=HogFun('./Data set/Training Set/Vertical/12132.jpg')
    Vertical.append(fd_19)

    fd_20, hog_image_20=HogFun('./Data set/Training Set/Vertical/16110.jpg')
    Vertical.append(fd_20)

    fd_21, hog_image_21=HogFun('./Data set/Training Set/Vertical/161210.jpg')
    Vertical.append(fd_21)

    fd_22, hog_image_22=HogFun('./Data set/Training Set/Vertical/1234567.jpg')
    Vertical.append(fd_22)

    fd_23, hog_image_23=HogFun('./Data set/Training Set/Vertical/asa.jpg')
    Vertical.append(fd_23)


    return Tick,QuestionMark,Square,Horizontal,Vertical