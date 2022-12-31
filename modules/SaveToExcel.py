from modules.utils import *

def Save_to_Excel(dataFrame,path):
    # dataFrame.style.applymap(lambda val: 'background-color: {}; color:{}'.format('transparent' if val != '-1' else 'red','black' if val != '-1' else 'red')).to_csv(path)
    dataFrame.to_csv(path)
    # dataFrame.style.apply('background-color: yellow').to_excel(path, engine='openpyxl')
    return