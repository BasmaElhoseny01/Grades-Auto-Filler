from modules.utils import *
from modules.PaperExtraction import *
from modules.CellExtraction import *



def GradesSheet(data,SVM,DSVM,CodeSVM):
    Imagepath=data[3]
    index=data[4]
    OCR=data[5]
    #Step1 Get Page Wrapped
    WarpedColoredImage,PageExtarcted,Wrapped=ExtractPaper(Imagepath)
    print("Basma")
    if(not Wrapped):
        print("Contours Failed to get Page")
    #Step2 Extract  Cells
    CellExtractor(WarpedColoredImage,PageExtarcted,'./CellsExtracted/'+str(index)+"/",ExcelPath='./Excel/'+str(index)+".xlsx",SVM=SVM,OCR=OCR,DSVM=DSVM,CodeSVM=CodeSVM)
    
#Step 3 Cell Detector
#Step 4 Save to Excel   

