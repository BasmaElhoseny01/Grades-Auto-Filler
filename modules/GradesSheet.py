from modules.utils import *
from modules.PaperExtraction import *


def GradesSheet(Imagepath):
    #Step1 Get Page Wrapped
    PageExtarcted,Wrapped=ExtractPaper(Imagepath)
    if(not Wrapped):
        print("Contours Failed to get Page")
    #Step2 Extract  Cells
    # CellExtractor(PageExtarcted,'./test')


