import customtkinter as ct
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
from Code.modules.utils import *
from Code.bubble_sheet import *
from modules.GradesSheet import *


# Trainng Model (to be in the Genral Main Function)
from modules.SymbolTrain import SVMTraining
model = SVMTraining()

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")


root = ct.CTk()
root.geometry("700x400")
root.title("Grade Auto Filler")

# Frame
frame = ct.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

radio_var = ct.IntVar()
checkbox_var = ct.IntVar()
model = None
see_steps = False
data = {}


def handleCheckBox():
    model = radio_var.get()
    print('model : ', model)
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
    print('checkbox : ', checkbox_var.get())
    progressBar = ct.CTkProgressBar(
        master=frame,
        orientation="horizontal",
        width=300,
        height=20,
        mode='determinate',
        progress_color="lime"
    )
    progressBar.place(relx=0.2, rely=0.9, anchor="w")
    progressBar.start()
    for i in range(1):
        frame.update_idletasks()
        time.sleep(1)
    progressBar.destroy()
    ct.CTkLabel(master=frame, text='Files Uploaded Successfully!',
                text_color="lime").place(relx=0.2, rely=0.9, anchor="w")


def start():
    model = radio_var.get()
    print('model : ', model)
    if (model == 1):
        do_work(data, checkbox_var.get())
    if (model == 2):
        # call do_work of table here
        print("Table")
        GradesSheet(data, SVM=model)
    else:
        print('Please, choose a model to start.')
    pass


    # radio buttons
ct.CTkLabel(master=frame, text='Choose the model.',
            text_color="lime").place(relx=0.2, rely=0.1, anchor="w")
radiobutton_1 = ct.CTkRadioButton(
    master=frame, text="Bubble Sheet", variable=radio_var, value=1).place(relx=0.2, rely=0.2, anchor="w")
radiobutton_2 = ct.CTkRadioButton(
    master=frame, text="Graded Sheet",  variable=radio_var, value=2).place(relx=0.75, rely=0.2, anchor="e")

# upload files
ct.CTkLabel(master=frame, text='Upload the files.',
            text_color="lime").place(relx=0.2, rely=0.3, anchor="w")
inputFileUpload = ct.CTkButton(
    master=frame,
    text='Choose the answers key',
    command=lambda: open_file(0)
).place(relx=0.2, rely=0.4, anchor="w")

gradesKeyFileUpload = ct.CTkButton(
    master=frame,
    text='Choose the grades key',
    command=lambda: open_file(1)
).place(relx=0.8, rely=0.4, anchor="e")

imageUpload = ct.CTkButton(
    master=frame,
    text='Choose the image path  ',
    command=lambda: open_file(3)
).place(relx=0.2, rely=0.5, anchor="w")

ExcelFileUpload = ct.CTkButton(
    master=frame,
    text='Choose the excel sheet',
    command=lambda: open_file(2)
).place(relx=0.8, rely=0.5, anchor="e")


ExcelFileUpload = ct.CTkButton(
    master=frame,
    text='Submit Files',
    command=lambda: uploadFiles()
).place(relx=0.4, rely=0.6, anchor="w")


checkbox = ct.CTkCheckBox(
    master=frame,
    text="See the steps.",
    variable=checkbox_var,
    onvalue=1,
    offvalue=0
).place(relx=0.2, rely=0.7, anchor="w")

ExcelFileUpload = ct.CTkButton(
    master=frame,
    text='Start',
    command=lambda: start()
).place(relx=0.2, rely=0.8, anchor="w")

root.mainloop()
