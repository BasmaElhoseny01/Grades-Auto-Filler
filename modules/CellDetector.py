from modules.utils import *

#Input Binary Cell
#Index=0 =>Code Column
def CellDetection(cell,index):
    s=''
    if(index==3):
        #Code detection using OCR
        out = pytesseract.image_to_string(cell,config="outputbase digits")
        out=out.replace("\n","").replace("|","").replace("_","").replace("[","").strip()
        if(len(out)==0):
            out = pytesseract.image_to_string(cell)
        else:
            s = s +" "+ out
    # elif(index==0) :
    # #HandWritten Numbers 
    #     s=None

    elif(index==1 or index==2):
        #Symbols

    return s