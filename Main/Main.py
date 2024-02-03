from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import cv2
import util
import os
import subprocess
import tempfile 
import csv
import os
import shutil
from tkcalendar import DateEntry  # pip install tkcalendar
import sqlite3
import sys
import random
import Student_backend
import College_Marksheet_Backend
import Staff_backend
import matplotlib.pyplot as plt
import pandas as pd
import threading
import College_Marksheet_Backend
import College_Fee_Backend
import tkinter.messagebox
import datetime
sys.path.insert(0, 'windows/')
root = Tk()
root.title("Classverge")
root.geometry('1520x1080')
root.maxsize(width=1520,height=1080)
root.minsize(width=1520,height=1080)
root.config(bg="#1A2238")
root.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
logo = PhotoImage(file="C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.png")
logo_label=Label(image=logo)
logo_label.place(x=410,y=100)
def performance():
    def display_pie_chart():
        """
        This function displays a pie chart of the selected student's marks.
        """
        # Get the selected student's name
        selected_student = student_listbox.get(tk.ACTIVE)
        
        # Load the CSV file
        try:
            df = pd.read_csv("students.csv")
        except FileNotFoundError:
            # Log the error
            print("Error: File not found")
            return
        
        # Filter the data for the selected student
        student_data = df[df["Name"] == selected_student]
        
        # Get the marks for each subject
        marks = student_data.iloc[0][1:].tolist()
        
        # Create a pie chart
        fig, ax = plt.subplots()
        ax.pie(marks, labels=["EM-4","CNND","OS","AT","COA"], autopct='%1.1f%%')
        ax.set_title(f"{selected_student}'s Marks")
        plt.show()

    def upload_csv_file():
        """
        This function loads the CSV file and displays the list of students in the GUI.
        """
        # Load the CSV file
        try:
            file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
            df = pd.read_csv(file_path)

        except FileNotFoundError:
            # Log the error
            print("Error: File not found")
            return
        
        # Clear the listbox
        student_listbox.delete(0, tk.END)
        
        # Get the list of students
        students = df["Name"].tolist()
        
        # Display the list of students in the GUI
        for student in students:
            student_listbox.insert(tk.END, student)

    def go_back():
        """
        This function destroys the pie chart window and returns to the main window.
        """
        pie_chart_window.destroy()
    def back():
        root.destroy()
    # Create the main GUI
    root = tk.Tk()
    root.title("Performance")
    root.minsize(width=400,height=250)
    root.maxsize(width=400,height=250)
    root.config(bg = '#1A2238')
    root.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
    title_lab = tk.Label(
        root,
        text='PERFORMANCE',
        font=('Consolas', 20, 'bold'),
        pady=12,bg="#1A2238",
        fg="#F4DB7D",padx=0
    )
    title_lab.pack()
    # Create the widgets
    upload_button = tk.Button(root, text="Upload CSV File",  command=upload_csv_file,bg="#FF6A3D",fg="White")
    student_listbox = tk.Listbox(root)
    display_button = tk.Button(root, text="Display Pie Chart", command=display_pie_chart,bg="#FF6A3D",fg="White")
    back1 = tk.Button(root, text="Back",bg="#9DAAF2",fg="Black", command=back)
    # Add the widgets to the main GUI
    upload_button.place(x=10,y=125,)
    student_listbox.place(x=130,y=50)
    display_button.place(x=280,y=125)
    back1.place(x=300,y=200)
    # Create the pie chart window
    pie_chart_window = tk.Toplevel(root)
    pie_chart_window.title("Pie Chart")
    pie_chart_window.withdraw()  # Hide the window until it's needed

    # Create the back button
    back_button = tk.Button(pie_chart_window, text="Back", command=go_back)

    # Add the back button to the pie chart window
    back_button.place(x=150,y=280)

    # Start the main GUI loop
    root.mainloop()
def add_student():  
       class Student_Information():
              def __init__(self, master):
                     self.master = master
                     self.master.title('Staff Information')
                     self.master.geometry('1350x750')
                     self.master.config(bg = '#1A2238')
                     self.master.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
                     def information():

                            self.name = StringVar()
                            self.father_name = StringVar()
                            self.mother_name = StringVar()
                            self.address = StringVar()
                            self.mobileno = StringVar()
                            self.email_address = StringVar()
                            self.date_of_birth = StringVar()
                            self.gender = StringVar()
                            


                            def Staff_Record(event):
                                   try: 
                                          global selected_tuple
                                          
                                          index = self.listbox.curselection()[0]
                                          selected_tuple = self.listbox.get(index)

                                          self.Text_Entry_name.delete(0, END)
                                          self.Text_Entry_name.insert(END, selected_tuple[1])
                                          self.Text_Entry_Father_Name.delete(0, END)
                                          self.Text_Entry_Father_Name.insert(END, selected_tuple[2])
                                          self.Text_Entry_Mother_Name.delete(0, END)
                                          self.Text_Entry_Mother_Name.insert(END, selected_tuple[3])
                                          self.Text_Entry_address.delete(0, END)
                                          self.Text_Entry_address.insert(END, selected_tuple[4])
                                          self.Text_Entry_mobileno.delete(0, END)
                                          self.Text_Entry_mobileno.insert(END, selected_tuple[5])
                                          self.Text_Entry_email_address.delete(0, END)
                                          self.Text_Entry_email_address.insert(END, selected_tuple[6])
                                          self.Text_Entry_date_of_birth.delete(0, END)
                                          self.Text_Entry_date_of_birth.insert(END, selected_tuple[7])
                                          self.Text_Entry_gender.delete(0, END)
                                          self.Text_Entry_gender.insert(END, selected_tuple[8])
                                   except IndexError:
                                          pass


                            def Add():
                                   if(len(self.name.get()) != 0):
                                          Student_backend.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                             self.gender.get())
                                          self.listbox.delete(0, END)
                                          self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                      self.gender.get()))

                            def Display():
                                   self.listbox.delete(0, END)
                                   for row in Student_backend.view():
                                          self.listbox.insert(END, row, str(' '))


                            def Exit():
                                   Exit =messagebox.askyesno("Login System", "Confirm if you want to Exit")
                                   if Exit > 0:
                                          self.master.destroy()
                                          return 
                                   

                            def Reset():
                                   self.name.set('')
                                   self.father_name.set('')
                                   self.mother_name.set('')
                                   self.address.set('')
                                   self.mobileno.set('')
                                   self.email_address.set('')
                                   self.date_of_birth.set('')
                                   self.gender.set('')
                                   self.listbox.delete(0, END)

                            

                            def Delete():
                                   if(len(self.name.get()) != 0):
                                          Student_backend.delete(selected_tuple[0])
                                          Reset()
                                          Display()


                            def Search():
                                   self.listbox.delete(0, END)
                                   for row in Staff_backend.search(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), self.gender.get()):
                                          self.listbox.insert(END, row, str(' '))
                                          

                            def Update():
                                   if(len(self.name.get()) != 0):
                                          Student_backend.delete(selected_tuple[0])
                                          if(len(self.name.get()) != 0):
                                                 Student_backend.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                    self.gender.get())

                                                 self.listbox.delete(0, END)
                                                 self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                             self.gender.get()))
                                   




                            self.Student_Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial', 20, 'bold'), \
                                                               bg = '#1A2238',fg="#FF6A3D", bd = 15, relief = 'ridge',text="Enter Details")
                            self.Student_Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

                            self.Student_Frame_1 = LabelFrame(self.Student_Main_Frame, width = 600, height = 400, font = ('arial', 15, 'bold'), \
                                                        relief = 'ridge', bd = 10, bg = '#1A2238',fg="#FF6A3D", text = 'Staff INFORMATION ')
                            self.Student_Frame_1.grid(row = 1, column = 0, padx = 10)

                            self.Student_Frame_2 = LabelFrame(self.Student_Main_Frame, width = 750, height = 400, font = ('arial', 15, 'bold'), \
                                                        relief = 'ridge', bd = 10, bg = '#1A2238',fg="#FF6A3D", text = 'STAFF DATABASE')
                            self.Student_Frame_2.grid(row = 1, column = 1, padx = 5)
                            
                            self.Student_Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial', 10, 'bold'), \
                                                        bg = '#1A2238', relief = 'ridge', bd = 13)
                            self.Student_Frame_3.grid(row = 2, column = 0, pady = 10)


                            

                            self.lbl_Name = Label(self.Student_Frame_1, text ='Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_Name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                            self.lbl_father_name = Label(self.Student_Frame_1, text ='Father Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_father_name.grid(row = 1, column = 0, sticky = W, padx = 20)
                            self.lbl_mother_name = Label(self.Student_Frame_1, text ='Mother Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_mother_name.grid(row = 2, column = 0, sticky = W, padx = 20)
                            self.lbl_address = Label(self.Student_Frame_1, text ='Address', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_address.grid(row = 3, column = 0, sticky = W, padx = 20)
                            self.lbl_mobileno = Label(self.Student_Frame_1, text ='Mobile Number', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_mobileno.grid(row = 4, column = 0, sticky = W, padx = 20)
                            self.lbl_email_address = Label(self.Student_Frame_1, text ='Email Address', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_email_address.grid(row = 5, column = 0, sticky = W, padx = 20)
                            self.lbl_dateOf_birth = Label(self.Student_Frame_1, text ='Date of Birth', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_dateOf_birth.grid(row = 6, column = 0, sticky = W, padx = 20)
                            self.lbl_gender = Label(self.Student_Frame_1, text ='Gender', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_gender.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 10)



                            self.Text_Entry_name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.name)
                            self.Text_Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_Father_Name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.father_name)
                            self.Text_Entry_Father_Name.grid(row = 1, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_Mother_Name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.mother_name)
                            self.Text_Entry_Mother_Name.grid(row = 2, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_address = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.address)
                            self.Text_Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_mobileno = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.mobileno)
                            self.Text_Entry_mobileno.grid(row = 4, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_email_address = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.email_address)
                            self.Text_Entry_email_address.grid(row = 5, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_date_of_birth = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.date_of_birth)
                            self.Text_Entry_date_of_birth.grid(row = 6, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_gender = ttk.Combobox(self.Student_Frame_1, values = (' ', 'Male', 'Female', 'Others'), \
                                                               font = ('arial',17,'bold'), textvariable = self.gender, width = 19)
                            self.Text_Entry_gender.grid(row = 7, column = 1, padx = 10, pady = 5)





                            self.SAVE_BUTTON = Button(self.Student_Frame_3, text ='SAVE', font = ('arial', 17, 'bold'), width = 8, command = Add ,bg="#9DAAF2")
                            self.SAVE_BUTTON.grid(row = 0, column = 0, padx = 10, pady = 10)
                            self.BUTTON_DISPLAY = Button(self.Student_Frame_3, text ='DISPLAY', font = ('arial', 17, 'bold'), width = 8, command = Display ,bg="#9DAAF2")
                            self.BUTTON_DISPLAY.grid(row = 0, column = 1, padx = 10, pady = 10)
                            self.BUTTON_RESET = Button(self.Student_Frame_3, text ='RESET', font = ('arial', 17, 'bold'), width = 8, command = Reset ,bg="#9DAAF2")
                            self.BUTTON_RESET.grid(row = 0, column = 2, padx = 10, pady = 10)
                            self.BUTTON_UPDATE = Button(self.Student_Frame_3, text ='UPDATE', font = ('arial', 17, 'bold'), width = 8, command = Update ,bg="#9DAAF2")
                            self.BUTTON_UPDATE.grid(row = 0, column = 3, padx = 10, pady = 10)
                            self.BUTTON_DELETE = Button(self.Student_Frame_3, text ='DELETE', font = ('arial', 17, 'bold'), width = 8, command = Delete,bg="#9DAAF2")
                            self.BUTTON_DELETE.grid(row = 0, column = 4, padx = 10, pady = 10)
                            # self.BUTTON_SEARCH = Button(self.Student_Frame_3, text ='SEARCH', font = ('arial', 17, 'bold'), width = 8, command = Search ,bg="#9DAAF2")
                            # self.BUTTON_SEARCH.grid(row = 0, column = 5, padx = 10, pady = 10)
                            self.BUTTON_EXIT = Button(self.Student_Frame_3, text ='EXIT', font = ('arial', 17, 'bold'), width = 8, command = Exit ,bg="#9DAAF2")
                            self.BUTTON_EXIT.grid(row = 0, column = 6, padx = 10, pady = 10)



                            
                            self.scrollbar = Scrollbar(self.Student_Frame_2)
                            self.scrollbar.grid(row = 0, column = 1, sticky = 'ns')

                            self.listbox = Listbox(self.Student_Frame_2, width = 75, height = 20, font = ('arial', 12, 'bold'))
                            self.listbox.bind('<<ListboxSelect>>', Staff_Record)
                            self.listbox.grid(row = 0, column = 0)
                            self.scrollbar.config(command = self.listbox.yview)
                                   
                     information()
                            

       root = Tk()
       obj = Student_Information(root)
       root.mainloop()
def assignment():
    root = Tk()
    root.geometry("1350x550+100+30")
    root.title("Assignment and Notes")
    root.maxsize(width=1350,height=550)
    root.minsize(width=1350,height=550)
    root.config(background="#1A2238")
    root.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
    def open_file():
        file = filedialog.askopenfilename()
        os.startfile(file)
        messagebox.showinfo('open file', file+" opened successfully")


    def delete_file():
        file = filedialog.askopenfilename()
        os.remove(file)
        messagebox.showinfo('delete file', file+" deleted successfully")


    def rename_file():
        global filename, file, f1, path
        file = filedialog.askopenfilename()
        path = os.path.abspath(file)
        f1 = Frame(root, background="grey")
        f1.grid(row=6, column=2)
        Label(f1, text="Enter the file name").grid(row=0, column=1, padx=10, pady=10)
        filename = Entry(f1)
        filename.grid(row=1, column=1, padx=10, pady=10)
        Button(f1, text='Rename file', command=change_name).grid(row=2, column=1, padx=10, pady=10)
        Button(f1, text='cancel', command=f1.destroy).grid(row=2, column=2)
        f1.mainloop()



    def change_name():
        newName = filename.get()
        dir = os.path.dirname(path)
        renamed = os.path.join(dir,newName)
        os.rename(path, renamed)
        f1.destroy()
        messagebox.showinfo('rename file', file + " renamed successfully")


    def deletefolder():
        delFolder = filedialog.askdirectory()
        os.rmdir(delFolder)
        messagebox.showinfo('confirmation', "Folder Deleted !")


    def create_folder():
        global name_entry, dir, f
        dir = filedialog.askdirectory()
        f = Frame(root, background="white")
        f.grid(row=6,column=0)
        Label(f, text="Enter the folder name",bg='white',font="bold").grid(row=0, column=0,padx=10,pady=10)
        name_entry = Entry(f,bd=4,width=25,relief=SUNKEN)
        name_entry.grid(row=1, column=0,padx=10,pady=10)
        Button(f, text='create folder',font="bold",bg='dark green',fg='white', command=makeFolder).grid(row=2, column=0,padx=10,pady=10)
        Button(f, text='cancel',font="bold",bg='red2',fg='white', command=f.destroy).grid(row=2, column=1)
        f.mainloop()


    def makeFolder():
        name = name_entry.get()
        os.chdir(dir)
        os.makedirs(name)
        f.destroy()
        messagebox.showinfo('create folder', " folder created successfully")


    def rename_folder():
        global dir, folder_name, f1,path
        dir = filedialog.askdirectory()
        path = os.path.abspath(dir)
        f1 = Frame(root, background="grey")
        f1.grid(row=6, column=2)
        Label(f1, text="Enter the folder name").grid(row=0, column=1, padx=10, pady=10)
        folder_name = Entry(f1)
        folder_name.grid(row=1, column=1, padx=10, pady=10)
        Button(f1, text='Rename folder', command=change_folder).grid(row=2, column=1, padx=10, pady=10)
        Button(f1, text='cancel', command=f1.destroy).grid(row=2, column=2)
        f1.mainloop()


    def change_folder():
        newName = folder_name.get()
        dir = os.path.dirname(path)
        renamed = os.path.join(dir,newName)
        os.rename(path, renamed)
        f1.destroy()
        messagebox.showinfo('rename folder', path + " renamed successfully")


    def view_folder():
        dir = filedialog.askdirectory()
        f1=Frame(root)
        f1.grid(row=5, column=2)
        listbox = Listbox(f1,width=30)
        listbox.grid(row=0,column=0)
        files = os.listdir(dir)
        for name in files:
            listbox.insert('end', name)
        exit_button = Button(f1, text='Ok', bg='dark green',fg='white',font="bold", command=f1.destroy)
        exit_button.grid(row=1, column=0)


    def copy_move_file():
        global sourceText, destinationText, destination_location, f1
        f1 = Frame(root, width=350, height=300, background="lavender")
        f1.grid(row=5, column=0, columnspan=4)

        source_location = StringVar()
        destination_location = StringVar()

        link_Label = Label(f1, text="Select The File To Copy ", font="bold", bg='lavender')
        link_Label.grid(row=0, column=0, pady=5, padx=5)

        sourceText = Entry(f1, width=50, textvariable=source_location, font="12")
        sourceText.grid(row=0, column=1, pady=5, padx=5)
        source_browseButton = Button(f1, text="Browse",bg='cyan2', command=source_browse, width=15, font="bold")
        source_browseButton.grid(row=0, column=2, pady=5, padx=5)

        destinationLabel = Label(f1, text="Select The Destination", bg="lavender", font="bold")
        destinationLabel.grid(row=1, column=0, pady=5, padx=5)

        destinationText = Entry(f1, width=50, textvariable=destination_location, font=12)
        destinationText.grid(row=1, column=1, pady=5, padx=5)
        dest_browseButton = Button(f1, text="Browse", bg='cyan2', command=destination_browse, width=15, font="12")
        dest_browseButton.grid(row=1, column=2, pady=5, padx=5)

        copyButton = Button(f1, text="Copy File", bg='dark green',fg='white',command=copy_file, width=15, font=('bold',12))
        copyButton.grid(row=2, column=0, pady=10, padx=10)

        moveButton = Button(f1, text="Move File", bg='dark green',fg='white',command=move_file, width=15, font=('bold',12))
        moveButton.grid(row=2, column=1, pady=10, padx=10)

        cancelButton = Button(f1, text="Cancel",bg='red2',fg='white', command= f1.destroy, width=15, font=('bold',12))
        cancelButton.grid(row=2, column=2, pady=10, padx=10)


    def source_browse():
        global files_list
        files_list = list(filedialog.askopenfilenames())
        sourceText.insert('1', files_list)


    def destination_browse():
        destinationdirectory = filedialog.askdirectory()
        destinationText.insert('1', destinationdirectory)


    def copy_file():
        dest_location = destination_location.get()
        for f in files_list:
            shutil.copy(f, dest_location)
        messagebox.showinfo('copy file',"copied successfully")
        f1.destroy()


    def move_file():
        dest_location = destination_location.get()
        for f in files_list:
            shutil.move(f, dest_location)
        messagebox.showinfo('move file',"moved file Successfully")
        f1.destroy()


    lbl_heading = Label(root, text="Assignment and notes",font=('Garamond', 20),fg="White",bg='#FF6A3D')
    lbl_heading.grid(row=1, column=1, pady=20, padx=200)

    open_btn = Button(root, text="Open File",command=open_file, width=15,font=('Garamond', 12,'bold'),bg="#F4DB7D")
    open_btn.grid(row=2, column=0,pady=20, padx=0)

    delete_btn = Button(root, text="Delete File",command=delete_file, width=15,font=('Garamond', 12,'bold'),bg="#F4DB7D")
    delete_btn.grid(row=2, column=1,pady=20, padx=0)

    rename_btn = Button(root, text="Rename File", command=rename_file, width=15,font=('Garamond', 12,'bold'),bg="#F4DB7D")
    rename_btn.grid(row=2, column=2,pady=20, padx=0)

    copy_move_btn = Button(root, text="Copy/Move File", command=copy_move_file, width=15,font=('Garamond', 12,'bold'),bg="#F4DB7D")
    copy_move_btn.grid(row=2, column=3,pady=20, padx=100)

    create_folder_btn = Button(root, text="Create folder", command=create_folder, width=15,font=('Garamond', 12,'bold'),bg="#F4DB7D")
    create_folder_btn.grid(row=3, column=0, pady=20, padx=20)

    deletefolder_btn = Button(root, text="Delete folder", command=deletefolder, width=15,font=('Garamond', 12,'bold'),bg="#F4DB7D")
    deletefolder_btn.grid(row=3, column=1, pady=20, padx=20)

    rename_folder_btn = Button(root, text="Rename Folder", command=rename_folder, width=15,font=('Garamond', 12,'bold'),bg="#F4DB7D")
    rename_folder_btn.grid(row=3, column=2,pady=20, padx=20)

    view_btn = Button(root, text="View folder contents", command=view_folder, width=15,font=('Garamond', 12,'bold'),bg="#F4DB7D")
    view_btn.grid(row=3, column=3, pady=20, padx=20)

    exit_btn = Button(root, text="Exit", command=root.destroy, width=12,font=('Garamond', 12,'bold'),bg="#9DAAF2")
    exit_btn.grid(row=4, column=1, pady=20, padx=100)

    root.mainloop()
def marking_sheet():
    os.system('py College_Marksheet_Frontend.py')
#     root = Tk()
#     root.title('Marksheet')
#     root.geometry('1350x750')
#     root.maxsize(width=1350,height=750)
#     root.minsize(width=1350,height=750)
#     root.config(bg = '#1A2238')
#     root.iconbitmap('C:\Users\Harsh Jajal\Documents\Classverge\Main\Logo.ico')

#     name = StringVar()
#     roll = StringVar()
#     father_name = StringVar()
#     mother_name = StringVar()
#     date_of_birth = StringVar()
#     gender = StringVar()
#     school = StringVar()
#     email_address = StringVar()
#     marks1 = DoubleVar()
#     marks2 = DoubleVar()
#     marks3 = DoubleVar()
#     marks4 = DoubleVar()
#     marks5 = DoubleVar()
#     grand_tot = DoubleVar()
#     percentage = DoubleVar()
#     cgpa = DoubleVar()
#     grade = StringVar()
#     division = StringVar()
#     result = StringVar()



#     def Add():
#             if (len(roll.get()) != 0):
#                     College_Marksheet_Backend.insert(name.get(), roll.get(), father_name.get(), mother_name.get(), date_of_birth.get(), gender.get(), \
#                                                     school.get(), email_address.get(), marks1.get(), marks2.get(), marks3.get(), marks4.get(), marks5.get(), \
#                                                     grand_tot.get(), percentage.get(), cgpa.get(), grade.get(), division.get(), result.get())

#     def Update():
#             if (len(roll.get()) != 0):
#                     College_Marksheet_Backend.update(name.get(), roll.get(), father_name.get(), mother_name.get(), date_of_birth.get(), gender.get(), \
#                                                     school.get(), email_address.get(), marks1.get(), marks2.get(), marks3.get(), marks4.get(), marks5.get(), \
#                                                     grand_tot.get(), percentage.get(), cgpa.get(), grade.get(), division.get(), result.get())
                
#     def Exit():
#             Exit = tkinter.messagebox.askyesno('Marksheet','Confirm if you want to Exit')
#             if Exit > 0:
#                     root.destroy()
#                     return

    
#     def Compute():
#             num1 = (marks1.get());      num2 = (marks2.get());    num3 = (marks3.get());      num4 = (marks4.get());    num5 = (marks5.get())

#             if num1 > 100:
#                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
#                     return
#             if num2 > 100:
#                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
#                     return
#             if num3 > 100:
#                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
#                     return
#             if num4 > 100:
#                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
#                     return
#             if num5 > 100:
#                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
#                     return
                    
    
#             TOTAL = num1+num2+num3+num4+num5
#             grand_tot.set(TOTAL)
            
#             Percentage = ((num1 + num2 + num3 + num4 + num5) * 100) / 500
#             percentage.set(Percentage)


#             c_grades = (((num1+num2+num3+num4+num5) * 100)/500) / 9.5
#             cgpa.set(round(c_grades,1))

#             if c_grades > 10:
#                     cgpa.set(10)


#             if (((num1+num2+num3+num4+num5) * 100)/500) <= 40:
#                     grades = 'G'
#             elif (((num1+num2+num3+num4+num5) * 100)/500) <= 50:
#                     grades = 'F'
#             elif (((num1+num2+num3+num4+num5) * 100)/500) <= 60:
#                     grades = 'E'
#             elif (((num1+num2+num3+num4+num5) * 100)/500) <= 70:
#                     grades = 'D'
#             elif (((num1+num2+num3+num4+num5) * 100)/500) <= 80:
#                     grades = 'C'
#             elif (((num1+num2+num3+num4+num5) * 100)/500) <= 90:
#                     grades = 'B'
#             else:
#                     grades = 'A'

#             grade.set(grades)

#             count = 0
#             if num1 < 33:
#                     count = count + 1
#             if num2 < 33:
#                     count = count + 1
#             if num3 < 33:
#                     count = count + 1
#             if num4 < 33:
#                     count = count + 1
#             if num5 < 33:
#                     count = count + 1

#             if (count == 0):
#                     result.set('PASS')
#             elif (count == 1 or count == 2 ):
#                     result.set('SUPPLY')
#             else:
#                     result.set('FAIL')

#             if Percentage <= 45 and result != "FAIL":
#                     division.set('THIRD')
#             elif Percentage <= 60 and result != "FAIL":
#                     division.set('SECOND')
#             elif Percentage <= 100:
#                     division.set('FIRST')     

#     def Reset():
#             name.set(' ')
#             roll.set(' ')
#             father_name.set(' ')
#             mother_name.set(' ')
#             date_of_birth.set(' ')
#             gender.set(' ')
#             school.set(' ')
#             email_address.set(' ')
#             marks1.set(' ')
#             marks2.set(' ')
#             marks3.set(' ')
#             marks4.set(' ')
#             marks5.set(' ')
#             grand_tot.set(' ')
#             percentage.set(' ')
#             cgpa.set(' ')
#             grade.set(' ')
#             division.set(' ')
#             result.set(' ')  
    

#     #========================================================Marks_Frame_1===============================================================
    
#     Marks_Frame_1 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = '#1A2238', bd = 10, \
#                         text = 'Student Details', fg="#F4DB7D",relief = 'ridge')
#     Marks_Frame_1.grid(row = 1, column = 0, pady = 20, padx = 20)


#     Name_lbl = Label(Marks_Frame_1, text = 'Name', fg="#FF6A3D",font = ('arial',15,'bold'), bg = '#1A2238')
#     Name_lbl.grid(row = 0, column = 0, padx = 80)
#     Name_TxtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = name)
#     Name_TxtEntry.grid(row = 0, column = 1, padx = 5, pady = 5)

#     RollNumber_lbl = Label(Marks_Frame_1, text = 'Roll Number',fg="#FF6A3D", font = ('arial',15,'bold'), bg = '#1A2238')
#     RollNumber_lbl.grid(row = 0, column = 3, padx = 80)
#     RollNumber_TxtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = roll)
#     RollNumber_TxtEntry.grid(row = 0, column = 4, padx = 40)

#     fname_lbl = Label(Marks_Frame_1, text = 'Father Name',fg="#FF6A3D", font = ('arial',15,'bold'), bg = '#1A2238')
#     fname_lbl.grid(row = 1, column = 0, padx = 80)
#     fname_txtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = father_name)
#     fname_txtEntry.grid(row = 1, column = 1, padx = 5, pady = 10)

#     mname_lbl = Label(Marks_Frame_1, text = 'Mother Name',fg="#FF6A3D", font = ('arial',15,'bold'), bg = '#1A2238')
#     mname_lbl.grid(row = 1, column = 3, padx = 80)
#     mname_txtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = mother_name)
#     mname_txtEntry.grid(row = 1, column = 4, padx = 5)

#     dateOFbirth_lbl = Label(Marks_Frame_1, text = 'Date of Birth',fg="#FF6A3D", font = ('arial',15,'bold'), bg = '#1A2238')
#     dateOFbirth_lbl.grid(row = 2, column = 0, padx = 80)
#     dateOFbirth_txtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = date_of_birth)
#     dateOFbirth_txtEntry.grid(row = 2, column = 1, padx = 5, pady = 5)

#     gender_lbl = Label(Marks_Frame_1, text = 'Gender',fg="#FF6A3D",font = ('arial',15,'bold'), bg = '#1A2238')
#     gender_lbl.grid(row = 2, column = 3, padx = 80)
#     gender_txtEntry = ttk.Combobox(Marks_Frame_1, values = (' ','Male','Female','Others'), font = ('arial',15), width = 23, textvariable = gender)
#     gender_txtEntry.grid(row = 2, column = 4, padx = 5, pady = 5)


#     school_lbl = Label(Marks_Frame_1, text = 'Email ID',fg="#FF6A3D", font = ('arial',15,'bold'), bg = '#1A2238')
#     school_lbl.grid(row = 3, column = 0, padx = 80)
#     school_txtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = school)
#     school_txtEntry.grid(row = 3, column = 1, padx = 5, pady = 5)


#     Marks_Frame_2 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = '#1A2238', bd = 10 \
#                         , text = 'Grades Point Obtained',fg="#F4DB7D", relief = 'ridge')
#     Marks_Frame_2.grid(row = 3, column = 0)

#     cl =Label(root,text="CLASS",fg="#F4DB7D",bg="#1A2238",font = ('Times New Roman',32,'bold'))
#     cl.place(x=500,y=690)
#     cl2 =Label(root,text="VERGE",fg="White",bg="#1A2238",font = ('Times New Roman',32,'bold'))
#     cl2.place(x=640,y=690)



#     subject_lbl = Label(Marks_Frame_2, text = 'SUBJECT',fg="#9DAAF2", font = ('arial',16,'bold'), bg = '#1A2238')
#     subject_lbl.grid(row = 3, column = 0, padx = 50, pady = 10)

#     marks_obtained_lbl = Label(Marks_Frame_2, text = 'MARKS OBTAINED',fg="#9DAAF2", font = ('arial',16,'bold'), bg = '#1A2238')
#     marks_obtained_lbl.grid(row = 3, column = 1, padx = 20)

#     subject_lbl = Label(Marks_Frame_2, text = 'PASSING MARKS',fg="#9DAAF2", font = ('arial',16,'bold'), bg = '#1A2238')
#     subject_lbl.grid(row = 3, column = 2, padx = 20)

#     marks_obtained_lbl = Label(Marks_Frame_2, text = 'TOTAL MARKS',fg="#9DAAF2", font = ('arial',16,'bold'), bg = '#1A2238')
#     marks_obtained_lbl.grid(row = 3, column = 3, padx = 20)

#     MATHEMATICS_lbl1 = Label(Marks_Frame_2, text = 'MATHEMATICS',fg="#FF6A3D", font = ('arial',14), bg = '#1A2238')
#     MATHEMATICS_lbl1.grid(row = 4, column = 0)
#     CNND = Label(Marks_Frame_2, text = 'CNND',fg="#FF6A3D", font = ('arial',14), bg = '#1A2238')
#     CNND.grid(row = 5, column = 0)
#     OS = Label(Marks_Frame_2, text = 'OS',fg="#FF6A3D", font = ('arial',14), bg = '#1A2238')
#     OS.grid(row = 6, column = 0)
#     AT = Label(Marks_Frame_2, text = 'AT',fg="#FF6A3D", font = ('arial',14), bg = '#1A2238')
#     AT.grid(row = 7, column = 0)
#     COA = Label(Marks_Frame_2, text = 'COA',fg="#FF6A3D", font = ('arial',14), bg = '#1A2238')
#     COA.grid(row = 8, column = 0)
#     GRAND_TOTAL_lbl6 = Label(Marks_Frame_2, text = 'GRAND TOTAL',fg="#9DAAF2", font = ('arial',16), bg = '#1A2238')
#     GRAND_TOTAL_lbl6.grid(row = 9, column = 0)
#     PERCENTAGE_lbl7 = Label(Marks_Frame_2, text = 'PERCENTAGE',fg="#9DAAF2", font = ('arial',16,'bold'), bg = '#1A2238')
#     PERCENTAGE_lbl7.grid(row = 10, column = 0)
#     CGPA_lbl8 = Label(Marks_Frame_2, text = 'CGPA',fg="#9DAAF2", font = ('arial',16,'bold'), bg = '#1A2238')
#     CGPA_lbl8.grid(row = 10, column = 2)
#     GRADE_lbl9 = Label(Marks_Frame_2, text = 'GRADE',fg="#9DAAF2", font = ('arial',16,'bold'), bg = '#1A2238')
#     GRADE_lbl9.grid(row = 10, column = 4)
#     DIVISION_lbl10 = Label(Marks_Frame_2, text = 'DIVISION',fg="#9DAAF2", font = ('arial',16,'bold'), bg = '#1A2238')
#     DIVISION_lbl10.grid(row = 11, column = 0)
#     DIVISION_lbl10 = Label(Marks_Frame_2, text = 'RESULT',fg="#9DAAF2", font = ('arial',16,'bold'), bg = '#1A2238')
#     DIVISION_lbl10.grid(row = 11, column = 2)
    

#     variables_1 = StringVar(Marks_Frame_2, value = '33')
#     variables_2 = StringVar(Marks_Frame_2, value = '100')
#     variables_3 = StringVar(Marks_Frame_2, value = '500')

#     Text_Entry1 = Entry(Marks_Frame_2, font = ('arial',16), width = 5, textvariable = marks1)
#     Text_Entry1.grid(row = 4, column = 1)
#     Text_Entry2 = Entry(Marks_Frame_2, font = ('arial',16), width = 5, textvariable = marks2)
#     Text_Entry2.grid(row = 5, column = 1)
#     Text_Entry3 = Entry(Marks_Frame_2, font = ('arial',16), width = 5, textvariable = marks3)
#     Text_Entry3.grid(row = 6, column = 1)
#     Text_Entry4 = Entry(Marks_Frame_2, font = ('arial',16), width = 5, textvariable = marks4)
#     Text_Entry4.grid(row = 7, column = 1)
#     Text_Entry5 = Entry(Marks_Frame_2, font = ('arial',16), width = 5, textvariable = marks5)
#     Text_Entry5.grid(row = 8, column = 1)
#     Text_Entry6 = Entry(Marks_Frame_2, font = ('arial',14), width = 5, textvariable = grand_tot, state = 'readonly')
#     Text_Entry6.grid(row = 9, column = 1, pady = 8)
#     Text_Entry7 = Entry(Marks_Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = percentage, state = 'readonly')
#     Text_Entry7.grid(row = 10, column = 1, pady = 8)
#     Text_Entry8 = Entry(Marks_Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = cgpa, state = 'readonly')
#     Text_Entry8.grid(row = 10, column = 3, pady = 8)
#     Text_Entry9 = Entry(Marks_Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = grade, state = 'readonly')
#     Text_Entry9.grid(row = 10, column = 5, padx = 20, pady = 8)
#     Text_Entry10 = Entry(Marks_Frame_2, font = ('arial',14,'bold'), width = 8, textvariable = division, state = 'readonly')
#     Text_Entry10.grid(row = 11, column = 1, padx = 20, pady = 8)
#     Text_Entry11 = Entry(Marks_Frame_2, font = ('arial',14,'bold'), width = 7, textvariable = result, state = 'readonly')
#     Text_Entry11.grid(row = 11, column = 3, padx = 20, pady = 8)
    
#     Text_Entry_1_2 = Entry(Marks_Frame_2, textvariable = variables_1, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_1_2.grid(row = 4, column = 2, pady = 5)
#     Text_Entry_1_3 = Entry(Marks_Frame_2, textvariable = variables_2, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_1_3.grid(row = 4, column = 3)
#     Text_Entry_2_2 = Entry(Marks_Frame_2, textvariable = variables_1, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_2_2.grid(row = 5, column = 2, pady = 5)
#     Text_Entry_2_3 = Entry(Marks_Frame_2, textvariable = variables_2, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_2_3.grid(row = 5, column = 3)
#     Text_Entry_3_2 = Entry(Marks_Frame_2, textvariable = variables_1, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_3_2.grid(row = 6, column = 2, pady = 5)
#     Text_Entry_3_3 = Entry(Marks_Frame_2, textvariable = variables_2, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_3_3.grid(row = 6, column = 3)
#     Text_Entry_4_2 = Entry(Marks_Frame_2, textvariable = variables_1, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_4_2.grid(row = 7, column = 2, pady = 5)
#     Text_Entry_4_3 = Entry(Marks_Frame_2, textvariable = variables_2, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_4_3.grid(row = 7, column = 3)
#     Text_Entry_5_2 = Entry(Marks_Frame_2, textvariable = variables_1, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_5_2.grid(row = 8, column = 2, pady = 5)
#     Text_Entry_5_3 = Entry(Marks_Frame_2, textvariable = variables_2, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_5_3.grid(row = 8, column = 3)
#     Text_Entry_6_3 = Entry(Marks_Frame_2, textvariable = variables_3, font = ('arial',16), width = 5, state = 'readonly')
#     Text_Entry_6_3.grid(row = 9, column = 3)
            



#     Compute_button = Button(Marks_Frame_2, text = 'COMPUTE', font = ('arial',12,'bold'),bg="#9DAAF2",fg = 'Black', width = 10, command = Compute)
#     Compute_button.grid(row = 4, column = 4, padx = 50, pady = 6)
#     Save_button = Button(Marks_Frame_2, text = 'SAVE', font = ('arial',12,'bold'),bg="#9DAAF2",fg = 'Black', width = 10, command = Add)
#     Save_button.grid(row = 5, column = 4, padx = 50, pady = 6)
#     Update_button = Button(Marks_Frame_2, text = 'UPDATE', font = ('arial',12,'bold'),bg="#9DAAF2",fg = 'Black', width = 10, command = Update)
#     Update_button.grid(row = 6, column = 4, padx = 50, pady = 6)
#     Cancel_button = Button(Marks_Frame_2, text = 'RESET', font = ('arial',12,'bold'),bg="#9DAAF2",fg = 'Black', width = 10, command = Reset)
#     Cancel_button.grid(row = 7, column = 4, padx = 50, pady = 6)
#     Exit_button = Button(Marks_Frame_2, text = 'EXIT', font = ('arial',12,'bold'),bg="#9DAAF2",fg = 'Black', width = 10, command = Exit)
#     Exit_button.grid(row = 8, column = 4, padx = 50, pady = 6)


#     root.mainloop()


# def search_result_marksheet(row):
#     root = Tk()
#     root.title('Marksheet')
#     root.geometry('1350x750')
#     root.config(bg = '#1A2238')

    

    
#     def Compute():
#             num1 = (marks1.get());      num2 = (marks2.get());    num3 = (marks3.get());      num4 = (marks4.get());    num5 = (marks5.get())                                   
    
#             TOTAL = num1+num2+num3+num4+num5
#             grand_tot.set(TOTAL)
            
#             Percentage = ((num1+num2+num3+num4+num5) * 100)/500
#             percentage.set(Percentage)


#             c_grades = (((num1+num2+num3+num4+num5) * 100)/500) / 9.5
#             cgpa.set(round(c_grades,1))


#             if (((num1+num2+num3+num4+num5) * 100)/500) <= 40:
#                     grades = 'G'
#             elif (((num1+num2+num3+num4+num5) * 100)/500) <= 50:
#                     grades = 'F'
#             elif (((num1+num2+num3+num4+num5) * 100)/500) <= 60:
#                     grades = 'E'
#             elif (((num1+num2+num3+num4+num5) * 100)/500) <= 70:
#                     grades = 'D'
#             elif (((num1+num2+num3+num4+num5) * 100)/500) <= 80:
#                     grades = 'C'
#             elif (((num1+num2+num3+num4+num5) * 100)/500) <= 90:
#                     grades = 'B'
#             else:
#                     grades = 'A'

#             grade.set(grades)

#             count = 0
#             if num1 < 33:
#                     count = count + 1
#             if num2 < 33:
#                     count = count + 1
#             if num3 < 33:
#                     count = count + 1
#             if num4 < 33:
#                     count = count + 1
#             if num5 < 33:
#                     count = count + 1

#             if (count == 0):
#                     result.set('PASS')
#             elif (count == 1 or count == 2 ):
#                     result.set('SUPPLY')
#             else:
#                     result.set('FAIL')

#             if Percentage <= 45 and result != "FAIL":
#                     div.set('THIRD')
#             elif Percentage <= 60 and result != "FAIL":
#                     div.set('SECOND')
#             elif Percentage <= 100:
#                     div.set('FIRST')     

    
    


    
#     Frame_1 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = '#1A2238', bd = 10, \
#                         text = 'Student Details', relief = 'ridge')
#     Frame_1.grid(row = 1, column = 0, pady = 20, padx = 20)

#     name = StringVar(Frame_1,value=row[0][1])
#     roll = StringVar(Frame_1,value=row[0][2])
#     father_name = StringVar(Frame_1,value=row[0][3])
#     mother_name = StringVar(Frame_1,value=row[0][4])
#     date_of_birth = StringVar(Frame_1,value=row[0][5])
#     gender = StringVar(Frame_1,value=row[0][6])
#     school = StringVar(Frame_1,value=row[0][7])
#     email_addres = StringVar(Frame_1,value=row[0][8])
    



#     lbl_name = Label(Frame_1, text = 'Name', font = ('arial',15,'bold'), bg = '#1A2238')
#     lbl_name.grid(row = 0, column = 0, padx = 80)
#     Txt_Entry_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = name)
#     Txt_Entry_Name.grid(row = 0, column = 1, padx = 5, pady = 5)

#     Lbl_Roll_no = Label(Frame_1, text = 'Roll Number', font = ('arial',15,'bold'), bg = '#1A2238')
#     Lbl_Roll_no.grid(row = 0, column = 3, padx = 80)
#     Txt_Entry_Roll_no = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = roll)
#     Txt_Entry_Roll_no.grid(row = 0, column = 4, padx = 40)

#     Llb_Father_Name = Label(Frame_1, text = 'Father Name', font = ('arial',15,'bold'), bg = '#1A2238')
#     Llb_Father_Name.grid(row = 1, column = 0, padx = 80)
#     Txt_Entry_Father_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = father_name)
#     Txt_Entry_Father_Name.grid(row = 1, column = 1, padx = 5, pady = 10)

#     Lbl_Mother_Name = Label(Frame_1, text = 'Mother Name', font = ('arial',15,'bold'), bg = '#1A2238')
#     Lbl_Mother_Name.grid(row = 1, column = 3, padx = 80)
#     Txt_Entry_Mother_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = mother_name)
#     Txt_Entry_Mother_Name.grid(row = 1, column = 4, padx = 5)

#     lbl_DateOFbirth = Label(Frame_1, text = 'Date of Birth', font = ('arial',15,'bold'), bg = '#1A2238')
#     lbl_DateOFbirth.grid(row = 2, column = 0, padx = 80)
#     Txt_Entry_DateOFbirth = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = date_of_birth)
#     Txt_Entry_DateOFbirth.grid(row = 2, column = 1, padx = 5, pady = 5)

#     Lbl_Gender = Label(Frame_1, text = 'Gender', font = ('arial',15,'bold'), bg = '#1A2238')
#     Lbl_Gender.grid(row = 2, column = 3, padx = 80)
#     TXt_Entry_Gender = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = gender)
#     TXt_Entry_Gender.grid(row = 2, column = 4, padx = 5, pady = 5)


#     Lbl_School = Label(Frame_1, text = 'School Name', font = ('arial',15,'bold'), bg = '#1A2238')
#     Lbl_School.grid(row = 3, column = 0, padx = 80)
#     Txt_Entry_School = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = school)
#     Txt_Entry_School.grid(row = 3, column = 1, padx = 5, pady = 5)

#     Lbl_EmailAddress = Label(Frame_1, text = 'Email Address', font = ('arial',15,'bold'), bg = '#1A2238')
#     Lbl_EmailAddress.grid(row = 3, column = 3, padx = 80)
#     Txt_Entry_EmailAddress = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = email_addres)
#     Txt_Entry_EmailAddress.grid(row = 3, column = 4, padx = 5, pady = 5)



#     Frame_2 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = '#1A2238', bd = 10 \
#                         , text = 'Grades Point Obtained', relief = 'ridge')
#     Frame_2.grid(row = 3, column = 0)

#     marks1 = DoubleVar(Frame_2,row[0][9])
#     marks2 = DoubleVar(Frame_2,row[0][10])
#     marks3 = DoubleVar(Frame_2,row[0][11])
#     marks4 = DoubleVar(Frame_2,row[0][12])
#     marks5 = DoubleVar(Frame_2,row[0][13])
#     grand_tot = DoubleVar(Frame_2,row[0][14])
#     percentage = DoubleVar(Frame_2,row[0][15])
#     cgpa = DoubleVar(Frame_2,row[0][16])
#     grade = StringVar(Frame_2,row[0][17])
#     div = StringVar(Frame_2,row[0][18])
#     result = StringVar(Frame_2,row[0][19])



#     Lbl_Sub = Label(Frame_2, text = 'SUBJECT', font = ('arial',16,'bold'), bg = '#1A2238')
#     Lbl_Sub.grid(row = 3, column = 0, padx = 50, pady = 10)

#     Lbl_obtained_Marks = Label(Frame_2, text = 'MARKS OBTAINED', font = ('arial',16,'bold'), bg = '#1A2238')
#     Lbl_obtained_Marks.grid(row = 3, column = 1, padx = 20)

#     Lbl_Sub = Label(Frame_2, text = 'PASSING MARKS', font = ('arial',16,'bold'), bg = '#1A2238')
#     Lbl_Sub.grid(row = 3, column = 2, padx = 20)

#     Lbl_obtained_Marks = Label(Frame_2, text = 'TOTAL MARKS', font = ('arial',16,'bold'), bg = '#1A2238')
#     Lbl_obtained_Marks.grid(row = 3, column = 3, padx = 20)

#     MATHEMATICS_lbl1 = Label(Frame_2, text = 'MATHEMATICS', font = ('arial',14), bg = '#1A2238')
#     MATHEMATICS_lbl1.grid(row = 4, column = 0)
#     CNND = Label(Frame_2, text = 'PHYSICS', font = ('arial',14), bg = '#1A2238')
#     CNND.grid(row = 5, column = 0)
#     OS = Label(Frame_2, text = 'CHEMISTRY', font = ('arial',14), bg = '#1A2238')
#     OS.grid(row = 6, column = 0)
#     AT = Label(Frame_2, text = 'PROGRAMMING', font = ('arial',14), bg = '#1A2238')
#     AT.grid(row = 7, column = 0)
#     COA = Label(Frame_2, text = 'ENGLISH', font = ('arial',14), bg = '#1A2238')
#     COA.grid(row = 8, column = 0)
#     GRAND_TOTAL_lbl6 = Label(Frame_2, text = 'GRAND TOTAL', font = ('arial',16), bg = '#1A2238')
#     GRAND_TOTAL_lbl6.grid(row = 9, column = 0)
#     PERCENTAGE_lbl7 = Label(Frame_2, text = 'PERCENTAGE', font = ('arial',16,'bold'), bg = '#1A2238')
#     PERCENTAGE_lbl7.grid(row = 10, column = 0)
#     CGPA_lbl8 = Label(Frame_2, text = 'CGPA', font = ('arial',16,'bold'), bg = '#1A2238')
#     CGPA_lbl8.grid(row = 10, column = 2)
#     GRADE_lbbl9 = Label(Frame_2, text = 'GRADE', font = ('arial',16,'bold'), bg = '#1A2238')
#     GRADE_lbbl9.grid(row = 10, column = 4)
#     DIVISIONRESULT_lbl10 = Label(Frame_2, text = 'DIVISION', font = ('arial',16,'bold'), bg = '#1A2238')
#     DIVISIONRESULT_lbl10.grid(row = 11, column = 0)
#     DIVISIONRESULT_lbl10 = Label(Frame_2, text = 'RESULT', font = ('arial',16,'bold'), bg = '#1A2238')
#     DIVISIONRESULT_lbl10.grid(row = 11, column = 2)
    

#     variables_1 = StringVar(Frame_2, value = '33')
#     variables_2 = StringVar(Frame_2, value = '100')
#     variables_3 = StringVar(Frame_2, value = '500')

#     Text_Entry1 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = marks1)
#     Text_Entry1.grid(row = 4, column = 1)
#     Text_Entry2 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = marks2)
#     Text_Entry2.grid(row = 5, column = 1)
#     Text_Entry3 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = marks3)
#     Text_Entry3.grid(row = 6, column = 1)
#     Text_Entry4 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = marks4)
#     Text_Entry4.grid(row = 7, column = 1)
#     Text_Entry5 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = marks5)
#     Text_Entry5.grid(row = 8, column = 1)
#     Text_Entry6 = Entry(Frame_2, font = ('arial',14), width = 5, textvariable = grand_tot)
#     Text_Entry6.grid(row = 9, column = 1, pady = 8)
#     Text_Entry7 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = percentage)
#     Text_Entry7.grid(row = 10, column = 1, pady = 8)
#     Text_Entry8 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = cgpa)
#     Text_Entry8.grid(row = 10, column = 3, pady = 8)
#     Text_Entry9 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = grade)
#     Text_Entry9.grid(row = 10, column = 5, padx = 20, pady = 8)
#     Text_Entry10 = Entry(Frame_2, font = ('arial',14,'bold'), width = 8, textvariable = div)
#     Text_Entry10.grid(row = 11, column = 1, padx = 20, pady = 8)
#     Text_Entry11 = Entry(Frame_2, font = ('arial',14,'bold'), width = 7, textvariable = result)
#     Text_Entry11.grid(row = 11, column = 3, padx = 20, pady = 8)
    
#     Text_Entry_1_2 = Entry(Frame_2, textvariable = variables_1, font = ('arial',16), width = 5)
#     Text_Entry_1_2.grid(row = 4, column = 2, pady = 5)
#     Text_Entry_1_3 = Entry(Frame_2, textvariable = variables_2, font = ('arial',16), width = 5)
#     Text_Entry_1_3.grid(row = 4, column = 3)
#     Text_Entry_2_2 = Entry(Frame_2, textvariable = variables_1, font = ('arial',16), width = 5)
#     Text_Entry_2_2.grid(row = 5, column = 2, pady = 5)
#     Text_Entry_2_3 = Entry(Frame_2, textvariable = variables_2, font = ('arial',16), width = 5)
#     Text_Entry_2_3.grid(row = 5, column = 3)
#     Text_Entry_3_2 = Entry(Frame_2, textvariable = variables_1, font = ('arial',16), width = 5)
#     Text_Entry_3_2.grid(row = 6, column = 2, pady = 5)
#     Text_Entry_3_3 = Entry(Frame_2, textvariable = variables_2, font = ('arial',16), width = 5)
#     Text_Entry_3_3.grid(row = 6, column = 3)
#     Text_Entry_4_2 = Entry(Frame_2, textvariable = variables_1, font = ('arial',16), width = 5)
#     Text_Entry_4_2.grid(row = 7, column = 2, pady = 5)
#     Text_Entry_4_3 = Entry(Frame_2, textvariable = variables_2, font = ('arial',16), width = 5)
#     Text_Entry_4_3.grid(row = 7, column = 3)
#     Text_Entry_5_2 = Entry(Frame_2, textvariable = variables_1, font = ('arial',16), width = 5)
#     Text_Entry_5_2.grid(row = 8, column = 2, pady = 5)
#     Text_Entry_5_3 = Entry(Frame_2, textvariable = variables_2, font = ('arial',16), width = 5)
#     Text_Entry_5_3.grid(row = 8, column = 3)
#     Text_Entry_6_3 = Entry(Frame_2, textvariable = variables_3, font = ('arial',16), width = 5)
#     Text_Entry_6_3.grid(row = 9, column = 3)
            


    
    
#     Exit_button = Button(Frame_2, text = 'EXIT', font = ('arial',12,'bold'), width = 10, command = root.destroy)
#     Exit_button.grid(row = 8, column = 4, padx = 50, pady = 6)

    
#     root.mainloop()

    # if __name__ == '__main__':
    #     marking_sheet()
def manage_fees():
    os.system('py College-Management_System\College_Fee_Frontend.py')
    
    # class college_fee():
    #     def __init__(self, master):
    #         self.master = master
    #         self.master.title('Fee Report')
    #         self.master.geometry('1350x750')
    #         self.master.minsize(width=1350,height=750)
    #         self.master.maxsize(width=1350,height=750)
    #         self.master.config(bg='#1A2238')
    #         self.master.iconbitmap('C:\Users\Harsh Jajal\Documents\Classverge\Main\Logo.ico')

    #         self.receipts = StringVar()
    #         self.name = StringVar()
    #         self.admin = StringVar()
    #         self.date = StringVar()
    #         self.branch = StringVar()
    #         self.semister = StringVar()
    #         self.total = DoubleVar()
    #         self.paid = DoubleVar()
    #         self.due = DoubleVar()


    #         def Tuple(event):
    #             try:
    #                 global studentInfo
    #                 index = self.list.curselection()[0]
    #                 studentInfo = self.list.get(index)

    #                 self.receipts_entry.delete(0, END)
    #                 self.receipts_entry.insert(END, studentInfo[1])
    #                 self.studentname_entry.delete(0, END)
    #                 self.studentname_entry.insert(END, studentInfo[2])
    #                 self.collegeAdmin_entry.delete(0, END)
    #                 self.collegeAdmin_entry.insert(END, studentInfo[3])
    #                 self.Date_entry.delete(0, END)
    #                 self.Date_entry.insert(END, studentInfo[4])
    #                 self.collegeBranch_entry.delete(0, END)
    #                 self.collegeBranch_entry.insert(END, studentInfo[5])
    #                 self.semister_entry.delete(0, END)
    #                 self.semister_entry.insert(END, studentInfo[6])
    #                 self.tot_entry.delete(0, END)
    #                 self.tot_entry.insert(END, studentInfo[7])
    #                 self.moneyPaid_entry.delete(0, END)
    #                 self.moneyPaid_entry.insert(END, studentInfo[8])
    #                 self.studdenDdue_entry.delete(0, END)
    #                 self.studdenDdue_entry.insert(END, studentInfo[9])
    #             except IndexError:
    #                 pass

    #         def Insert():
    #             if (len(self.admin.get()) != 0):
    #                 College_Fee_Backend.insert(self.receipts.get(), self.name.get(), self.admin.get(), self.date.get(),
    #                                         self.branch.get(), self.semister.get(), self.total.get(), self.paid.get(),
    #                                         self.due.get())
    #                 self.list.delete(0, END)
    #                 self.list.insert(END, (self.receipts.get(), self.name.get(), self.admin.get(), self.date.get(),
    #                                     self.branch.get(), self.semister.get(), self.total.get(), self.paid.get(),
    #                                     self.due.get()))

    #         def View():
    #             self.list.delete(0, END)
    #             for row in College_Fee_Backend.view():
    #                 self.list.insert(END, row, str(' '))

    #         def Reset():
    #             self.receipts.set(' ')
    #             self.name.set(' ')
    #             self.admin.set(' ')
    #             #self.date.set(' ')
    #             self.branch.set(' ')
    #             self.semister.set(' ')
    #             self.paid.set(' ')
    #             self.due.set(' ')
    #             self.Display.delete('1.0', END)
    #             self.list.delete(0, END)

    #         def Delete():
    #             College_Fee_Backend.delete(studentInfo[0])
    #             Reset()
    #             View()

    #         def Receipt():
    #             self.Display.delete('1.0', END)
    #             self.Display.insert(END, '\t\tRECEIPT' + '\n\n')
    #             self.Display.insert(
    #                 END, '\tReceipt No.\t     :' + self.receipts.get() + '\n')
    #             self.Display.insert(END, '\tStudent Name  :' +
    #                                 self.name.get() + '\n')
    #             self.Display.insert(END, '\tAdmission No.\t:' +
    #                                 self.admin.get() + '\n')
    #             self.Display.insert(
    #                 END, '\tDate\t          :' + self.date.get() + '\n')
    #             self.Display.insert(
    #                 END, '\tBranch\t          :' + self.branch.get() + '\n')
    #             self.Display.insert(
    #                 END, '\tSemester \t        :' + self.semister.get() + '\n\n')

    #             x1 = (self.var_1.get())
    #             x2 = (self.paid.get())
    #             x3 = (x1 - x2)

    #             self.Display.insert(END, '\tTotal Amount  :' + str(x1) + '\n')
    #             self.Display.insert(END, '\tPaid Amount   :' + str(x2) + '\n')
    #             self.Display.insert(END, '\tBalance\t         :' + str(x3) + '\n')

    #             self.due.set(x3)

    #         def Search():
    #             self.list.delete(0, END)
    #             for row in College_Fee_Backend.search(self.receipts.get(), self.name.get(), self.admin.get(), self.date.get(),
    #                                                 self.branch.get(), self.semister.get(), self.total.get(), self.paid.get(),
    #                                                 self.due.get()):
    #                 self.list.insert(END, row, str(' '))

    #         def Update():
    #             College_Fee_Backend.delete(studentInfo[0])
    #             Insert()

    #         def Exit():
    #             Exit = tkinter.messagebox.askyesno(
    #                 'Attention', 'Confirm, if you want to Exit')
    #             if Exit > 0:
    #                 root.destroy()
    #                 return


    #         College_Main_Frame = Frame(self.master, bg='#1A2238')
    #         College_Main_Frame.grid()

    #         College_Title_Frame = LabelFrame(
    #             College_Main_Frame, width=1350, height=100, bg='#1A2238', relief='ridge', bd=15)
    #         College_Title_Frame.pack(side=TOP)

    #         self.lblTitle = Label(College_Title_Frame,bg="#1A2238",fg="#FF6A3D" ,font=('Times New Roman', 32, 'bold'), text='FEE REPORT',padx=13)
    #         self.lblTitle.grid(padx=200)
    #         # cl =Label(College_Title_Frame,text="CLASS",fg="#F4DB7D",bg="#1A2238",font = ('Times New Roman',32,'bold'))
    #         # cl.place(x=630,y=0)
    #         # cl2 =Label(College_Title_Frame,text="VERGE",fg="White",bg="#1A2238",font = ('Times New Roman',32,'bold'))
    #         # cl2.place(x=770,y=00)
    #         College_Data_Frame = Frame(College_Main_Frame, width=1350, height=350,
    #                         bg='#1A2238', relief='ridge', bd=15)
    #         College_Data_Frame.pack(side=TOP, padx=15)

    #         College_Frame_1 = LabelFrame(College_Data_Frame, width=850, height=350, bg='#1A2238', relief='ridge', bd=8,
    #                             text='Informations',fg="#F4DB7D", font=('arial', 15, 'bold'))
    #         College_Frame_1.pack(side=LEFT, padx=10)

    #         College_Frame_2 = LabelFrame(College_Data_Frame, width=495, height=350, bg='#1A2238', relief='ridge', bd=8,
    #                             text='Fee Receipt',fg="#F4DB7D", font=('arial', 15, 'bold'))
    #         College_Frame_2.pack(side=RIGHT, padx=10)

    #         College_List_Frame = Frame(College_Main_Frame, width=1350, height=150,
    #                         bg='#1A2238', relief='ridge', bd=15)
    #         College_List_Frame.pack(side=TOP, padx=15)

    #         Btn_Frame = Frame(College_Main_Frame, width=1350, height=80,
    #                         bg='#1A2238', relief='ridge', bd=15)
    #         Btn_Frame.pack(side=TOP)


    #         self.receipts_lbl = Label(College_Frame_1, text='Receipt No. : ', font=(
    #             'arial', 14, 'bold'),fg="#FF6A3D",  bg='#1A2238')
    #         self.receipts_lbl.grid(row=0, column=0, padx=15, sticky=W)

    #         self.studentName_lbl = Label(College_Frame_1, text='Student Name : ', font=(
    #             'arial', 14, 'bold'),fg="#FF6A3D",  bg='#1A2238')
    #         self.studentName_lbl.grid(row=1, column=0, padx=15, sticky=W)

    #         self.collegeAdmin_lbl = Label(College_Frame_1, text='Admission No. : ', font=(
    #             'arial', 14, 'bold'),fg="#FF6A3D",  bg='#1A2238')
    #         self.collegeAdmin_lbl.grid(row=2, column=0, padx=15, sticky=W)

    #         self.Date_lbl = Label(College_Frame_1, text='Date : ', font=(
    #             'arial', 14, 'bold'),fg="#FF6A3D",  bg='#1A2238')
    #         self.Date_lbl.grid(row=3, column=0, padx=15, sticky=W)

    #         self.college_branch_lbl = Label(College_Frame_1, text='Branch : ', font=(
    #             'arial', 14, 'bold'),fg="#FF6A3D",  bg='#1A2238')
    #         self.college_branch_lbl.grid(row=4, column=0, padx=15, sticky=W)

    #         self.semister_lbl = Label(College_Frame_1, text='Semester : ', font=(
    #             'arial', 14, 'bold'),fg="#FF6A3D",  bg='#1A2238')
    #         self.semister_lbl.grid(row=5, column=0, padx=15, sticky=W)

    #         self.total_lbl = Label(College_Frame_1, text='TOTAL AMOUNT : ', font=(
    #             'arial', 14, 'bold'),fg="#FF6A3D",  bg='#1A2238')
    #         self.total_lbl.grid(row=2, column=2, padx=5, sticky=W)

    #         self.paid_lbl = Label(College_Frame_1, text='PAID AMOUNT : ', font=(
    #             'arial', 14, 'bold'),fg="#FF6A3D",  bg='#1A2238')
    #         self.paid_lbl.grid(row=3, column=2, padx=5, sticky=W)

    #         self.due_lbl = Label(College_Frame_1, text='BALANCE : ', font=(
    #             'arial', 14, 'bold'),fg="#FF6A3D",  bg='#1A2238')
    #         self.due_lbl.grid(row=4, column=2, padx=5, sticky=W)


    #         self.var_1 = DoubleVar(College_Frame_1, value='1,50,000')
    #         d1 = datetime.date.today()
    #         self.date.set(d1)

    #         self.receipts_entry = Entry(College_Frame_1, font=(
    #             'arial', 14), textvariable=self.receipts)
    #         self.receipts_entry.grid(row=0, column=1, padx=15, pady=5)

    #         self.studentname_entry = Entry(College_Frame_1, font=(
    #             'arial', 14), textvariable=self.name)
    #         self.studentname_entry.grid(row=1, column=1, padx=15, pady=5)

    #         self.collegeAdmin_entry = Entry(College_Frame_1, font=(
    #             'arial', 14), textvariable=self.admin)
    #         self.collegeAdmin_entry.grid(row=2, column=1, padx=15, pady=5)

    #         self.Date_entry = Entry(College_Frame_1, font=(
    #             'arial', 14), textvariable=self.date)
    #         self.Date_entry.grid(row=3, column=1, padx=15, pady=5)

    #         self.collegeBranch_entry = ttk.Combobox(College_Frame_1, values=(' ', 'CSE', 'IT', 'ETC/ET&T', 'Mechanical Engineer', 'Civil Engineer', 'IT/CT', 'Electrical Engineer'),
    #                                                 font=('arial', 14), width=19, textvariable=self.branch)
    #         self.collegeBranch_entry.grid(row=4, column=1, padx=15, pady=5)

    #         self.semister_entry = ttk.Combobox(College_Frame_1, values=(' ', 'FIRST', 'SECOND', 'THIRD'), font=('arial', 14), width=19,
    #                                         textvariable=self.semister)
    #         self.semister_entry.grid(row=5, column=1, padx=15, pady=5)

    #         self.tot_entry = Entry(College_Frame_1, font=(
    #             'arial', 14), width=10, textvariable=self.var_1, state='readonly')
    #         self.tot_entry.grid(row=2, column=3, padx=8, pady=5)

    #         self.moneyPaid_entry = Entry(College_Frame_1, font=(
    #             'arial', 14), width=10, textvariable=self.paid)
    #         self.moneyPaid_entry.grid(row=3, column=3, pady=5)

    #         self.studdenDdue_entry = Entry(College_Frame_1, font=(
    #             'arial', 14), width=10, textvariable=self.due)
    #         self.studdenDdue_entry.grid(row=4, column=3, pady=7)


    #         self.Display = Text(College_Frame_2, width=42, height=12,
    #                             font=('arial', 14, 'bold'))
    #         self.Display.grid(row=0, column=0, padx=3)

    #         sb = Scrollbar(College_List_Frame)
    #         sb.grid(row=0, column=1, sticky='ns')

    #         self.list = Listbox(College_List_Frame, font=(
    #             'arial', 13, 'bold'), width=140, height=8)
    #         self.list.bind('<<ListboxSelect>>', Tuple)
    #         self.list.grid(row=0, column=0)
    #         sb.config(command=self.list.yview)


    #         button_Save = Button(Btn_Frame, text='SAVE', font=(
    #             'arial', 14, 'bold'), width=10, command=Insert)
    #         button_Save.grid(row=0, column=0, padx=5, pady=5)

    #         button_display = Button(Btn_Frame, text='DISPLAY', font=(
    #             'arial', 14, 'bold'), width=10, command=View)
    #         button_display.grid(row=0, column=1, padx=5, pady=5)

    #         button_Reset = Button(Btn_Frame, text='RESET', font=(
    #             'arial', 14, 'bold'), width=10, command=Reset)
    #         button_Reset.grid(row=0, column=2, padx=5, pady=5)

    #         button_Reset = Button(Btn_Frame, text='UPDATE', font=(
    #             'arial', 14, 'bold'), width=10, command=Update)
    #         button_Reset.grid(row=0, column=3, padx=5, pady=5)

    #         button_Search = Button(Btn_Frame, text='SEARCH', font=(
    #             'arial', 14, 'bold'), width=10, command=Search)
    #         button_Search.grid(row=0, column=4, padx=5, pady=5)

    #         button_Delete = Button(Btn_Frame, text='DELETE', font=(
    #             'arial', 14, 'bold'), width=10, command=Delete)
    #         button_Delete.grid(row=0, column=5, padx=5, pady=5)

    #         button_Receipt = Button(Btn_Frame, text='RECEIPT', font=(
    #             'arial', 14, 'bold'), width=10, command=Receipt)
    #         button_Receipt.grid(row=0, column=6, padx=5, pady=5)

    #         button_Exit = Button(Btn_Frame, text='EXIT', font=(
    #             'arial', 14, 'bold'), width=10, command=Exit)
    #         button_Exit.grid(row=0, column=7, padx=5, pady=5)


    # root = Tk()
    # obj = college_fee(root)
    # root.mainloop()
def library():
    os.system('py College-Management_System\College_Library_Frontend.py')      
def staffmanager():
   st=Tk()
   st.title("Staff Manager")
   st.maxsize(width=1520,height=1080)
   st.minsize(width=1520,height=1080) 
   st.config(bg="#1A2238")
   st.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
   cl =Label(st,text="CLASS",fg="#F4DB7D",bg="#1A2238",font = ('Times New Roman',32,'bold'))
   cl.place(x=630,y=30)
   cl2 =Label(st,text="VERGE",fg="White",bg="#1A2238",font = ('Times New Roman',32,'bold'))
   cl2.place(x=770,y=30)
   stud=Button(st,text="Add student",bg="#FF6A3D",fg="White",width=20,height=1,font = ('Times New Roman',22,'bold'),command=add_student)
   stud.place(x=150,y=150)
   perform=Button(st,text="View Performance",width=20,height=1,font = ('Times New Roman',22,'bold'),bg="#FF6A3D",fg="White",command=performance)
   perform.place(x=600,y=150)
   assign=Button(st,text="Assignment",width=20,height=1,font = ('Times New Roman',22,'bold'),bg="#FF6A3D",fg="White",command=assignment)
   assign.place(x=1050,y=150)
   sub=Button(st,text="Time Table",width=20,height=1,font = ('Times New Roman',22,'bold'),bg="#FF6A3D",fg="White",command=time_table)
   sub.place(x=150,y=350)
   mark=Button(st,text="Grading System",width=20,height=1,font = ('Times New Roman',22,'bold'),bg="#FF6A3D",fg="White",command=marking_sheet)
   mark.place(x=600,y=350)
   fees=Button(st,text="Fees Management",width=20,height=1,font = ('Times New Roman',22,'bold'),bg="#FF6A3D",fg="White",command=manage_fees)
   fees.place(x=1050,y=350)
   lib=Button(st,text="College Library",width=20,height=1,font = ('Times New Roman',22,'bold'),bg="#FF6A3D",fg="White",command=library)
   lib.place(x=600,y=550)
#    exit=Button(st,text="Back",width=15,height=1,font = ('Times New Roman',22,'bold'),bg="#9DAAF2",fg="Black",command=back)
#    exit.place(x=1050,y=550)
   st.mainloop()
def add_new_staff():
       class Student_Information():
              def __init__(self, master):
                     self.master = master
                     self.master.title('Staff Information')
                     self.master.geometry('1350x750')
                     self.master.config(bg = '#1A2238')
                     self.master.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
                     def information():

                            self.name = StringVar()
                            self.father_name = StringVar()
                            self.mother_name = StringVar()
                            self.address = StringVar()
                            self.mobileno = StringVar()
                            self.email_address = StringVar()
                            self.date_of_birth = StringVar()
                            self.gender = StringVar()
                            


                            def Staff_Record(event):
                                   try: 
                                          global selected_tuple
                                          
                                          index = self.listbox.curselection()[0]
                                          selected_tuple = self.listbox.get(index)

                                          self.Text_Entry_name.delete(0, END)
                                          self.Text_Entry_name.insert(END, selected_tuple[1])
                                          self.Text_Entry_Father_Name.delete(0, END)
                                          self.Text_Entry_Father_Name.insert(END, selected_tuple[2])
                                          self.Text_Entry_Mother_Name.delete(0, END)
                                          self.Text_Entry_Mother_Name.insert(END, selected_tuple[3])
                                          self.Text_Entry_address.delete(0, END)
                                          self.Text_Entry_address.insert(END, selected_tuple[4])
                                          self.Text_Entry_mobileno.delete(0, END)
                                          self.Text_Entry_mobileno.insert(END, selected_tuple[5])
                                          self.Text_Entry_email_address.delete(0, END)
                                          self.Text_Entry_email_address.insert(END, selected_tuple[6])
                                          self.Text_Entry_date_of_birth.delete(0, END)
                                          self.Text_Entry_date_of_birth.insert(END, selected_tuple[7])
                                          self.Text_Entry_gender.delete(0, END)
                                          self.Text_Entry_gender.insert(END, selected_tuple[8])
                                   except IndexError:
                                          pass


                            def Add():
                                   if(len(self.name.get()) != 0):
                                          Staff_backend.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                             self.gender.get())
                                          self.listbox.delete(0, END)
                                          self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                      self.gender.get()))
                                   Save = messagebox.showinfo("Login System", "Your Data is Saved successfully")
                                   self.master.destroy()
                            def Display():
                                   self.listbox.delete(0, END)
                                   for row in Staff_backend.view():
                                          self.listbox.insert(END, row, str(' '))


                            def Exit():
                                   Exit =messagebox.askyesno("Login System", "Confirm if you want to Exit")
                                   if Exit > 0:
                                          self.master.destroy()
                                          return 
                                   

                            def Reset():
                                   self.name.set('')
                                   self.father_name.set('')
                                   self.mother_name.set('')
                                   self.address.set('')
                                   self.mobileno.set('')
                                   self.email_address.set('')
                                   self.date_of_birth.set('')
                                   self.gender.set('')
                                   self.listbox.delete(0, END)

                            

                            def Delete():
                                   if(len(self.name.get()) != 0):
                                          Staff_backend.delete(selected_tuple[0])
                                          Reset()
                                          Display()


                            def Search():
                                   self.listbox.delete(0, END)
                                   for row in Staff_backend.search(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), self.gender.get()):
                                          self.listbox.insert(END, row, str(' '))
                                          

                            def Update():
                                   if(len(self.name.get()) != 0):
                                          Staff_backend.delete(selected_tuple[0])
                                          if(len(self.name.get()) != 0):
                                                 Staff_backend.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                    self.gender.get())

                                                 self.listbox.delete(0, END)
                                                 self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                             self.gender.get()))
                                   




                            self.Student_Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial', 20, 'bold'), \
                                                               bg = '#1A2238',fg="#FF6A3D", bd = 15, relief = 'ridge',text="Enter Details")
                            self.Student_Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

                            self.Student_Frame_1 = LabelFrame(self.Student_Main_Frame, width = 600, height = 400, font = ('arial', 15, 'bold'), \
                                                        relief = 'ridge', bd = 10, bg = '#1A2238',fg="#FF6A3D", text = 'Staff INFORMATION ')
                            self.Student_Frame_1.grid(row = 1, column = 0, padx = 10)

                            self.Student_Frame_2 = LabelFrame(self.Student_Main_Frame, width = 750, height = 400, font = ('arial', 15, 'bold'), \
                                                        relief = 'ridge', bd = 10, bg = '#1A2238',fg="#FF6A3D", text = 'STAFF DATABASE')
                            self.Student_Frame_2.grid(row = 1, column = 1, padx = 5)
                            
                            self.Student_Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial', 10, 'bold'), \
                                                        bg = '#1A2238', relief = 'ridge', bd = 13)
                            self.Student_Frame_3.grid(row = 2, column = 0, pady = 10)


                            

                            self.lbl_Name = Label(self.Student_Frame_1, text ='Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_Name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                            self.lbl_father_name = Label(self.Student_Frame_1, text ='Father Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_father_name.grid(row = 1, column = 0, sticky = W, padx = 20)
                            self.lbl_mother_name = Label(self.Student_Frame_1, text ='Mother Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_mother_name.grid(row = 2, column = 0, sticky = W, padx = 20)
                            self.lbl_address = Label(self.Student_Frame_1, text ='Address', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_address.grid(row = 3, column = 0, sticky = W, padx = 20)
                            self.lbl_mobileno = Label(self.Student_Frame_1, text ='Mobile Number', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_mobileno.grid(row = 4, column = 0, sticky = W, padx = 20)
                            self.lbl_email_address = Label(self.Student_Frame_1, text ='Email Address', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_email_address.grid(row = 5, column = 0, sticky = W, padx = 20)
                            self.lbl_dateOf_birth = Label(self.Student_Frame_1, text ='Date of Birth', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_dateOf_birth.grid(row = 6, column = 0, sticky = W, padx = 20)
                            self.lbl_gender = Label(self.Student_Frame_1, text ='Gender', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                            self.lbl_gender.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 10)



                            self.Text_Entry_name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.name)
                            self.Text_Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_Father_Name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.father_name)
                            self.Text_Entry_Father_Name.grid(row = 1, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_Mother_Name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.mother_name)
                            self.Text_Entry_Mother_Name.grid(row = 2, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_address = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.address)
                            self.Text_Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_mobileno = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.mobileno)
                            self.Text_Entry_mobileno.grid(row = 4, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_email_address = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.email_address)
                            self.Text_Entry_email_address.grid(row = 5, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_date_of_birth = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.date_of_birth)
                            self.Text_Entry_date_of_birth.grid(row = 6, column = 1, padx = 10, pady = 5)
                            self.Text_Entry_gender = ttk.Combobox(self.Student_Frame_1, values = (' ', 'Male', 'Female', 'Others'), \
                                                               font = ('arial',17,'bold'), textvariable = self.gender, width = 19)
                            self.Text_Entry_gender.grid(row = 7, column = 1, padx = 10, pady = 5)




                            self.SAVE_BUTTON = Button(self.Student_Frame_3, text ='SAVE', font = ('arial', 17, 'bold'), width = 8, command = Add ,bg="#9DAAF2")
                            self.SAVE_BUTTON.grid(row = 0, column = 0, padx = 10, pady = 10)
                            self.BUTTON_DISPLAY = Button(self.Student_Frame_3, text ='DISPLAY', font = ('arial', 17, 'bold'), width = 8, command = Display ,bg="#9DAAF2")
                            self.BUTTON_DISPLAY.grid(row = 0, column = 1, padx = 10, pady = 10)
                            self.BUTTON_RESET = Button(self.Student_Frame_3, text ='RESET', font = ('arial', 17, 'bold'), width = 8, command = Reset ,bg="#9DAAF2")
                            self.BUTTON_RESET.grid(row = 0, column = 2, padx = 10, pady = 10)
                            self.BUTTON_UPDATE = Button(self.Student_Frame_3, text ='UPDATE', font = ('arial', 17, 'bold'), width = 8, command = Update ,bg="#9DAAF2")
                            self.BUTTON_UPDATE.grid(row = 0, column = 3, padx = 10, pady = 10)
                            self.BUTTON_DELETE = Button(self.Student_Frame_3, text ='DELETE', font = ('arial', 17, 'bold'), width = 8, command = Delete,bg="#9DAAF2")
                            self.BUTTON_DELETE.grid(row = 0, column = 4, padx = 10, pady = 10)
                            # self.BUTTON_SEARCH = Button(self.Student_Frame_3, text ='SEARCH', font = ('arial', 17, 'bold'), width = 8, command = Search ,bg="#9DAAF2")
                            # self.BUTTON_SEARCH.grid(row = 0, column = 5, padx = 10, pady = 10)
                            self.BUTTON_EXIT = Button(self.Student_Frame_3, text ='EXIT', font = ('arial', 17, 'bold'), width = 8, command = Exit ,bg="#9DAAF2")
                            self.BUTTON_EXIT.grid(row = 0, column = 6, padx = 10, pady = 10)



                            
                            self.scrollbar = Scrollbar(self.Student_Frame_2)
                            self.scrollbar.grid(row = 0, column = 1, sticky = 'ns')

                            self.listbox = Listbox(self.Student_Frame_2, width = 75, height = 20, font = ('arial', 12, 'bold'))
                            self.listbox.bind('<<ListboxSelect>>', Staff_Record)
                            self.listbox.grid(row = 0, column = 0)
                            self.scrollbar.config(command = self.listbox.yview)
                                   
                     information()
                            

       root = Tk()
       obj = Student_Information(root)
       root.mainloop()
def time_table():
       def run_sub():
              os.system('py subjects.py')
       def run_sch(): 
              os.system('py scheduler.py')
       def run_tt_s(): 
               os.system('py timetable_stud.py')
       def run_tt_f(): 
               os.system('py timetable_fac.py')

       ad = tk.Tk()
       ad.geometry('500x430')
       ad.config(bg = '#1A2238')
       ad.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
       ad.minsize(width=500,height=430)
       ad.title('Time Table')

       tk.Label(
       ad,
       text='F A C U L T Y',
       font=('Consolas', 20, 'bold'),
       bg = '#1A2238',fg="#F4DB7D",
       pady=10
       ).pack()

       tk.Label(
       ad,
       text='You are the Faculty',
       font=('Consolas', 12, 'italic'),
       bg = '#1A2238',fg="#F4DB7D",
       ).pack(pady=9)

       modify_frame = LabelFrame(ad,text='Modify', font=('Consolas'), padx=20, bg = '#1A2238',fg="#F4DB7D")
       modify_frame.place(x=50, y=150)

       tk.Button(
       modify_frame,
       text='Subjects',
       font=('Consolas'),
       bg="#FF6A3d",
       fg="#fff",
       command=run_sub
       ).pack(pady=40)

       tt_frame = LabelFrame(ad,text='Timetable', font=('Consolas'), padx=20, bg = '#1A2238',fg="#F4DB7D")
       tt_frame.place(x=250, y=100)

       tk.Button(
       tt_frame,
       text='Schedule Periods',
       font=('Consolas'),
       bg="#FF6A3d",
       fg="#fff",
       command=run_sch
       ).pack(pady=20)

       tk.Button(
       tt_frame,
       text='View Section-Wise',
       bg="#FF6A3d",
       fg="#fff",
       font=('Consolas'),
       command=run_tt_s
       ).pack(pady=20)

       tk.Button(
       tt_frame,
       text='View Faculty-wise',
       bg="#FF6A3d",
       fg="#fff",
       font=('Consolas'),
       command=run_tt_f
       ).pack(pady=20)


       tk.Button(
       ad,
       text='Quit',
       font=('Consolas'),
       bg="#9DAAF2",
       command=ad.destroy
       ).place(x=220, y=360)

       ad.mainloop() 
        
def hodmanager():   
    hod=Tk()
    hod.title("HOD Manager")
    hod.state("zoomed")       
    hod.maxsize(width=1520,height=1080)
    hod.minsize(width=1520,height=1080) 
    hod.config(bg="#1A2238")
    hod.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
    cl =Label(hod,text="CLASS",fg="#F4DB7D",bg="#1A2238",font = ('Times New Roman',32,'bold'))
    cl.place(x=630,y=30)
    cl2 =Label(hod,text="VERGE",fg="White",bg="#1A2238",font = ('Times New Roman',32,'bold'))
    cl2.place(x=770,y=30)
    stud=Button(hod,text="Add staff",bg="#FF6A3D",fg="White",width=20,height=1,font = ('Times New Roman',22,'bold'),command=add_new_staff)
    stud.place(x=150,y=150)
    # my_menu=Menu(hod)
    # hod.config(menu=my_menu)
    # file_menu=Menu(my_menu,bg="#FF6A3D",fg="White")#drop down color
    #creted top header menu
    # #Adding drop down in each option for student
    # staff_menu=Menu(my_menu,bg="#FF6A3D",fg="White")
    # my_menu.add_cascade(label="Staff",menu=staff_menu)
    # staff_menu.add_cascade(label="Add new staff member",command=add_new_staff)
    # staff_menu.add_separator()#Adding a line after a block
    # staff_menu.add_cascade(label="pass")
    # staff_menu.add_separator()
    # staff_menu.add_cascade(label="Staff leave")
    # staff_menu.add_separator()
    # staff_menu.add_cascade(label="Staff feedback")
    # staff_menu.add_separator()
    hod.mainloop()    
def loginall():
    root.destroy()
    lg=Tk()
    lg.title('login')
    lg.config(bg="#1A2238")
    lg.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
    lg.geometry('800x500')
    lg.maxsize(width=1520,height=1080)
    '''img=PhotoImage(file="C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.png")
    img=Label(lg,image=logo)
    img.place(x=350,y=100)'''
    ls=Button(lg,text="Login as staff",bg="#FF6A3d",fg="white",width=0,height=1,font=("Times new roman", 15),command=staffmanager)
    ls.place(x=150,y=350)
    ls=Button(lg,text="Login as student",bg="#FF6A3d",fg="white",width=0,height=1,font=("Times new roman", 15))
    ls.place(x=350,y=350)
    ls=Button(lg,text="Login as Hod",bg="#FF6A3d",fg="white",width=0,height=1,font=("Times new roman", 15),command=hodmanager)
    ls.place(x=550,y=350)
    lg.mainloop()
def hoddata():
    hod=Tk()
    hod.title("HOD")
    hod.maxsize(width=500,height=300)
    hod.minsize(width=500,height=300)
    hod.config(bg="#1A2238")
    hod.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
    pin=Label(hod,text="Enter your safety pin for Authentication",fg="#FF6A3D",bg="#1A2238",font = ("Garamond", 15, 'bold'))
    pin.place(x=100,y=50)
    #hod pin = 4556
    CORRECT_PIN = "4556"
    def check_pin(pin_entry):
        if pin_entry.get() == CORRECT_PIN:
            login_successful()
        else:
            invalid_pin()
    def login_successful():
        pass
        #face recognise
    def invalid_pin():
        pin_entry.delete(0, "end") # Clear the PIN entry field
        error_label = Label(hod, text="Invalid PIN. Please try again.", fg="red")
        error_label.pack(padx=20, pady=5)
        error_label.place(x=180,y=250)
    pin_entry = Entry(hod, show="*")
    pin_entry.pack(padx=20, pady=5)
    pin_entry.place(x=200,y=100)
    #submit_button = Button(hod, text="Submit", command=login_successful)
    submit_button=Button(hod,text="Register Pin",bg="#9DAAF2",bd = 1,fg="Black",command=lambda: check_pin(pin_entry),width=10,height=0,font=("Times new roman", 15))
    submit_button.pack(padx=20, pady=20)
    submit_button.place(x=200,y=150)
    exit=Button(
            hod,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
            command=hod.destroy
        )
    exit.place(x=400,y=250,width=55)
def staffdata():
    staff=Tk()
    staff.title("Staff")
    staff.maxsize(width=500,height=300)
    staff.minsize(width=500,height=300)
    staff.config(bg="#1A2238")
    staff.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
    pin=Label(staff,text="Enter your safety pin for Authentication",fg="#FF6A3D",bg="#1A2238",font = ("Garamond", 15, 'bold'))
    pin.place(x=100,y=50)
    #hod pin = 2885
    CORRECT_PIN = "2885"
    def check_pin(pin_entry):
        if pin_entry.get() == CORRECT_PIN:
            login_successful()
        else:
            invalid_pin()
    def login_successful():
        staff.destroy()
        class staffinfo():
                def __init__(self, master):
                        self.master = master
                        self.master.title('Staff Information')
                        root.geometry('850x650')
                        root.maxsize(width=850,height=650)
                        root.config(bg="#1A2238")
                        root.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
                        
                        def information():

                                self.name = StringVar()
                                self.father_name = StringVar()
                                self.mother_name = StringVar()
                                self.address = StringVar()
                                self.mobileno = StringVar()
                                self.email_address = StringVar()
                                self.date_of_birth = StringVar()
                                self.gender = StringVar()
                                


                                def Student_Record(event):
                                    try: 
                                            global selected_tuple
                                            
                                            index = self.listbox.curselection()[0]
                                            selected_tuple = self.listbox.get(index)

                                            self.Text_Entry_name.delete(0, END)
                                            self.Text_Entry_name.insert(END, selected_tuple[1])
                                            self.Text_Entry_Father_Name.delete(0, END)
                                            self.Text_Entry_Father_Name.insert(END, selected_tuple[2])
                                            self.Text_Entry_Mother_Name.delete(0, END)
                                            self.Text_Entry_Mother_Name.insert(END, selected_tuple[3])
                                            self.Text_Entry_address.delete(0, END)
                                            self.Text_Entry_address.insert(END, selected_tuple[4])
                                            self.Text_Entry_mobileno.delete(0, END)
                                            self.Text_Entry_mobileno.insert(END, selected_tuple[5])
                                            self.Text_Entry_email_address.delete(0, END)
                                            self.Text_Entry_email_address.insert(END, selected_tuple[6])
                                            self.Text_Entry_date_of_birth.delete(0, END)
                                            self.Text_Entry_date_of_birth.insert(END, selected_tuple[7])
                                            self.Text_Entry_gender.delete(0, END)
                                            self.Text_Entry_gender.insert(END, selected_tuple[8])
                                    except IndexError:
                                            pass


                                def Add():
                                    if(len(self.name.get()) != 0):
                                        Staff_backend.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                            self.gender.get())
                                        self.listbox.delete(0, END)
                                        self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                    self.gender.get()))
                                    Save = messagebox.showinfo("Login System", "Your Data is Saved successfully")
                                    self.master.destroy()
            
                                    
                                def Display():
                                    self.listbox.delete(0, END)
                                    for row in Staff_backend.view():
                                            self.listbox.insert(END, row, str(' '))


                                def Exit():
                                    Exit = messagebox.askyesno("Login System", "Confirm if you want to Exit")
                                    if Exit > 0:
                                            self.master.destroy()
                                            return 
                                    

                                def Reset():
                                    self.name.set('')
                                    self.father_name.set('')
                                    self.mother_name.set('')
                                    self.address.set('')
                                    self.mobileno.set('')
                                    self.email_address.set('')
                                    self.date_of_birth.set('')
                                    self.gender.set('')
                                    self.listbox.delete(0, END)

                                

                                def Delete():
                                    if(len(self.name.get()) != 0):
                                            Staff_backend.delete(selected_tuple[0])
                                            Reset()
                                            #Display()


                                def Search():
                                    self.listbox.delete(0, END)
                                    for row in Staff_backend.search(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), self.gender.get()):
                                            self.listbox.insert(END, row, str(' '))
                                            

                                def Update():
                                    if(len(self.name.get()) != 0):
                                            Staff_backend.delete(selected_tuple[0])
                                            if(len(self.name.get()) != 0):
                                                    Staff_backend.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                        self.gender.geaff)
                                                    self.listbox.delete(0, END)
                                                    self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                self.gender.get()))
                                    



                                self.Student_Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial', 20, 'bold'),
                                                                bg = '#1A2238',fg="#FF6A3D", bd = 15, relief = 'ridge',text="Enter details")
                                self.Student_Main_Frame.grid(row = 0, column = 0, padx = 50, pady = 20)

                                self.Student_Frame_1 = LabelFrame(self.Student_Main_Frame, width = 600, height = 400, font = ('arial', 15, 'bold'),
                                                            relief = 'ridge', bd = 10, bg = '#1A2238',fg="#FF6A3D", text = 'STUDENT INFORMATION ')
                                self.Student_Frame_1.grid(row = 1, column = 0, padx = 50,pady=10)
                                
                                self.Student_Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial', 10, 'bold'),
                                                            bg = '#1A2238', relief = 'ridge', bd = 13)
                                self.Student_Frame_3.grid(row = 2, column = 0, pady = 0,padx=60)


                                

                                self.lbl_Name = Label(self.Student_Frame_1, text ='Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_Name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                                self.lbl_father_name = Label(self.Student_Frame_1, text ='Father Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_father_name.grid(row = 1, column = 0, sticky = W, padx = 20)
                                self.lbl_mother_name = Label(self.Student_Frame_1, text ='Mother Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_mother_name.grid(row = 2, column = 0, sticky = W, padx = 20)
                                self.lbl_address = Label(self.Student_Frame_1, text ='Address', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_address.grid(row = 3, column = 0, sticky = W, padx = 20)
                                self.lbl_mobileno = Label(self.Student_Frame_1, text ='Mobile Number', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_mobileno.grid(row = 4, column = 0, sticky = W, padx = 20)
                                self.lbl_email_address = Label(self.Student_Frame_1, text ='Email Address', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_email_address.grid(row = 5, column = 0, sticky = W, padx = 20)
                                self.lbl_dateOf_birth = Label(self.Student_Frame_1, text ='Date of Birth', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_dateOf_birth.grid(row = 6, column = 0, sticky = W, padx = 20)
                                self.lbl_gender = Label(self.Student_Frame_1, text ='Gender', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_gender.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 10)



                                self.Text_Entry_name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.name)
                                self.Text_Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_Father_Name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.father_name)
                                self.Text_Entry_Father_Name.grid(row = 1, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_Mother_Name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.mother_name)
                                self.Text_Entry_Mother_Name.grid(row = 2, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_address = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.address)
                                self.Text_Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_mobileno = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.mobileno)
                                self.Text_Entry_mobileno.grid(row = 4, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_email_address = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.email_address)
                                self.Text_Entry_email_address.grid(row = 5, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_date_of_birth = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.date_of_birth)
                                self.Text_Entry_date_of_birth.grid(row = 6, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_gender = ttk.Combobox(self.Student_Frame_1, values = (' ', 'Male', 'Female', 'Others'), \
                                                                font = ('arial',17,'bold'), textvariable = self.gender, width = 19)
                                self.Text_Entry_gender.grid(row = 7, column = 1, padx = 10, pady = 5)





                                self.SAVE_BUTTON = Button(self.Student_Frame_3, text ='SAVE', font = ('arial', 17, 'bold'), width = 8, command = Add,bg="#9DAAF2")
                                self.SAVE_BUTTON.grid(row = 0, column = 0, padx = 10, pady = 10)
                                #self.BUTTON_DISPLAY = Button(self.Student_Frame_3, text ='DISPLAY', font = ('arial', 17, 'bold'), width = 8, command = Display)
                                #self.BUTTON_DISPLAY.grid(row = 0, column = 1, padx = 10, pady = 10)
                                self.BUTTON_RESET = Button(self.Student_Frame_3, text ='RESET', font = ('arial', 17, 'bold'), width = 8, command = Reset,bg="#9DAAF2")
                                self.BUTTON_RESET.grid(row = 0, column = 2, padx = 10, pady = 10)
                                #self.BUTTON_UPDATE = Button(self.Student_Frame_3, text ='UPDATE', font = ('arial', 17, 'bold'), width = 8, command = Update,bg="#9DAAF2")
                                #self.BUTTON_UPDATE.grid(row = 0, column = 3, padx = 10, pady = 10)
                                #self.BUTTON_DELETE = Button(self.Student_Frame_3, text ='DELETE', font = ('arial', 17, 'bold'), width = 8, command = Delete,bg="#9DAAF2")
                                #self.BUTTON_DELETE.grid(row = 0, column = 4, padx = 10, pady = 10)
                                #self.BUTTON_SEARCH = Button(self.Student_Frame_3, text ='SEARCH', font = ('arial', 17, 'bold'), width = 8, command = Search,bg="#9DAAF2")
                                #self.BUTTON_SEARCH.grid(row = 0, column = 5, padx = 10, pady = 10)
                                self.BUTTON_EXIT = Button(self.Student_Frame_3, text ='EXIT', font = ('arial', 17, 'bold'), width = 8, command = Exit,bg="#9DAAF2")
                                self.BUTTON_EXIT.grid(row = 0, column = 6, padx = 10, pady = 10)



                                
                                self.scrollbar = Scrollbar(self.Student_Frame_2)
                                self.scrollbar.grid(row = 0, column = 1, sticky = 'ns')

                                self.listbox = Listbox(self.Student_Frame_2, width = 75, height = 20, font = ('arial', 12, 'bold'))
                                self.listbox.bind('<<ListboxSelect>>', Student_Record)
                                self.listbox.grid(row = 0, column = 0)
                                self.scrollbar.config(command = self.listbox.yview)
                                    
                        information()
        root = Tk()
        obj = staffinfo(root)
        root.mainloop()                        
    def invalid_pin():
        pin_entry.delete(0, "end") # Clear the PIN entry field
        error_label = Label(staff, text="Invalid PIN. Please try again.", fg="red")
        error_label.pack(padx=20, pady=5)
        error_label.place(x=180,y=250)
    pin_entry = Entry(staff, show="*")
    pin_entry.pack(padx=20, pady=5)
    pin_entry.place(x=200,y=100)
    #submit_button = Button(st, text="Submit", command=login_successful)
    submit_button=Button(staff,text="Register pin",bg="#9DAAF2",bd = 1,fg="Black",command=lambda: check_pin(pin_entry),width=10,height=0,font=("Times new roman", 15))
    submit_button.pack(padx=20, pady=20)
    submit_button.place(x=200,y=150)
    exit=Button(
            staff,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
            command=staff.destroy
        )
    exit.place(x=350,y=250,width=55)
    staff.mainloop()
        #face recognise
    def invalid_pin():
        pin_entry.delete(0, "end") # Clear the PIN entry field
        error_label = Label(staff, text="Invalid PIN. Please try again.", fg="red")
        error_label.pack(padx=20, pady=5)
        error_label.place(x=180,y=250)
    pin_entry = Entry(staff, show="*")
    pin_entry.pack(padx=20, pady=5)
    pin_entry.place(x=200,y=100)
    #submit_button = Button(hod, text="Submit", command=login_successful)
    submit_button=Button(staff,text="Register pin",bg="#9DAAF2",bd = 1,fg="Black",command=lambda: check_pin(pin_entry),width=10,height=0,font=("Times new roman", 15))
    submit_button.pack(padx=20, pady=20)
    submit_button.place(x=200,y=150)
    exit=Button(
            staff,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
            command=staff.destroy
        )
    exit.place(x=400,y=250,width=55)
def studentdata():
    st=Tk()
    st.title("Students")
    st.maxsize(width=500,height=300)
    st.minsize(width=500,height=300)
    st.config(bg="#1A2238")
    st.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
    pin=Label(st,text="Enter your safety pin for Authentication",fg="#FF6A3D",bg="#1A2238",font = ("Garamond", 15, 'bold'))
    pin.place(x=100,y=50)
    CORRECT_PIN = "5228"
    def check_pin(pin_entry):
        if pin_entry.get() == CORRECT_PIN:
            login_successful()
        else:
            invalid_pin()
    def login_successful():
        st.destroy()
        class Student_Information():
                def __init__(self, master):
                        self.master = master
                        self.master.title('Student Information')
                        root.geometry('850x650')
                        root.maxsize(width=850,height=650)
                        root.config(bg="#1A2238")
                        root.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
                        
                        def information():

                                self.name = StringVar()
                                self.father_name = StringVar()
                                self.mother_name = StringVar()
                                self.address = StringVar()
                                self.mobileno = StringVar()
                                self.email_address = StringVar()
                                self.date_of_birth = StringVar()
                                self.gender = StringVar()
                                


                                def Student_Record(event):
                                    try: 
                                            global selected_tuple
                                            
                                            index = self.listbox.curselection()[0]
                                            selected_tuple = self.listbox.get(index)

                                            self.Text_Entry_name.delete(0, END)
                                            self.Text_Entry_name.insert(END, selected_tuple[1])
                                            self.Text_Entry_Father_Name.delete(0, END)
                                            self.Text_Entry_Father_Name.insert(END, selected_tuple[2])
                                            self.Text_Entry_Mother_Name.delete(0, END)
                                            self.Text_Entry_Mother_Name.insert(END, selected_tuple[3])
                                            self.Text_Entry_address.delete(0, END)
                                            self.Text_Entry_address.insert(END, selected_tuple[4])
                                            self.Text_Entry_mobileno.delete(0, END)
                                            self.Text_Entry_mobileno.insert(END, selected_tuple[5])
                                            self.Text_Entry_email_address.delete(0, END)
                                            self.Text_Entry_email_address.insert(END, selected_tuple[6])
                                            self.Text_Entry_date_of_birth.delete(0, END)
                                            self.Text_Entry_date_of_birth.insert(END, selected_tuple[7])
                                            self.Text_Entry_gender.delete(0, END)
                                            self.Text_Entry_gender.insert(END, selected_tuple[8])
                                    except IndexError:
                                            pass


                                def Add():
                                    if(len(self.name.get()) != 0):
                                        Student_backend.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                            self.gender.get())
                                        self.listbox.delete(0, END)
                                        self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                    self.gender.get()))
                                    Save = messagebox.showinfo("Login System", "Your Data is Saved successfully")
                                    self.master.destroy()
            
                                    
                                def Display():
                                    self.listbox.delete(0, END)
                                    for row in Student_backend.view():
                                            self.listbox.insert(END, row, str(' '))


                                def Exit():
                                    Exit = messagebox.askyesno("Login System", "Confirm if you want to Exit")
                                    if Exit > 0:
                                            self.master.destroy()
                                            return 
                                    

                                def Reset():
                                    self.name.set('')
                                    self.father_name.set('')
                                    self.mother_name.set('')
                                    self.address.set('')
                                    self.mobileno.set('')
                                    self.email_address.set('')
                                    self.date_of_birth.set('')
                                    self.gender.set('')
                                    self.listbox.delete(0, END)

                                

                                def Delete():
                                    if(len(self.name.get()) != 0):
                                            Student_backend.delete(selected_tuple[0])
                                            Reset()
                                            #Display()


                                def Search():
                                    self.listbox.delete(0, END)
                                    for row in Student_backend.search(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), self.gender.get()):
                                            self.listbox.insert(END, row, str(' '))
                                            

                                def Update():
                                    if(len(self.name.get()) != 0):
                                            Student_backend.delete(selected_tuple[0])
                                            if(len(self.name.get()) != 0):
                                                    Student_backend.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                        self.gender.get())

                                                    self.listbox.delete(0, END)
                                                    self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                self.gender.get()))
                                    



                                self.Student_Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial', 20, 'bold'),
                                                                bg = '#1A2238',fg="#FF6A3D", bd = 15, relief = 'ridge',text="Enter details")
                                self.Student_Main_Frame.grid(row = 0, column = 0, padx = 50, pady = 20)

                                self.Student_Frame_1 = LabelFrame(self.Student_Main_Frame, width = 600, height = 400, font = ('arial', 15, 'bold'),
                                                            relief = 'ridge', bd = 10, bg = '#1A2238',fg="#FF6A3D", text = 'STUDENT INFORMATION ')
                                self.Student_Frame_1.grid(row = 1, column = 0, padx = 50,pady=10)
                                
                                self.Student_Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial', 10, 'bold'),
                                                            bg = '#1A2238', relief = 'ridge', bd = 13)
                                self.Student_Frame_3.grid(row = 2, column = 0, pady = 0,padx=60)


                                

                                self.lbl_Name = Label(self.Student_Frame_1, text ='Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_Name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                                self.lbl_father_name = Label(self.Student_Frame_1, text ='Father Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_father_name.grid(row = 1, column = 0, sticky = W, padx = 20)
                                self.lbl_mother_name = Label(self.Student_Frame_1, text ='Mother Name', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_mother_name.grid(row = 2, column = 0, sticky = W, padx = 20)
                                self.lbl_address = Label(self.Student_Frame_1, text ='Address', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_address.grid(row = 3, column = 0, sticky = W, padx = 20)
                                self.lbl_mobileno = Label(self.Student_Frame_1, text ='Mobile Number', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_mobileno.grid(row = 4, column = 0, sticky = W, padx = 20)
                                self.lbl_email_address = Label(self.Student_Frame_1, text ='Email Address', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_email_address.grid(row = 5, column = 0, sticky = W, padx = 20)
                                self.lbl_dateOf_birth = Label(self.Student_Frame_1, text ='Date of Birth', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_dateOf_birth.grid(row = 6, column = 0, sticky = W, padx = 20)
                                self.lbl_gender = Label(self.Student_Frame_1, text ='Gender', font = ('arial', 20, 'bold'), bg ='#1A2238',fg="#F4DB7D")
                                self.lbl_gender.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 10)



                                self.Text_Entry_name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.name)
                                self.Text_Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_Father_Name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.father_name)
                                self.Text_Entry_Father_Name.grid(row = 1, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_Mother_Name = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.mother_name)
                                self.Text_Entry_Mother_Name.grid(row = 2, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_address = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.address)
                                self.Text_Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_mobileno = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.mobileno)
                                self.Text_Entry_mobileno.grid(row = 4, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_email_address = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.email_address)
                                self.Text_Entry_email_address.grid(row = 5, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_date_of_birth = Entry(self.Student_Frame_1, font = ('arial', 17, 'bold'), textvariable = self.date_of_birth)
                                self.Text_Entry_date_of_birth.grid(row = 6, column = 1, padx = 10, pady = 5)
                                self.Text_Entry_gender = ttk.Combobox(self.Student_Frame_1, values = (' ', 'Male', 'Female', 'Others'), \
                                                                font = ('arial',17,'bold'), textvariable = self.gender, width = 19)
                                self.Text_Entry_gender.grid(row = 7, column = 1, padx = 10, pady = 5)





                                self.SAVE_BUTTON = Button(self.Student_Frame_3, text ='SAVE', font = ('arial', 17, 'bold'), width = 8, command = Add,bg="#9DAAF2")
                                self.SAVE_BUTTON.grid(row = 0, column = 0, padx = 10, pady = 10)
                                #self.BUTTON_DISPLAY = Button(self.Student_Frame_3, text ='DISPLAY', font = ('arial', 17, 'bold'), width = 8, command = Display)
                                #self.BUTTON_DISPLAY.grid(row = 0, column = 1, padx = 10, pady = 10)
                                self.BUTTON_RESET = Button(self.Student_Frame_3, text ='RESET', font = ('arial', 17, 'bold'), width = 8, command = Reset,bg="#9DAAF2")
                                self.BUTTON_RESET.grid(row = 0, column = 2, padx = 10, pady = 10)
                                #self.BUTTON_UPDATE = Button(self.Student_Frame_3, text ='UPDATE', font = ('arial', 17, 'bold'), width = 8, command = Update,bg="#9DAAF2")
                                #self.BUTTON_UPDATE.grid(row = 0, column = 3, padx = 10, pady = 10)
                                #self.BUTTON_DELETE = Button(self.Student_Frame_3, text ='DELETE', font = ('arial', 17, 'bold'), width = 8, command = Delete,bg="#9DAAF2")
                                #self.BUTTON_DELETE.grid(row = 0, column = 4, padx = 10, pady = 10)
                                #self.BUTTON_SEARCH = Button(self.Student_Frame_3, text ='SEARCH', font = ('arial', 17, 'bold'), width = 8, command = Search,bg="#9DAAF2")
                                #self.BUTTON_SEARCH.grid(row = 0, column = 5, padx = 10, pady = 10)
                                self.BUTTON_EXIT = Button(self.Student_Frame_3, text ='EXIT', font = ('arial', 17, 'bold'), width = 8, command = Exit,bg="#9DAAF2")
                                self.BUTTON_EXIT.grid(row = 0, column = 6, padx = 10, pady = 10)



                                
                                '''self.scrollbar = Scrollbar(self.Student_Frame_2)
                                self.scrollbar.grid(row = 0, column = 1, sticky = 'ns')

                                self.listbox = Listbox(self.Student_Frame_2, width = 75, height = 20, font = ('arial', 12, 'bold'))
                                self.listbox.bind('<<ListboxSelect>>', Student_Record)
                                self.listbox.grid(row = 0, column = 0)
                                self.scrollbar.config(command = self.listbox.yview)'''
                                    
                        information()
        root = Tk()
        obj = Student_Information(root)
        root.mainloop()                        
    def invalid_pin():
        pin_entry.delete(0, "end") # Clear the PIN entry field
        error_label = Label(st, text="Invalid PIN. Please try again.", fg="red")
        error_label.pack(padx=20, pady=5)
        error_label.place(x=180,y=250)
    pin_entry = Entry(st, show="*")
    pin_entry.pack(padx=20, pady=5)
    pin_entry.place(x=200,y=100)
    #submit_button = Button(st, text="Submit", command=login_successful)
    submit_button=Button(st,text="Register pin",bg="#9DAAF2",bd = 1,fg="Black",command=lambda: check_pin(pin_entry),width=10,height=0,font=("Times new roman", 15))
    submit_button.pack(padx=20, pady=20)
    submit_button.place(x=200,y=150)
    exit=Button(
            st,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
            command=st.destroy
        )
    exit.place(x=350,y=250,width=55)
    st.mainloop()
student= Button(root,text="Register As Staff",bg="#FF6A3d",fg="white",width=0,height=1,font=("Times new roman", 15),command=staffdata)
student.place(x=300,y=650)
student= Button(root,text="Register As Student",bg="#FF6A3d",fg="white",width=0,height=1,font=("Times new roman", 15),command=studentdata)
student.place(x=700,y=650)
student= Button(root,text="Register As HOD",bg="#FF6A3d",fg="white",width=0,height=1,font=("Times new roman", 15),command=hoddata)
student.place(x=1100,y=650)
login=Button(root,text="Login",bg="#FF6A3d",fg="white",width=0,height=1,font=("Times new roman", 15),command=loginall)
login.place(x=1400,y=30)
def notice():
    root = Tk()
    root.title("Notice Board")
    root.geometry("500x400")
    root.minsize(width=500,height=400)
    root.maxsize(width=500,height=400)
    root.iconbitmap('C:/Users/Harsh Jajal/Documents/Classverge/Main/Logo.ico')
    root.config(bg="#1A2238")

    # Create the label for the notice board
    notice_board_label = Label(root, text="Notice Board", font=("Times new roman", 16),bg="#FF643d",fg="#fff")
    notice_board_label.pack(pady=30)
    exit=Button(
            root,text="Back",font=('Garamond', 12),bg="#9DAAF2",
            command=root.destroy
        )
    exit.place(x=350,y=300,width=55)
    # Create the text box for the notices
    notice_text_box = Text(root, height=10, width=50,bg="#F4DB7D",fg="black",font=('bold'))
    notice_text_box.pack()

    # Create the button to submit a notice


    def submit_notice():
        notice = notice_text_box.get("1.0", END)
        # Here, you can add code to save the notice to a database or file
        print("Notice submitted:", notice)
        root.destroy()



    submit_button = Button(root, text="Submit Notice",bg="#9DAAF2",font=('Garamond', 12), command=submit_notice)
    submit_button.pack(pady=29)

    # Create a login screen for the admin


    def login_screen():
        # Create a new window for the login screen
        login_window = Toplevel(root)
        login_window.title("Admin Login")

        # Create the labels and entry boxes for the username and password
        username_label = Label(login_window, text="Username:")
        username_label.grid(row=0, column=0)
        username_entry = Entry(login_window)
        username_entry.grid(row=0, column=1)

        password_label = Label(login_window, text="Password:")
        password_label.grid(row=1, column=0)
        password_entry = Entry(login_window, show="*")
        password_entry.grid(row=1, column=1)

        # Create the login button
        def login():
            # Here, you can add code to check if the username and password are correct
            # If they are, allow the admin to edit the notice board
            print("Logged in as admin")

            # Enable editing of the notice board
            notice_text_box.config(state=NORMAL)

            # Close the login window
            login_window.destroy()

        login_button = Button(login_window, text="Login", command=login)
        login_button.grid(row=2, column=1)


    # Create a menu bar
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    # Create a "Admin Login" menu
    admin_menu = Menu(menu_bar)
    menu_bar.add_cascade(label="Admin", menu=admin_menu)
    admin_menu.add_command(label="Login", command=login_screen)

    # Disable editing of the notice board by default
    notice_text_box.config(state=DISABLED)

    # Start the main loop
    root.mainloop()
note=Button(root,text="Add notice",bg="#FF6A3d",fg="white",width=0,height=1,font=("Times new roman", 15),command=notice)
note.place(x=100,y=30)
root.mainloop()