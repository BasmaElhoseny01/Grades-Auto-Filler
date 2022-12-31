
def Page_Extraction(path,ocrFunction = None):
    # Dictonary to store data to be returned
    ret = {}
    # Read Image
    Gray_Scale_img=cv.imread(path,0)
    # Gray_Scale_img=rgb2gray(Original_img)

    # Show_Images([Original_img],['Original'])
    show_images([Gray_Scale_img],['GrayScale'])
    
    # Step 1 Enhance lines of the image
    #1.Guassian to blur image 
    kernel_size=max(int(Gray_Scale_img.shape[0] * 0.005), int(Gray_Scale_img.shape[1] * 0.005))
    # Kernel must have odd values because of GaussianBlur
    if kernel_size % 2 == 0:
        kernel_size += 1
    kernel=(kernel_size,kernel_size) #filter size
    Gaussian_Img=cv.GaussianBlur(Gray_Scale_img,kernel,1)
    print(np.shape(Gaussian_Img))
    
    #2.Adpative Thresholding
    # If we tried to use Normal Thresholding =>Global Thresholding Regions Black so use like local thershold for every region depending on its neigh
    Thresholded_Img = cv.adaptiveThreshold(Gaussian_Img, 255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 21, 10)
    #3.La Placian
    laplacian = cv.Laplacian(Thresholded_Img, cv.CV_64F)
    # Convert data type from 64f to unsigned 8-bit integer
    laplacian = np.uint8(np.absolute(laplacian))
#     show_images([Gray_Scale_img,Gaussian_Img],['Gray Scale Imge','Guassian Sigma=1'])
#     show_images([Thresholded_Img,laplacian],['Thersholded Img','La Placian'])
    
    # Extract Table Region
    #Table takes most of the Region so Extract table by finding largest countor with 4 sides

    #1.Find Largest rectangle in the image
    # FIND CONTOUR
    contours, _ = cv.findContours(laplacian, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    #Identifying Contour with largest 4 sides
    table_contour, table_contour_approx = findLargestQuadrilateralContour(contours)
    if table_contour[0] is None:
        raise ValueError("No table detected.")
    print(table_contour_approx)
    
    # Sort points in clocwise order, compute table width and height
    table_pts, table_width, table_height =processContour(table_contour_approx[0])\
    
    #2.
    # EXTRACT TABLE REGION
    # Start with a full black image
    mask = np.zeros(Gray_Scale_img.shape).astype(Gray_Scale_img.dtype)
    # Create a mask for the table region
    cv.fillPoly(mask, table_contour, (255, 255, 255))
    
    # Apply the mask to the thresholded image, filling the region
    # outside of the table with white
    table_img = cv.bitwise_and(Gray_Scale_img, mask)
    
    
    # WARP TABLE
    # Use warp to extract the table region from the processed image
    # by mapping table points to a new image of size table_width x table_height
    target_points = np.float32([[0, 0], [table_width, 0], [table_width, table_height], [0, table_height]])
    matrix = cv.getPerspectiveTransform(table_pts, target_points)
    # Apply warp to the image to extract the tbale region
    warped = cv.warpPerspective(table_img, matrix, (table_width, table_height))
    # Apply warp to mask
    warped_mask = cv.warpPerspective(mask, matrix, (table_width, table_height))
    # Resize warped and mask to have width 750px
    scale_factor = 1500 / table_width
    warped = cv.resize(warped, (0, 0), fx=scale_factor, fy=scale_factor)
    warped_mask = cv.resize(warped_mask, (0, 0), fx=scale_factor, fy=scale_factor)
    warped = cv.GaussianBlur(warped, (5, 5), 2)
    # Apply threshold
    warped = cv.adaptiveThreshold(warped, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 2)
    return (warped)