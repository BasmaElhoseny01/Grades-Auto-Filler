from modules.utils import *
# from modules.PageExtractor import *
#from PageExtractor import *


def ExtractPaper(ImagePath):
    # =========================================Read Image==========================================

    # Reading image BGR
    img_BGR=cv2.imread(ImagePath, cv2.IMREAD_COLOR)

    # Converting BGR color to RGB color format
    img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

    # Converting image to gary scale (0-255)
    img_gray = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
    # print("max",np.max(img_gray))

    # Show Images
    # show_images([img_RGB,img_gray],titles=['RGB','Gray'])

    # =========================================PreProcessing==========================================

    # Guassian Filter on the image to remove noise
    # Gray Scale image,Kernel size(postive and odd),Sigma
    Blurred_image_Guassian=cv2.GaussianBlur(img_gray,(5,5),1)

    # Median Filter to remove Salt and Pepper
    # non-linear Filtering technique => takes median of all pixels in the kernel and replaces the central element with this median value =>To reduce salt and pepper
    # Image-Kernel size
    Blurred_image_Median=cv2.medianBlur(img_gray, 5)

    # show_images([img_gray,Blurred_image_Guassian,Blurred_image_Median],titles=['Gray Scale image','step2:Guassian filter','step3:MedianFilter'])

    # =========================================Edge Detection==========================================
    # Edge Dectrion using Canny (Optimal Edge Detector)
    # Steps of Algorithm
    #1.Guassian Smoothing:
    #2.Sobel: to get first derivative in horizontal direction (Gx) and vertical direction (Gy) => the n it finds find edge gradient and direction for each pixel as follows:
    # Edge_Gradient(G)=root(G2x+G2y),Angle(θ)=tan−1(Gy/Gx)
    #3.Non Maxima Supression: to get rid of Double response of edges [Thin Edges] ie pixel is checked if it is a local maximum in its neighborhood in the direction of gradient. 
    #4.Hysteresis Thresholding:decides which are all edges are really edges and which are not Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity.
    # Image(GrayScale),MinThreshold,MaxThreshold for hystresis Thresholding
    Edged_Image=cv2.Canny(Blurred_image_Median,180,255)

    #Aplly Closing (Dialtion - Errsoion) [Poor Results => we need more Dialation the Errosion]
    # =>closing small holes inside the foreground objects, or small black points on the object.
    # Closed_img = cv.morphologyEx(Edged_Image, cv.MORPH_CLOSE, (7,7))
    # show_images([Edged_Image,Closed_img],titles=['Canny Edged Image(Disconnected Edges :( )','After Closing'])

    kernel = np.ones((5,5),np.uint8)
    Dilated_img = cv2.dilate(Edged_Image,kernel,iterations=2)
    Erroded_img = cv2.erode(Dilated_img,kernel,iterations=1)
    # show_images([Dilated_img,Erroded_img],titles=['Dalated_img','Erroded_img'])

    # =========================================Getting Contours==========================================
    # Finding All Contours
    # OpenCV has findContour() function that helps in extracting the contours from the image. It works best on binary images
    # so we should first apply thresholding techniques, Sobel edges, etc. Already Done Above :D
    #WARNING : Use a copy of the image =>since findContours alters the image
    contrours_img=np.copy(Erroded_img)
    # i/p:image,contour retrieval mode,contour approximation method 
    # Does it store all the coordinates ? That is specified by this contour approximation method.
    # =>If you pass cv.CHAIN_APPROX_NONE, all the boundary points are stored. But actually do we need all the points? For eg, you found the contour of a straight line. 
    # =>Do you need all the points on the line to represent that line? No, we need just two end points of that line. 
    # =>This is what cv.CHAIN_APPROX_SIMPLE does.It removes all redundant points and compresses the contour, thereby saving memory.
    # o/p: Contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
    contours, hierarchy=cv2.findContours(contrours_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    # Drawing Contours
    # i/p:image(So we can draw on it the contours),contours list, index of contours (useful when drawing individual contour. To draw all contours, pass -1) 
    # ,color, thickness
    #Draw Contours on the Original Image (Gray Image)
    image_with_contours=np.copy(img_RGB)
    cv2.drawContours(image_with_contours,contours, -1, (0, 255, 0), 20)
    # show_images([image_with_contours],titles=['Contours'])


    # Getting Biggest Contour
    biggest_contour = np.array([])
    max_area = 0
    j=0
    for i in contours:
        area = cv2.contourArea(i)
        #Approximate The Contour to the nearest Poly 
        peri = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.02 * peri, True)

        # print(j,"Area:",area)
        # print(j,"Approximate",len(approx))
        # If Graeter tahn Max Aea and it is a rectangle
        if area > max_area and len(approx) == 4:
            # print("Inside if",j)
            max_area = area
            biggest_contour=approx
        j=j+1
    
    print("Max_Area",max_area)
    print("Biggest Rectangle",biggest_contour)
    print("Height*Width",img_gray.shape[0]*img_gray.shape[1])


    # Reordering Contours Points
    # print("BeforeOrder",biggest_contour)
    biggestContour= reorderPoints(biggest_contour)
    # print("AfterOrder",biggestContour)

    biggest_contour_img=np.copy(img_RGB)
    # Drawing Biggest Contour
    cv2.drawContours(biggest_contour_img, biggestContour, -1, (0, 255, 0), 20) #Will Draw only 4 points
    biggest_contour_img = drawRectangle(biggest_contour_img,biggestContour,20)
    # show_images([biggest_contour_img],titles=['Biggest Contour'])


    # Prespectve
    # Get image dimensions
    imgHeight = img_gray.shape[0]
    imgWidth = img_gray.shape[1]
    pts1 = np.float32(biggestContour)#SRC
    pts2 = np.float32([[0, 0],[imgWidth, 0], [0, imgHeight],[imgWidth, imgHeight]])#DST
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    WarpedGrayImage = cv2.warpPerspective(img_gray, matrix, (imgWidth, imgHeight))
    WarpedColoredImage = cv2.warpPerspective(img_RGB, matrix, (imgWidth, imgHeight))
    
    # show_images([WarpedGrayImage],titles=['WarpedGrayImage'])
    print(np.shape(WarpedGrayImage))


    
    # Solving problem of False Contours The max area must be Greater than 10% of the Image area
    if(max_area<0.10*imgHeight*imgWidth):
        WarpedGrayImage=img_gray
        Wrapped=False
    else: 
        Wrapped=True

    show_images([img_RGB,image_with_contours,biggest_contour_img,WarpedColoredImage,WarpedGrayImage],['Original','All Contours','BiggestContour','WarpedColoredImage','WarpedGrayImage'])
    return (WarpedColoredImage,WarpedGrayImage,Wrapped)