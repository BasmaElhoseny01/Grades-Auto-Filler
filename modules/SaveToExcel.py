from modules.utils import *

def Save_to_Excel(dataFrame,path):

    dataFrame.to_csv(path)
    return