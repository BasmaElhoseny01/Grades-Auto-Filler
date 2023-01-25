from modules.DigitsTrain import CodeTraining
from modules.DigitsTrain import DigitTraining
from modules.SymbolTrain import SVMTraining
import customtkinter as ct
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
from modules.utils import *
from modules.bubble_sheet import *
from modules.GradesSheet import *


# Trainng Model(to be in the Genral/ Main Function)
model = SVMTraining()

# Trainng Model (to be in the Genral Main Function)
Digitsmodel = DigitTraining()


# Traning on Codes
Codemodel = CodeTraining()


ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")


root = ct.CTk()
root.geometry("700x500")
root.title("Grades Auto Filler")

# Frame
frame = ct.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

radio_var = ct.IntVar()
checkbox_var = ct.IntVar()
checkbox_OCR_var = ct.IntVar()
index_var = ct.StringVar()
model = None
see_steps = False
data = {}


def handleCheckBox():
    model = radio_var.get()
    return


def open_file(which_file):
    my_file = askopenfile(mode='r')
    if (which_file == 0):  # answers key file
        data[0] = my_file.name

    if (which_file == 1):  # grades key file
        data[1] = my_file.name

    if (which_file == 2):  # excel file
        data[2] = my_file.name

    if (which_file == 3):  # image to be corrected
        data[3] = my_file.name

    return


def uploadFiles():
    progressBar = ct.CTkProgressBar(
        master=frame,
        orientation="horizontal",
        width=300,
        height=5,
        mode='determinate',
        progress_color="lime"
    )
    progressBar.place(relx=0.28, rely=0.76, anchor="w")
    progressBar.start()
    for i in range(1):
        frame.update_idletasks()
        time.sleep(1)
    progressBar.destroy()
    ct.CTkLabel(master=frame, text='Files Uploaded Successfully!',
                text_color="lime").place(relx=0.6, rely=0.8, anchor="w")


def handleRadioButton():
    frame.update_idletasks()

    return


def start():
    model = radio_var.get()
    data[4] = index_var.get()
    data[5] = True if checkbox_OCR_var.get() == 1 else False

    if (model == 1):
        do_work(data, checkbox_var.get())
    if (model == 2):
        GradesSheet(data, SVM=model, DSVM=Digitsmodel, CodeSVM=Codemodel)
    else:
        print('Please, choose a model to start.')
    pass

    # radio buttons


ct.CTkLabel(master=frame, text='Choose the model.',
            text_color="lime").place(relx=0.2, rely=0.05, anchor="w")
radiobutton_1 = ct.CTkRadioButton(
    master=frame, text="Bubble Sheet", variable=radio_var, value=1).place(relx=0.2, rely=0.1, anchor="w")
radiobutton_2 = ct.CTkRadioButton(
    master=frame, text="Graded Sheet", variable=radio_var, value=2).place(relx=0.77, rely=0.1, anchor="e")

# Bubble sheet
ct.CTkLabel(master=frame, text='Bubble sheet files.',
            text_color="lime").place(relx=0.2, rely=0.2, anchor="w")
inputFileUpload = ct.CTkButton(
    master=frame,
    text='Choose the answers key',
    command=lambda: open_file(0)
).place(relx=0.2, rely=0.3, anchor="w")
imageUpload = ct.CTkButton(
    master=frame,
    text='Choose the image  ',
    command=lambda: open_file(3)
).place(relx=0.2, rely=0.4, anchor="w")
ExcelFileUpload = ct.CTkButton(
    master=frame,
    text='Choose the excel sheet',
    command=lambda: open_file(2)
).place(relx=0.2, rely=0.5, anchor="w")
gradesKeyFileUpload = ct.CTkButton(
    master=frame,
    text='Choose the grades key',
    command=lambda: open_file(1)
).place(relx=0.2, rely=0.6, anchor="w")
ExcelFileUpload = ct.CTkButton(
    master=frame,
    text='Submit Files',
    command=lambda: uploadFiles()
).place(relx=0.4, rely=0.7, anchor="w")
checkbox = ct.CTkCheckBox(
    master=frame,
    text="See the steps.",
    variable=checkbox_var,
    onvalue=1,
    offvalue=0
).place(relx=0.2, rely=0.8, anchor="w")
ExcelFileUpload = ct.CTkButton(
    master=frame,
    text='Start',
    command=lambda: start()
).place(relx=0.4, rely=0.9, anchor="w")

# Table Grades
ct.CTkLabel(master=frame, text='Bubble sheet files.',
            text_color="lime").place(relx=0.6, rely=0.2, anchor="w")

imageUpload = ct.CTkButton(
    master=frame,
    text='Choose the image',
    command=lambda: open_file(3)
).place(relx=0.6, rely=0.3, anchor="w")

index_input = ct.CTkEntry(master=frame, textvariable=index_var, placeholder_text="Enter the index").place(
    relx=0.6, rely=0.4, anchor="w")

checkbox = ct.CTkCheckBox(
    master=frame,
    text="OCR",
    variable=checkbox_OCR_var,
    onvalue=1,
    offvalue=0
).place(relx=0.6, rely=0.5, anchor="w")
root.mainloop()
