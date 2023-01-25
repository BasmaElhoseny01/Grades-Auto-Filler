from modules.utils import *


def Save_to_Excel(dataFrame,path):

    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    # Finally, close the Excel file
    # via the close() method.
    workbook.close()
    
    #Creating a dataframe of the generated OCR list
    dataframe =dataFrame
    # print("Datt",dataframe)
    # print("Datt",dataframe[3])
    # print("Datt",dataframe[2])
    # print("Datt",dataframe[1])
    # print("Datt",dataframe[0])
    Code=np.copy(dataframe[3])
    Numbers=np.copy(dataframe[0])
    Col1=np.copy(dataframe[1])
    Col2=np.copy(dataframe[2])

    dataframe[0]=Code
    dataframe[1]=Numbers
    dataframe[2]=Col1
    dataframe[3]=Col2




    # temp=dataframe[0]
    # dataframe[0]=dataframe[3]

    # temp2=dataframe[1]
    # dataframe[1]=temp

    # temp=dataframe[2]
    # dataframe[2]=temp2

    # dataframe[3]=temp

    dataframe.reset_index(drop=True,inplace=True)
    dataframe = dataframe.applymap(lambda x: x.encode('unicode_escape').
                 decode('utf-8') if isinstance(x, str) else x)
    dataframe.style.applymap(lambda val: 'background-color: {}; color:{}'.format('transparent' if val != '-1' else 'red','black' if val != '-1' else 'red')).\
            to_excel(path, engine='openpyxl',header=False,index=False)
    # print('pathhh',path)
    # dataFrame.style.applymap(lambda val: 'background-color: {}; color:{}'.format('transparent' if val != '-1' else 'red','black' if val != '-1' else 'red')).to_csv(path)
    # dataFrame.to_csv(path,header=False,index=False)
    # dataFrame.style.apply('background-color: yellow').to_excel(path, engine='openpyxl')
    # dataFrame.style.apply(f, axis=0)
    return

# def f(dat, c='red'):
#     return [f'background-color: {c}' for i in dat]
