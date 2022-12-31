from modules.utils import *
from modules.SymbolDetector import SymbolValue,DigitValue

#Input Binary Cell
#Index=0 =>Code Column
def CellDetection(cell,index,SVM,OCR,DSVM):
    s=''
    if(index==3):
        #Code detection using OCR
        out = pytesseract.image_to_string(cell,config="outputbase digits")
        out=out.replace("\n","").replace("|","").replace("_","").replace("[","").strip()
        if(len(out)==0):
            out = pytesseract.image_to_string(cell)
        else:
            s = s +" "+ out
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


def get_digit(image):
#
#This function detects the id using OCR
#Arguments:
#    img: Image
#Returns:
#    The ID ,if found
#"""
# image = cv2.imread(image_path)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(image, -1, sharpen_kernel)
    thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # show_images([thresh], ['thresholded image'])
    possible_values_for_1 = ['|', 'i', 'I', '!', '/', "\\"]
    # OCR
    # conf = '--psm 13 --oem 1 -c tessedit_char_whitelist=0123456789'
    digit = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
    trimmed = digit.strip()
    if(trimmed in possible_values_for_1):
        trimmed = str(1)
    return trimmed