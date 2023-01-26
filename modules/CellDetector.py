from modules.utils import *
from modules.SymbolDetector import SymbolValue,DigitValue,CodeValue

#Input Binary Cell
#Index=0 =>Code Column
def CellDetection(cell,index,SVM,OCR,DSVM,CodeSVM):
    print("inedxxx",index)
    s=''
    if(index==3):
        # Code detection using OCR
        out = pytesseract.image_to_string(cell,config="outputbase digits")
        out=out.replace("\n","").replace("|","").replace("_","").replace("[","").strip()
        if(len(out)==0):
            out = pytesseract.image_to_string(cell)
        else:
            s = s +" "+ out
        # if(OCR):
        #     #Code detection using OCR
        #     out = pytesseract.image_to_string(cell,config="outputbase digits")
        #     out=out.replace("\n","").replace("|","").replace("_","").replace("[","").strip()
        #     if(len(out)==0):
        #         out = pytesseract.image_to_string(cell)
        #     else:
        #         s = s +" "+ out
        # else:
        #     print("Code")
        #     s=s+" "+GetCode(cell,index,CodeSVM)
    elif(index==0) :
        #HandWritten Numbers
        if(OCR):
            #Call OCR
            s=s+" "+ get_digit(cell)
        else:
            #Use SVM
            s =s+" "+ str(DigitValue(cell,DSVM))
            

    elif(index==1 or index==2):
        #Symbols
        #Empty Cell
        Cropped=cell[20:np.shape(cell)[0]-20,20:np.shape(cell)[1]-20]
        if(np.sum(Cropped)==0):
            # Empty Cell
            s=""
        else :
            s =s+" "+ str(SymbolValue(cell,SVM))
    return s

def GetCode(thresh,index,CodeSVM):
    code=""

    # show_images([thresh])

    kernel = np.ones((2,2),np.uint8)
    Dilated_img = cv2.erode(thresh,kernel,iterations=3)
    # Erroded_img = cv2.dilate(Dilated_img,kernel,iterations=1)
    # show_images([Erroded_img],["Erroded"])

    # thninned5=thin(Erroded_img,2)
    # show_images([thninned5],["Thinned"])

    # Dilated_img = cv2.erode(np.float32(thninned5),kernel,iterations=1)
    # show_images([Dilated_img],["Dialated2"])



    # thresh=np.copy(Dilated_img)

    vis_img=np.copy(thresh)
    vis_img_1=np.copy(thresh)

    thresh = thresh.astype(np.uint8)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cv2.drawContours(vis_img_1, cnts, -1, 150, 15)
    # show_images([vis_img_1])
    # print("shape",np.shape(vis_img_1))



    digit_bb = []
    # loop over the digit area candidates
    for c in cnts:
        # compute the bounding box of the contour
        (x, y, w, h) = cv2.boundingRect(c)
        # if the contour is sufficiently large, it must be a digit
        if w >= 20 and (h >= 50 and h <= 800):
            digit_bb.append([x, y, w, h])
            cv2.drawContours(vis_img, [c], -1, 150, 15)
    
    digits = []
    i=0
    for bb in digit_bb:
        x,y,w,h = bb
        dig=thresh[y:y+h,x:x+w]
        # io.imsave('./CellsExtracted/'+str(index)+'/'+str(i)+'.jpg',dig)
        io.imsave('./CellsExtracted/'+str(index)+str(i)+'.jpg',dig)
        i=i+1
        code=code+str(CodeValue(dig,CodeSVM))
        digits.append(dig)

    # print("Digits",digits)  
    # print("Shape",np.shape(digits))   
    # show_images(np.array(digits))

    return code

# OCR TO DETECT DIGITS 0-9
def get_digit(image):
    """
    This function detects the id using OCR
    Arguments:
        img: Image
    Returns:
        The ID ,if found
    """
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(image, -1, sharpen_kernel)
    thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # show_images([thresh], ['thresholded image'])
    
    possible_values_for_0 = ['O', 'o']
    possible_values_for_1 = ['|', 'i', 'I', '!', '/', "\\", "T"]
    possible_values_for_2 = ['z', 'zz', 'Zz', 'Z', 'zZ', "ZZ"]
    possible_values_for_4 = ['q']
    possible_values_for_5 = ['So', 's', 'S']
    possible_values_for_7 = ['we']
    possible_values_for_9 = ['a','9)']
    # OCR
    # conf = '--psm 13 --oem 1 -c tessedit_char_whitelist=0123456789'
    digit = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
    trimmed = digit.strip()
    if(trimmed in possible_values_for_0):
        trimmed = "0"
    if(trimmed in possible_values_for_1):
        trimmed = "1"
    if(trimmed in possible_values_for_2):
        trimmed = "2"
    if(trimmed in possible_values_for_4):
        trimmed = "4"
    if(trimmed in possible_values_for_5):
        trimmed = "5"
    if(trimmed in possible_values_for_7):
        trimmed = "7"
    if(trimmed in possible_values_for_9):
        trimmed = "9"
    return trimmed