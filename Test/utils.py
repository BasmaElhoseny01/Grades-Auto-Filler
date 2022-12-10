# Imports
import cv2 as cv
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import math

# Read RGB image uisng CV and result is a RGB image
def Read_RGB_Image(path):
    image=cv.imread(path,1)#cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected.
    # Converting BGR color to RGB color format
    RGB_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return RGB_img

# Read Gray image uisng CV and result is a Gray image
def Read_GrayScale_Image(path):
    image=cv.imread(path,0)
    return image


def show_images(images,titles=None):
    #This function is used to show image(s) with titles by sending an array of images and an array of associated titles.
    # images[0] will be drawn with the title titles[0] if exists
    # You aren't required to understand this function, use it as-is.
    n_ims = len(images)
    if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
    fig = plt.figure()
    n = 1
    for image,title in zip(images,titles):
        a = fig.add_subplot(1,n_ims,n)
        if image.ndim == 2: 
            plt.gray()
        plt.imshow(image)
        a.set_title(title)
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show()


def showHist(img):
    # An "interface" to matplotlib.axes.Axes.hist() method
    plt.figure()
    imgHist = histogram(img, nbins=256)
    
    bar(imgHist[1].astype(np.uint8), imgHist[0], width=0.8, align='center')

# # Show images in plot
# def Show_Images(images,titles):
#     # Create Figure
#     fig=plt.figure(figsize=(20, 10))
    
#     # Setting number of rows and columns
#     columns=2 # 2columns
#     rows=math.ceil(np.shape(images)[0]/columns) #No of rows    
    
#     n=1 #Counter for the subplots order
#     for image,title in zip(images,titles):
#         #Add subplot @ order postion 
#         fig.add_subplot(rows, columns, n)
#         n+=1
#         plt.axis('off')
#         plt.title(title)
#         plt.imshow(image)
        
    

# Function to sort points in a contour in clockwise order, starting from top left
def processContour(approx):
    # Reshape array([x, y], ...) to array( array([x], [y]), ...)
    approx = approx.reshape((4, 2))

    # Sort points in clockwise order, starting from top left
    pts = np.zeros((4, 2), dtype=np.float32)

    # Add up all values
    # Smallest sum = top left point
    # Largest sum = bottom right point
    s = approx.sum(axis=1)
    pts[0] = approx[np.argmin(s)]
    pts[2] = approx[np.argmax(s)]

    # For the other 2 points, compute difference between all points
    # Smallest difference = top right point
    # Largest difference = bottom left point
    diff = np.diff(approx, axis=1)
    pts[1] = approx[np.argmin(diff)]
    pts[3] = approx[np.argmax(diff)]

    # Calculate smallest height and width
    width = int(min(pts[1][0] - pts[0][0], pts[2][0] - pts[3][0]))
    height = int(min(pts[3][1] - pts[0][1], pts[2][1] - pts[1][1]))

    return pts, width, height

# Function to find the largest 4-sided contour from an array of countours
def findLargestQuadrilateralContour(contours):
    # Sort contours from smallest area to biggest
    sorted_contours = sorted(contours, key=cv.contourArea, reverse=True)

    biggest_contour = None
    biggest_contour_approx = None

    for cnt in sorted_contours:
        # Get the length of the perimeter
        perimeter = cv.arcLength(cnt, True)

        # Approximate a shape that resembles the contour
        # This is needed because the image might be warped, thus
        # edges are curved and not perfectly straight
        approx = cv.approxPolyDP(cnt, 0.01 * perimeter, True)

        # Check if the approximation contains only 4 sides
        # (i.e. quadrilateral)
        if len(approx) == 4:
            biggest_contour = cnt
            biggest_contour_approx = approx
            break

    return [biggest_contour], [biggest_contour_approx]

# This funciton is used to recursively find the leaf entries in a dictionary, and replace
# the last list values with dictionaries. This is done beacuse a new table heading should
# be represented by a dictionary type, whereas column values are stored in a list.
def leafListToDict(column):
    # If the column is a list...
    # This could happen if a heading has multiple values followed by a column split
    # E.g.
    #       +-----------------+------------------+-------------------+
    #       |        A        |        B         |         C         |
    #       +-----------------+------------------+-------------------+
    #       |     value1      |     value2       |      value3       |
    #       +-----------------+------------------+-------------------+
    #       |     value4      |     value5       |      value6       |
    #       +--------+--------+--------+---------+---------+---------+
    #       |   D    |   E    |   F    |    G    |    H    |    I    |
    #       +--------+--------+--------+---------+---------+---------+
    #       | value7 | value8 | value9 | value10 | value11 | value12 |
    #       +--------+--------+--------+---------+---------+---------+
    # Column A has 2 values (value1, value4) followed by a column split (D, E)
    if type(column) is list:
        # If the last item in the list is a dictionary, iterate over that dictionary to
        # find the leaf list
        if type(column[-1]) is dict:
            return leafListToDict(column[-1])
        
        # Otherwise create a new dictiorary and return it
        new_value = {}
        column.append(new_value)
        return [new_value]

    # If the values are all empty lists...
    # any(list) returns True if list contains non-empty lists
    # E.g. any([[1], [2], [3]]) = True, any([[], [], []]) = False
    if not any(column.values()):
        # ...replace them with dictionaries
        for key in column:
            column[key] = {}
        return column.values()
    # Otherwise recursively iterate all the dictionaries until the leaf key-value pair is
    # reached. Double for-loop is used to flatten the return array
    # E.g. [[a], [b], [c]] => [a, b, c]
    return [column for child in column.values() for column in leafListToDict(child)]


# Function to find the largest 4-sided contour from an array of countours
def findSecondLargestQuadrilateralContour(contours):
    # Sort contours from smallest area to biggest
    sorted_contours = sorted(contours, key=cv.contourArea, reverse=True)
#     Drop first 4 Elements
    sorted_contours=sorted_contours[4:]

    biggest_contour = None
    biggest_contour_approx = None

    for cnt in sorted_contours:
        # Get the length of the perimeter
        perimeter = cv.arcLength(cnt, True)

        # Approximate a shape that resembles the contour
        # This is needed because the image might be warped, thus
        # edges are curved and not perfectly straight
        approx = cv.approxPolyDP(cnt, 0.01 * perimeter, True)

        # Check if the approximation contains only 4 sides
        # (i.e. quadrilateral)
        if len(approx) == 4:
            biggest_contour = cnt
            biggest_contour_approx = approx
            break

    return [biggest_contour], [biggest_contour_approx]

# This funciton is used to recursively find the leaf entries in a dictionary, and replace
# the last list values with dictionaries. This is done beacuse a new table heading should
# be represented by a dictionary type, whereas column values are stored in a list.
def leafListToDict(column):
    # If the column is a list...
    # This could happen if a heading has multiple values followed by a column split
    # E.g.
    #       +-----------------+------------------+-------------------+
    #       |        A        |        B         |         C         |
    #       +-----------------+------------------+-------------------+
    #       |     value1      |     value2       |      value3       |
    #       +-----------------+------------------+-------------------+
    #       |     value4      |     value5       |      value6       |
    #       +--------+--------+--------+---------+---------+---------+
    #       |   D    |   E    |   F    |    G    |    H    |    I    |
    #       +--------+--------+--------+---------+---------+---------+
    #       | value7 | value8 | value9 | value10 | value11 | value12 |
    #       +--------+--------+--------+---------+---------+---------+
    # Column A has 2 values (value1, value4) followed by a column split (D, E)
    if type(column) is list:
        # If the last item in the list is a dictionary, iterate over that dictionary to
        # find the leaf list
        if type(column[-1]) is dict:
            return leafListToDict(column[-1])
        
        # Otherwise create a new dictiorary and return it
        new_value = {}
        column.append(new_value)
        return [new_value]

    # If the values are all empty lists...
    # any(list) returns True if list contains non-empty lists
    # E.g. any([[1], [2], [3]]) = True, any([[], [], []]) = False
    if not any(column.values()):
        # ...replace them with dictionaries
        for key in column:
            column[key] = {}
        return column.values()
    # Otherwise recursively iterate all the dictionaries until the leaf key-value pair is
    # reached. Double for-loop is used to flatten the return array
    # E.g. [[a], [b], [c]] => [a, b, c]
    return [column for child in column.values() for column in leafListToDict(child)]