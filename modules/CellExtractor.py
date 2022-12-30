from modules.PageExtractor import *
from modules.utils import *

def CellExtractor(path,CellsSavePath):

    img=io.imread(path)
    imageArr=getPageWarped(img, thresh1=180)
    show_images(imageArr,titles=['img','grayImg','thresholdedImg','imgWithContours','img','img'])
    Table_Extracted=np.copy(imageArr[5])


    # print(np.max(Table_Extracted))
    # print(np.shape(Table_Extracted))
    # Table_Extracted=rgb2gray(Table_Extracted)
    # Converting table to binary
    thresh,img_bin = cv2.threshold(Table_Extracted,128,255,cv2.THRESH_BINARY)
    # thresh,img_bin = cv2.threshold(Table_Extracted,128,255,cv2.THRESH_OTSU)

    img_bin = 255-img_bin
    show_images([img_bin],titles=['Bianry Image'])

    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, np.array(img).shape[1]//150))
    eroded_image = cv2.erode(img_bin, vertical_kernel, iterations=10)
    show_images([eroded_image],titles=['Erroded'])

    vertical_lines = cv2.dilate(eroded_image, vertical_kernel, iterations=10)
    show_images([vertical_lines],titles=['Dilated'])

    hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (np.array(img).shape[1]//150, 1))
    image_2 = cv2.erode(img_bin, hor_kernel, iterations=10)
    horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=10)
    show_images([image_2,horizontal_lines],titles=['Eroded horizontal','Dilated horizontal'])

    vertical_horizontal_lines = cv2.addWeighted(vertical_lines, 0.5, horizontal_lines, 0.5, 0.0)
    vertical_horizontal_lines_2 = cv2.erode(~vertical_horizontal_lines, cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2)), iterations=3)
    show_images([vertical_horizontal_lines,vertical_horizontal_lines_2],titles=['Added hor+v',' erosion to result'])

    thresh, vertical_horizontal_lines_3 = cv2.threshold(vertical_horizontal_lines_2,128,255, cv2.THRESH_BINARY)
    b_image = cv2.bitwise_not(cv2.bitwise_xor(Table_Extracted,vertical_horizontal_lines_3))
    show_images([vertical_horizontal_lines_3,b_image],titles=['1','2'])


    img1 = cv2.cvtColor(vertical_horizontal_lines_3, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(img1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    boundingBoxes = [cv2.boundingRect(c) for c in contours]
    (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes),
    key=lambda x:x[1][1]))

    boxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if (w<500 and h<500):
            image = cv2.rectangle(Table_Extracted,(x,y),(x+w,y+h),(0,255,0),2)
            boxes.append([x,y,w,h])
    plotting = plt.imshow(image,cmap='gray')
    plt.title("Identified contours")
    plt.show()

    rows=[]
    columns=[]
    heights = [boundingBoxes[i][3] for i in range(len(boundingBoxes))]
    mean = np.mean(heights)
    print(mean)
    columns.append(boxes[0])
    previous=boxes[0]
    for i in range(1,len(boxes)):
        if(boxes[i][1]<=previous[1]+mean/2):
            columns.append(boxes[i])
            previous=boxes[i]
            if(i==len(boxes)-1):
                rows.append(columns)
        else:
            rows.append(columns)
            columns=[]
            previous = boxes[i]
            columns.append(boxes[i])
    print("Rows")
    for row in rows:
        print(row)
        
    print(np.shape(rows))


    total_cells=0
    for i in range(len(row)):
        if len(row[i]) > total_cells:
            total_cells = len(row[i])
    print(total_cells)


    center = [int(rows[i][j][0]+rows[i][j][2]/2) for j in range(len(rows[i])) if rows[0]]
    print(center)
    center=np.array(center)
    center.sort()
    print(center)


    boxes_list = []
    for i in range(len(rows)):
        l=[]
        for k in range(total_cells):
            l.append([])
    #     print(l)
        for j in range(len(rows[i])):
            diff = abs(center-(rows[i][j][0]+rows[i][j][2]/4))
            minimum = min(diff)
            indexing = list(diff).index(minimum)
    #         print(indexing)
            l[indexing-1].append(rows[i][j])
        boxes_list.append(l)
    for box in boxes_list:
        print(box)

    import pytesseract
    dataframe_final=[]
    for i in range(len(boxes_list)):
        for j in range(len(boxes_list[i])):
            s=''
            if(len(boxes_list[i][j])==0):
                dataframe_final.append(' ')
            else:
                for k in range(len(boxes_list[i][j])):
                    y,x,w,h = boxes_list[i][j][k][0],boxes_list[i][j][k][1], boxes_list[i][j][k][2],boxes_list[i][j][k][3]
                    roi = image[x:x+h, y:y+w]
                    cropHeight= int(0.1* roi.shape[0])
                    cropWidth= int(0.03* roi.shape[1])
                    roi= roi[cropHeight:-cropHeight,cropWidth:-cropWidth]
                    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
                    border = cv2.copyMakeBorder(roi,2,2,2,2, cv2.BORDER_CONSTANT,value=[255,255])
                    resizing = cv2.resize(border, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                    dilation = cv2.dilate(resizing, kernel,iterations=1)
                    erosion = cv2.erode(dilation, kernel,iterations=2)
                    img3 = cv2.cvtColor(erosion, cv2.COLOR_BGR2GRAY)
                    thresh = cv2.threshold(img3, 127, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
                    options = "outputbase digits"
                    out = pytesseract.image_to_string( thresh,config=options)
                    show_images([thresh])
                    io.imsave(CellsSavePath+str(i)+str(j)+str(k)+'.jpg',thresh)
                    out=out.replace("\n","").replace("|","").replace("_","").replace("[","").strip()
                    if(len(out)==0):
                        out = pytesseract.image_to_string(thresh)
                    else:
                        s = s +" "+ out
                dataframe_final.append(s.strip())
    print(dataframe_final)


    arr = np.array(dataframe_final)


    import pandas as pd
    dataframe = pd.DataFrame(arr.reshape(len(rows), total_cells))
    # data = dataframe.style.set_properties(align="left")
    #print(data)
    #print(dataframe)
    # d=[]
    # for i in range(0,len(rows)):
    #     for j in range(0,total_cells):
    #         print(dataframe[i][j],end=" ")
    # print()


    dataframe.to_csv("output.csv")