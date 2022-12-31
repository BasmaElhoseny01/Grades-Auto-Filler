from modules.utils import *
from modules.PaperExtraction import *
from modules.CellExtraction import *



def GradesSheet(Imagepath,index,SVM,OCR=False):
    #Step1 Get Page Wrapped
    WarpedColoredImage,PageExtarcted,Wrapped=ExtractPaper(Imagepath)
    if(not Wrapped):
        print("Contours Failed to get Page")

    #Step2 Extract  Cells
    CellExtractor(WarpedColoredImage,PageExtarcted,'./CellsExtracted/'+str(index)+"/",ExcelPath='./Excel/'+str(index)+".csv",SVM=SVM,OCR=OCR)


#Step 3 Cell Detector
#Step 4 Save to Excel   

