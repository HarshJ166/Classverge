from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter as tk
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
import College_Std_info_BackEnd
root = Tk()
root.title("Homepage")
root.geometry('1550x1080')
root.maxsize(width=1550,height=1080)
root.minsize(width=1550,height=1080)
root.config(bg="#1A2238")
root.iconbitmap('Logo.ico')
headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
sublabelfont = ("Noto Sans CJK TC", 15)
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)
logo = PhotoImage(file="logo.png")
logo_label=Label(image=logo)
logo_label.place(x=410,y=100)
#For jpg use Image.open("Address")
#register
def register():
    exec(open('main.py').read())

def student_leave():
    conn = sqlite3.connect('leave_applications.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leave_applications (id INTEGER PRIMARY KEY, name TEXT, from_date TEXT, to_date TEXT, reason TEXT, status TEXT)''')
    conn.commit()

    # Create a function to submit the leave application form


    def submit_application():
            success=Label(root,text="You application succesffuly submitted!!",fg="#FF6A3D")
            success.place(x=150,y=350)
            status = 'Pending'
            c.execute('''INSERT INTO leave_applications (name, from_date, to_date, reason, status) VALUES (?, ?, ?, ?, ?)''',
                    (status))
            conn.commit()
    def back():
        root.destroy()
    # Create a function to refresh the leave applications list with the latest applications from the database



    # Create a function to approve a leave application

    # Create the GUI elements for the leave application form and applications list
    root = tk.Tk()
    root.title('Leave Application')
    root.maxsize(width=500,height=400)
    root.minsize(width=500,height=400)
    root.config(bg="#1A2238")

    app=Label(root,
            text='Leave application',
            font=('Garamond', 20,'bold'),bg='#FF6A3D',fg="white"
        ).pack(side=TOP, fill=X,pady=10)
    name_label = tk.Label(root, text='Name:', font=('Garamond', 12,'bold'),bg="#F4DB7D")
    name_label.place(x=150,y=100)
    name_entry = tk.Entry(root, font=('Garamond', 12))
    name_entry.place(x=220,y=100)


    from_date_label = tk.Label(
    root, text='From Date (dd/mm/yyyy):', font=('Garamond', 12,'bold'),bg="#F4DB7D")
    from_date_label.place(x=10,y=150)
    from_date_entry = tk.Entry(root, font=('Garamond', 12))
    from_date_entry.place(x=220,y=150)

    to_date_label = tk.Label(
        root, text='To Date (dd/mm/yyyy):', font=('Garamond', 12,'bold'),bg="#F4DB7D")
    # to_date
    to_date_label.place(x=30,y=200)
    to_date_entry = tk.Entry(root, font=('Garamond', 12))
    to_date_entry.place(x=220,y=200)

    reason_label = tk.Label(root, text='Reason:', font=('Garamond', 12,'bold'),bg="#F4DB7D")
    reason_label.place(x=150,y=250)
    reason_entry = tk.Entry(root, font=('Garamond', 12))
    reason_entry.place(x=220,y=250)

    submit_button = tk.Button(root, text='Submit', font=(
        'Garamond', 16,'bold'),bg="#9DAAF2", command=submit_application)
    submit_button.pack(pady=20)
    submit_button.place(x=150,y=300)
    back_button = tk.Button(root, text='back', font=(
        'Garamond', 16,'bold'),bg="#9DAAF2", command=back)
    back_button.pack(pady=20)
    back_button.place(x=250,y=300)

    applications_frame = tk.Frame(root)
    applications_frame.pack()

    # Refresh the leave applications list on startup

    # Run the main loop
    root.mainloop()

    # Close the database connection when the program is finished
    conn.close()

def student_manager():
    root.destroy()
    hod=Tk()
    hod.title("Students")
    hod.maxsize(width=500,height=300)
    hod.minsize(width=500,height=300)
    hod.config(bg="#1A2238")
    hod.iconbitmap('logo.ico')
    headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
    sublabelfont = ("Noto Sans CJK TC", 15)
    labelfont = ('Garamond', 14)
    entryfont = ('Garamond', 12)
    t2=Label(hod,text="Enter your safety pin for Authentication",fg="#FF6A3D",bg="#1A2238",font = ("Garamond", 15, 'bold'))
    t2.place(x=100,y=50)
    #Hod pin = 5228
    CORRECT_PIN = "5228"
    def check_pin(pin_entry):
        if pin_entry.get() == CORRECT_PIN:
            login_successful()
        else:
            invalid_pin()
    # Define a function to display a "Login Successful" message
    def login_successful():
        # Close the login window
        # Close the login window
        def studentinfo():
            class Student_Information():
                    def __init__(self, master):
                            self.master = master
                            self.master.title('Student Information')
                            root.geometry('850x650')
                            root.maxsize(width=850,height=650)
                            root.config(bg="#1A2238")
                            root.iconbitmap('Logo.ico')
                            
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
                                                College_Std_info_BackEnd.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                    self.gender.get())
                                                self.listbox.delete(0, END)
                                                self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                            self.gender.get()))
                                        after_save()
                                        
                                    '''def Display():
                                        self.listbox.delete(0, END)
                                        for row in College_Std_info_BackEnd.view():
                                                self.listbox.insert(END, row, str(' '))'''


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
                                                College_Std_info_BackEnd.delete(selected_tuple[0])
                                                Reset()
                                                #Display()


                                    def Search():
                                        self.listbox.delete(0, END)
                                        for row in College_Std_info_BackEnd.search(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), self.gender.get()):
                                                self.listbox.insert(END, row, str(' '))
                                                

                                    def Update():
                                        if(len(self.name.get()) != 0):
                                                College_Std_info_BackEnd.delete(selected_tuple[0])
                                                if(len(self.name.get()) != 0):
                                                        College_Std_info_BackEnd.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                            self.gender.get())

                                                        self.listbox.delete(0, END)
                                                        self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                    self.gender.get()))
                                        



                                    self.Student_Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial', 20, 'bold'),
                                                                    bg = '#1A2238',fg="#FF6A3D", bd = 15, relief = 'ridge',text="Enter your details")
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
                                    self.BUTTON_DELETE = Button(self.Student_Frame_3, text ='DELETE', font = ('arial', 17, 'bold'), width = 8, command = Delete,bg="#9DAAF2")
                                    self.BUTTON_DELETE.grid(row = 0, column = 4, padx = 10, pady = 10)
                                    self.BUTTON_SEARCH = Button(self.Student_Frame_3, text ='SEARCH', font = ('arial', 17, 'bold'), width = 8, command = Search,bg="#9DAAF2")
                                    self.BUTTON_SEARCH.grid(row = 0, column = 5, padx = 10, pady = 10)
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
        studentinfo()
    def invalid_pin():
        pin_entry.delete(0, "end") # Clear the PIN entry field
        error_label = Label(hod, text="Invalid PIN. Please try again.", fg="red")
        error_label.pack(padx=20, pady=5)
        error_label.place(x=180,y=250)
    pin_entry = Entry(hod, show="*")
    pin_entry.pack(padx=20, pady=5)
    pin_entry.place(x=200,y=100)
    #submit_button = Button(hod, text="Submit", command=login_successful)
    submit_button=Button(hod,text="Login",bg="#9DAAF2",bd = 1,fg="Black",command=lambda: check_pin(pin_entry),width=10,height=0,font=("Times new roman", 15))
    submit_button.pack(padx=10, pady=20)
    submit_button.place(x=200,y=150)
    exit=Button(
            hod,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
            command=hod.destroy
        )
    exit.place(x=350,y=250,width=55)

def staff_manager():
    root.destroy()
    hod=Tk()
    hod.title("Staff Manager")
    hod.maxsize(width=500,height=300)
    hod.minsize(width=500,height=300)
    hod.config(bg="#1A2238")
    hod.iconbitmap('logo.ico')
    headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
    sublabelfont = ("Noto Sans CJK TC", 15)
    labelfont = ('Garamond', 14)
    entryfont = ('Garamond', 12)
    #Hod pin = 4556
    CORRECT_PIN = "2885"
    def check_pin(pin_entry):
        if pin_entry.get() == CORRECT_PIN:
            login_successful()
        else:
            invalid_pin()
    # Define a function to display a "Login Successful" message
    def login_successful():
        # Close the login window
        # Close the login window
        hod=Tk()
        hod.title("Staff Manager")
        hod.maxsize(width=1800,height=1080)
        hod.minsize(width=1000,height=1080)
        hod.config(bg="#1A2238")
        hod.iconbitmap('logo.ico')
        headlabelfont = ("Noto Sans CJK TC", 15, 'bold')   
        sublabelfont = ("Noto Sans CJK TC", 15)
        labelfont = ('Garamond', 14)    
        entryfont = ('Garamond', 12)
        def add():
            pass
        my_menu=Menu(hod)
        hod.config(menu=my_menu)
        file_menu=Menu(my_menu,bg="#FF6A3D",fg="White")#drop down color
        my_menu.add_cascade(label="Student",menu=file_menu)#creted top header menu
        #Adding drop down in each option for student
        file_menu.add_cascade(label="Add new student",command=add_new_student)
        file_menu.add_separator()#Adding a line after a block
        file_menu.add_cascade(label="Attendance",command=student_Attendance) 
        file_menu.add_separator()
        file_menu.add_cascade(label="Results",command=results)
        file_menu.add_separator()
        file_menu.add_cascade(label="Student leave",command=leave)
        file_menu.add_separator()
        file_menu.add_cascade(label="Student feedback",command=student_feedback)
        file_menu.add_separator()
        edit_menu=Menu(my_menu,bg="#FF6A3D",fg="White")
        my_menu.add_cascade(label="Class data",menu=edit_menu)
        #Adding drop down in each option for student
        #Adding a line after a block
        edit_menu.add_cascade(label="Add Assignment",command=file)
        edit_menu.add_separator()
        edit_menu.add_cascade(label="Add Results",command=add)
        edit_menu.add_separator()
        staff_menu=Menu(my_menu,bg="#FF6A3D",fg="White")
    def invalid_pin():
        pin_entry.delete(0, "end") # Clear the PIN entry field
        error_label = Label(hod, text="Invalid PIN. Please try again.", fg="red")
        error_label.pack(padx=20, pady=5)
        error_label.place(x=180,y=250)
    pin_entry = Entry(hod, show="*")
    pin_entry.pack(padx=20, pady=5)
    pin_entry.place(x=200,y=100)
    #submit_button = Button(hod, text="Submit", command=login_successful)
    submit_button=Button(hod,text="Login",bg="#9DAAF2",bd = 1,fg="Black",command=lambda: check_pin(pin_entry),width=10,height=0,font=("Times new roman", 15))
    submit_button.pack(padx=20, pady=20)
    submit_button.place(x=200,y=150)
    exit=Button(
            hod,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
            command=hod.destroy
        )
    exit.place(x=400,y=250,width=55)
    
def file():
    file = Tk()
    file.geometry('1000x1080')
    file.maxsize(width=1800,height=1080)
    file.minsize(width=1000,height=1080)
    file.config(background="#1A2238")
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
        f1 = Frame(file, background="grey")
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
        f = Frame(file, background="white")
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
        f1 = Frame(file, background="grey")
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
        f1=Frame(file)
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
        f1 = Frame(file, width=350, height=300, background="lavender")
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


    lbl_heading = Label(file, text="File Management system",font=("bold",18),fg="gold2",bg='black')
    lbl_heading.grid(row=1, column=1, pady=20, padx=20)

    open_btn = Button(file, text="Open File",command=open_file, width=15,font=('bold',14))
    open_btn.grid(row=2, column=0,pady=20, padx=20)

    delete_btn = Button(file, text="Delete File",command=delete_file, width=15,font=('bold',14))
    delete_btn.grid(row=2, column=1,pady=20, padx=20)

    rename_btn = Button(file, text="Rename File", command=rename_file, width=15,font=('bold',14))
    rename_btn.grid(row=2, column=2,pady=20, padx=20)

    copy_move_btn = Button(file, text="Copy/Move File", command=copy_move_file, width=15,font=('bold',14))
    copy_move_btn.grid(row=2, column=3,pady=20, padx=20)

    create_folder_btn = Button(file, text="Create folder", command=create_folder, width=15,font=('bold',14))
    create_folder_btn.grid(row=3, column=0, pady=20, padx=20)

    deletefolder_btn = Button(file, text="Delete folder", command=deletefolder, width=15,font=('bold',14))
    deletefolder_btn.grid(row=3, column=1, pady=20, padx=20)

    rename_folder_btn = Button(file, text="Rename Folder", command=rename_folder, width=15,font=('bold',14))
    rename_folder_btn.grid(row=3, column=2,pady=20, padx=20)

    view_btn = Button(file, text="View folder contents", command=view_folder, width=15,font=('bold',14))
    view_btn.grid(row=3, column=3, pady=20, padx=20)

    exit_btn = Button(file, text="Exit", command=file.destroy, width=12,font=('bold',14))
    exit_btn.grid(row=4, column=1, pady=20, padx=20)

    file.mainloop()
def add_new_student():
    def studentinfo():
        class Student_Information():
                def __init__(self, master):
                        self.master = master
                        self.master.title('Student Information')
                        root.geometry('850x650')
                        root.maxsize(width=850,height=650)
                        root.config(bg="#1A2238")
                        root.iconbitmap('Logo.ico')
                        
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
                                    self.master.destroy()
                                    if(len(self.name.get()) != 0):
                                            College_Std_info_BackEnd.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                self.gender.get())
                                            self.listbox.delete(0, END)
                                            self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                        self.gender.get()))

                                '''def Display():
                                    self.listbox.delete(0, END)
                                    for row in College_Std_info_BackEnd.view():
                                            self.listbox.insert(END, row, str(' '))'''


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
                                            College_Std_info_BackEnd.delete(selected_tuple[0])
                                            Reset()
                                            #Display()


                                def Search():
                                    self.listbox.delete(0, END)
                                    for row in College_Std_info_BackEnd.search(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), self.gender.get()):
                                            self.listbox.insert(END, row, str(' '))
                                            

                                def Update():
                                    if(len(self.name.get()) != 0):
                                            College_Std_info_BackEnd.delete(selected_tuple[0])
                                            if(len(self.name.get()) != 0):
                                                    College_Std_info_BackEnd.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
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
                                self.BUTTON_DELETE = Button(self.Student_Frame_3, text ='DELETE', font = ('arial', 17, 'bold'), width = 8, command = Delete,bg="#9DAAF2")
                                self.BUTTON_DELETE.grid(row = 0, column = 4, padx = 10, pady = 10)
                                self.BUTTON_SEARCH = Button(self.Student_Frame_3, text ='SEARCH', font = ('arial', 17, 'bold'), width = 8, command = Search,bg="#9DAAF2")
                                self.BUTTON_SEARCH.grid(row = 0, column = 5, padx = 10, pady = 10)
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
    studentinfo()
def student_Attendance():
    pass
def results():
    pass
def leave():
    # Create a database connection and a table to store the leave applications
    conn = sqlite3.connect('leave_applications.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leave_applications (id INTEGER PRIMARY KEY, name TEXT, from_date TEXT, to_date TEXT, reason TEXT, status TEXT)''')
    conn.commit()

    # Create a function to submit the leave application form


    def submit_application():

        status = 'Pending'
        c.execute('''INSERT INTO leave_applications (name, from_date, to_date, reason, status) VALUES (?, ?, ?, ?, ?)''',
                ( status))
        conn.commit()
        refresh_leave_applications()



    def refresh_leave_applications():
        for widget in applications_frame.winfo_children():
            widget.destroy()
        c.execute('''SELECT * FROM leave_applications ORDER BY id DESC''')
        rows = c.fetchall()
        for row in rows:
            application_frame = tk.Frame(applications_frame)
            application_frame.pack(pady=10)
            name_label = tk.Label(
                application_frame, text=row[1], font=('Garamond', 12, 'bold'))
            name_label.pack()
            date_range_label = tk.Label(
                application_frame, text=row[2] + ' to ' + row[3], font=('Arial', 12))
            date_range_label.pack()
            reason_label = tk.Label(
                application_frame, text=row[4], font=('Arial', 12))
            reason_label.pack()
            status_label = tk.Label(
                application_frame, text=row[5], font=('Arial', 12))
            status_label.pack()
            if row[5] == 'Pending':
                approve_button = tk.Button(application_frame, text='Approve', font=(
                    'Arial', 12), command=lambda id=row[0]: approve_application(id))
                approve_button.pack(side=tk.LEFT, padx=10)
                reject_button = tk.Button(application_frame, text='Reject', font=(
                    'Arial', 12), command=lambda id=row[0]: reject_application(id))
                reject_button.pack(side=tk.LEFT, padx=10)

    # Create a function to approve a leave application


    def approve_application(id):
        c.execute(
            '''UPDATE leave_applications SET status='Approved' WHERE id=?''', (id,))
        conn.commit()
        B4=Button(
            root,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
            command= refresh_leave_applications()
        )

    # Create a function to reject a leave application


    def reject_application(id):
        c.execute(
            '''UPDATE leave_applications SET status='Rejected' WHERE id=?''', (id,))
        conn.commit()
        refresh_leave_applications()


    # Create the GUI elements for the leave application form and applications list
    root = tk.Tk()
    
    root.title('Leave Application System')
    root.maxsize(width=1500,height=1300)
    root.minsize(width=1500,height=1300)
    root.config(bg="#1A2238")

    form_frame = tk.Frame(root)
    form_frame.pack()

    
    applications_frame = tk.Frame(root)
    applications_frame.pack()

    # Refresh the leave applications list on startup
    refresh_leave_applications()
    

    # Run the main loop
    root.mainloop()

    # Close the database connection when the program is finished
    conn.close()
def student_feedback():
    root = Tk()
    root.title("Student Feedback")
    root.maxsize(width=600,height=400)
    root.minsize(width=600,height=400)
    root.config(bg="#1A2238")
    frame_header = ttk.Frame(root)
    frame_header.pack(pady=10)

    headerlabel = ttk.Label(frame_header, text='STUDENT FEEDBACK ', foreground='#FF6A3D',
                            font=('Arial', 24))
    headerlabel.grid(row=1, column=1)
    messagelabel = ttk.Label(frame_header,
                            text='PLEASE TELL US WHAT YOU THINK',
                            foreground='green', font=('Arial', 10))
    messagelabel.grid(row=2, column=1)

    frame_content = ttk.Frame(root)
    frame_content.pack()
    # def submit():
    #     username = entry_name.get()
    #     print(username)
    def back():
        root.destroy()
    myvar = StringVar()
    var = StringVar()
    # cmnt= StringVar()
    namelabel = ttk.Label(frame_content, text='Name')
    namelabel.grid(row=0, column=0, padx=5, sticky='sw')
    entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
    entry_name.grid(row=1, column=0)

    emaillabel = ttk.Label(frame_content, text='Email')
    emaillabel.grid(row=0, column=1, sticky='sw')
    entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
    entry_email.grid(row=1, column=1)

    commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 10))
    commentlabel.grid(row=2, column=0, sticky='sw')
    textcomment = Text(frame_content, width=55, height=10)
    textcomment.grid(row=3, column=0, columnspan=2)


    textcomment.config(wrap ='word')
    # def clear():
    #     textcomment.delete(1.0,'end')
    def clear():
        global entry_name
        global entry_email
        global textcomment
        messagebox.showinfo(title='clear', message='Do you want to clear?')
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)


    def submit():
        global entry_name
        global entry_email
        global textcomment
        print('Name:{}'.format(myvar.get()))
        print('Email:{}'.format(var.get()))
        print('Comment:{}'.format(textcomment.get(1.0, END)))
        messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        textcomment.delete(1.0, END)


    submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0, sticky='e')
    clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')
    back_button = tk.Button(root, text='back', font=(
        'Garamond', 16,'bold'),bg="#9DAAF2", command=back)
    back_button.pack(pady=20)
    back_button.place(x=250,y=350)
    mainloop()
def add_new_staff():
    fid = passw = conf_passw = name = ini = email = subcode1 = subcode2 = None


    '''
        LIST OF FUNCTIONS USED FOR VARIOUS FUNCTIONS THROUGH TKinter INTERFACE
            * create_treeview()
            * update_treeview()
            * parse_data()
            * update data()
            * remove_data()
            * show_passw()
    '''

    # create treeview (call this function once)
    def create_treeview():
        tree['columns'] = list(map(lambda x: '#' + str(x), range(1, 5)))
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("#1", width=70, stretch=tk.NO)
        tree.column("#2", width=200, stretch=tk.NO)
        tree.column("#3", width=80, stretch=tk.NO)
        tree.column("#4", width=80, stretch=tk.NO)
        tree.heading('#0', text="")
        tree.heading('#1', text="Fid")
        tree.heading('#2', text="Name")
        tree.heading('#3', text="Subject 1")
        tree.heading('#4', text="Subject 2")
        tree['height'] = 15


    # update treeview (call this function after each update)
    def update_treeview():
        for row in tree.get_children():
            tree.delete(row)
        cursor = conn.execute("SELECT FID, NAME, SUBCODE1, SUBCODE2 FROM FACULTY")
        for row in cursor:
            tree.insert(
                "",
                0,
                values=(row[0], row[1], row[2], row[3])
            )
        tree.place(x=530, y=100)


    # Parse and store data into database and treeview upon clcicking of the add button
    def parse_data():
        fid = str(fid_entry.get())
        passw = str(passw_entry.get())
        conf_passw = str(conf_passw_entry.get())
        name = str(name_entry.get()).upper()
        ini = str(ini_entry.get()).upper()
        email = str(email_entry.get())
        subcode1 = str(combo1.get())
        subcode2 = str(combo2.get())

        if fid == "" or passw == "" or \
            conf_passw == "" or name == "":
            messagebox.showwarning("Bad Input", "Some fields are empty! Please fill them out!")
            return

        if passw != conf_passw:
            messagebox.showerror("Passwords mismatch", "Password and confirm password didnt match. Try again!")
            passw_entry.delete(0, tk.END)
            conf_passw_entry.delete(0, tk.END)
            return

        if subcode1 == "NULL":
            messagebox.showwarning("Bad Input", "Subject 1 cant be NULL")
            return
        
        conn.execute(f"REPLACE INTO FACULTY (FID, PASSW, NAME, INI, EMAIL, SUBCODE1, SUBCODE2)\
            VALUES ('{fid}','{passw}','{name}', '{ini}', '{email}', '{subcode1}', '{subcode2}')")
        conn.commit()
        update_treeview()
        
        fid_entry.delete(0, tk.END)
        passw_entry.delete(0, tk.END)
        conf_passw_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        ini_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        combo1.current(0)
        combo2.current(0)
        

    # update a row in the database
    def update_data():
        fid_entry.delete(0, tk.END)
        passw_entry.delete(0, tk.END)
        conf_passw_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        ini_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        combo1.current(0)
        combo2.current(0)
        try:
            # print(tree.selection())
            if len(tree.selection()) > 1:
                messagebox.showerror("Bad Select", "Select one faculty at a time to update!")
                return

            q_fid = tree.item(tree.selection()[0])['values'][0]
            cursor = conn.execute(f"SELECT * FROM FACULTY WHERE FID = '{q_fid}'")

            cursor = list(cursor)
            fid_entry.insert(0, cursor[0][0])
            passw_entry.insert(0, cursor[0][1])
            conf_passw_entry.insert(0, cursor[0][1])
            name_entry.insert(0, cursor[0][2])
            ini_entry.insert(0, cursor[0][3])
            email_entry.insert(0, cursor[0][4])
            combo1.current(subcode_li.index(cursor[0][5]))
            combo2.current(subcode_li.index(cursor[0][6]))

            conn.execute(f"DELETE FROM FACULTY WHERE FID = '{cursor[0][0]}'")
            conn.commit()
            update_treeview()

        except IndexError:
            messagebox.showerror("Bad Select", "Please select a faculty from the list first!")
            return


    # remove selected data from databse and treeview
    def remove_data():
        if len(tree.selection()) < 1:
            messagebox.showerror("Bad Select", "Please select a faculty from the list first!")
            return
        for i in tree.selection():
            # print(tree.item(i)['values'][0])
            conn.execute(f"DELETE FROM FACULTY WHERE FID = '{tree.item(i)['values'][0]}'")
            conn.commit()
            tree.delete(i)
            update_treeview()


    # toggles between show/hide password
    def show_passw():
        if passw_entry['show'] == "●":
            passw_entry['show'] = ""
            B1_show['text'] = '●'
            B1_show.update()
        elif passw_entry['show'] == "":
            passw_entry['show'] = "●"
            B1_show['text'] = '○'
            B1_show.update()
        passw_entry.update()




    # main
    if __name__ == "__main__":  

        '''
            DATABASE CONNECTIONS AND SETUP
        '''

        # connecting database
        conn = sqlite3.connect(r'files/timetable.db')

        # creating Tabe in the database
        conn.execute('CREATE TABLE IF NOT EXISTS FACULTY\
        (FID CHAR(10) NOT NULL PRIMARY KEY,\
        PASSW CHAR(50) NOT NULL,\
        NAME CHAR(50) NOT NULL,\
        INI CHAR(5) NOT NULL,\
        EMAIL CHAR(50) NOT NULL,\
        SUBCODE1 CHAR(10) NOT NULL,\
        SUBCODE2 CHAR(10)    )')


        '''
            TKinter WINDOW SETUP WITH WIDGETS
                * Label(1-11)
                * Entry(6)
                * ComboBox(1-2)
                * Treeview(1)
                * Button(1-3)
        '''

        # TKinter Window
        subtk = Tk()
        subtk.title('Add/Update Faculties') 
        subtk.geometry('1000x550')
        subtk.maxsize(width=1000,height=550)
        subtk.iconbitmap('logo.ico')
        subtk.config(bg="#1A2238")

        # Label1
        tk.Label(
            subtk,
            text='List of Faculties',
            font=('Garamond', 20,'bold'),bg='#FF6A3D',fg="white"
        ).place(x=650, y=50)

        # Label2
        tk.Label(
            subtk,
            text='Add/Update Faculties',
            font=('Garamond', 20,'bold'),bg='#FF6A3D',fg="white"
        ).place(x=150, y=50)

        # Label3
        # Label4
        tk.Label(
            subtk,
            text='Faculty id:',
            font=('Garamond', 12),bg="#F4DB7D"
        ).place(x=100, y=130)

        # Entry1
        fid_entry = tk.Entry(
            subtk,
            font=('Garamond', 12),
            width=20
        )
        fid_entry.place(x=260, y=130)

        # Label5
        tk.Label(
            subtk,
            text='Password:',
            font=('Garamond', 12),bg="#F4DB7D"
        ).place(x=100, y=170)

        # Entry2
        passw_entry = tk.Entry(
            subtk,
            font=('Garamond', 12),
            width=20,
            show="●"
        )
        passw_entry.place(x=260, y=170)

        B1_show = tk.Button(
            subtk,
            text='○',
            font=('Consolas', 9, 'bold'),
            command=show_passw,bg="#F4DB7D"
        )
        B1_show.place(x=460,y=170)

        # Label6
        tk.Label(
            subtk,
            text='Confirm Password:',
            font=('Garamond', 12),bg="#F4DB7D"
        ).place(x=100, y=210)

        # Entry3
        conf_passw_entry = tk.Entry(
            subtk,
            font=('Garamond', 12),
            width=20,
            show="●"
        )
        conf_passw_entry.place(x=260, y=210)

        # Label7
        tk.Label(
            subtk,
            text='Faculty Name:',
            font=('Garamond', 12),bg="#F4DB7D"
        ).place(x=100, y=250)

        # Entry4
        name_entry = tk.Entry(
            subtk,
            font=('Garamond', 12),
            width=25,
        )
        name_entry.place(x=260, y=250)

        # Label8
        tk.Label(
            subtk,
            text='Initials:',
            font=('Garamond', 12),bg="#F4DB7D"
        ).place(x=100, y=290)

        # Entry5
        ini_entry = tk.Entry(
            subtk,
            font=('Garamond', 12),
            width=5,
        )
        ini_entry.place(x=260, y=290)

        # Label9
        tk.Label(
            subtk,
            text='Email:',
            font=('Garamond', 12),bg="#F4DB7D"
        ).place(x=100, y=330)

        # Entry6
        email_entry = tk.Entry(
            subtk,
            font=('Garamond', 12),
            width=25,
        )
        email_entry.place(x=260, y=330)

        # get subject code list from the database
        cursor = conn.execute("SELECT SUBCODE FROM SUBJECTS")
        subcode_li = [row[0] for row in cursor]
        subcode_li.insert(0, 'NULL')

        # Label10
        tk.Label(
            subtk,
            text='Subject 1:',
            font=('Garamond', 12),bg="#F4DB7D"
        ).place(x=100, y=370)

        # ComboBox1
        combo1 = ttk.Combobox(
            subtk,
            values=subcode_li,
        )
        combo1.place(x=260, y=370)
        combo1.current(0)

        # Label11
        tk.Label(
            subtk,
            text='Subject 2:',
            font=('Garamond', 12),bg="#F4DB7D"
        ).place(x=100, y=410)

        # ComboBox2
        combo2 = ttk.Combobox(
            subtk,
            values=subcode_li,
        )
        combo2.place(x=260, y=410)
        combo2.current(0)

        # Button1
        B1 = tk.Button(
            subtk,
            text='Add Faculty',
            font=('Garamond', 12),bg="#9DAAF2",
            command=parse_data
        )
        B1.place(x=100,y=465)

        # Button2
        B2 = tk.Button(
            subtk,
            text='Update Faculty',
            font=('Garamond', 12),bg="#9DAAF2",
            command=update_data
        )
        B2.place(x=350,y=465)

        # Treeview1
        tree = ttk.Treeview(subtk)
        create_treeview()
        update_treeview()

        # Button3
        B3 = tk.Button(
            subtk,
            text='Delete Faculty(s)',
            font=('Garamond', 12),bg="#9DAAF2",
            command=remove_data
        )
        B3.place(x=600,y=465)
        # Button4
        B4=Button(
            subtk,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
            command=subtk.destroy
        )
        B4.place(x=800,y=465,width=55)
        # looping Tkiniter window
        subtk.mainloop()
        conn.close() # close database after all operations

        
def hod_manager():
    root.destroy()
    hod=Tk()
    hod.title("HOD Manager")
    hod.maxsize(width=500,height=300)
    hod.minsize(width=500,height=300)
    hod.config(bg="#1A2238")
    hod.iconbitmap('logo.ico')
    headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
    sublabelfont = ("Noto Sans CJK TC", 15)
    labelfont = ('Garamond', 14)
    entryfont = ('Garamond', 12)
    #Hod pin = 4556
    CORRECT_PIN = "4556"
    def check_pin(pin_entry):
        if pin_entry.get() == CORRECT_PIN:
            login_successful()
        else:
            invalid_pin()
    # Define a function to display a "Login Successful" message
    def login_successful():
        # Close the login window
        # Close the login window
        hod=Tk()
        hod.title("HOD Manager")
        hod.maxsize(width=1550,height=1080)
        hod.minsize(width=1550,height=1080)
        hod.config(bg="#1A2238")
        hod.iconbitmap('logo.ico')
        headlabelfont = ("Noto Sans CJK TC", 15, 'bold')   
        sublabelfont = ("Noto Sans CJK TC", 15)
        labelfont = ('Garamond', 14)    
        entryfont = ('Garamond', 12)
        def add():
            pass
        my_menu=Menu(hod)
        hod.config(menu=my_menu)
        file_menu=Menu(my_menu,bg="#FF6A3D",fg="White")#drop down color
        #creted top header menu
        #Adding drop down in each option for student
        staff_menu=Menu(my_menu,bg="#FF6A3D",fg="White")
        my_menu.add_cascade(label="Staff",menu=staff_menu)
        staff_menu.add_cascade(label="Add new staff member",command=add_new_staff)
        staff_menu.add_separator()#Adding a line after a block
        staff_menu.add_cascade(label="view staff list",command=add)
        staff_menu.add_separator()
        staff_menu.add_cascade(label="Staff leave",command=add)
        staff_menu.add_separator()
        staff_menu.add_cascade(label="Staff feedback",command=add)
        staff_menu.add_separator()
        time_=Label(hod,text="View time tables",bg="#FF6A3D",fg="White",width=55,height=1,font=('Garamond', 42,'bold')).pack()
    def invalid_pin():
        pin_entry.delete(0, "end") # Clear the PIN entry field
        error_label = Label(hod, text="Invalid PIN. Please try again.", fg="red")
        error_label.pack(padx=20, pady=5)
        error_label.place(x=180,y=250)
    pin_entry = Entry(hod, show="*")
    pin_entry.pack(padx=20, pady=5)
    pin_entry.place(x=200,y=100)
    #submit_button = Button(hod, text="Submit", command=login_successful)
    submit_button=Button(hod,text="Login",bg="#9DAAF2",bd = 1,fg="Black",command=lambda: check_pin(pin_entry),width=10,height=0,font=("Times new roman", 15))
    submit_button.pack(padx=20, pady=20)
    submit_button.place(x=200,y=150)
    exit=Button(
            hod,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
            command=hod.destroy
        )
    exit.place(x=400,y=250,width=55)
    
    hod.mainloop()
Hod_login = Button(root,text="HOD Login",bg="#FF6A3D",fg="White",width=0,height=1,font=("Times new roman", 15),command=hod_manager)#B is capital
Hod_login.place(x=490,y=600)
Staff_login = Button(root,text="Staff Login",bg="#FF6A3D",fg="White",width=10,height=1,font=("Times new roman", 15),command=staff_manager)
Staff_login.place(x=725,y=600)
student_login = Button(root,text="Student Login",bg="#FF6A3D",fg="White",width=10,height=1,font=("Times new roman", 15),command=student_manager)
student_login.place(x=975,y=600)
def after_save():
    root = Tk()
    root.title("Homepage")
    root.geometry('1550x1080')
    root.maxsize(width=1550,height=1080)
    root.minsize(width=1550,height=1080)
    root.config(bg="#1A2238")
    root.iconbitmap('Logo.ico')
    headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
    sublabelfont = ("Noto Sans CJK TC", 15)
    labelfont = ('Garamond', 14)
    entryfont = ('Garamond', 12)
    logo = PhotoImage(file="logo.png")
    logo_label=Label(image=logo)
    logo_label.place(x=410,y=100)
    #For jpg use Image.open("Address")
    #register
    def register():
        exec(open('main.py').read())

    def student_leave():
        conn = sqlite3.connect('leave_applications.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS leave_applications (id INTEGER PRIMARY KEY, name TEXT, from_date TEXT, to_date TEXT, reason TEXT, status TEXT)''')
        conn.commit()

        # Create a function to submit the leave application form


        def submit_application():
                success=Label(root,text="You application succesffuly submitted!!",fg="#FF6A3D")
                success.place(x=150,y=350)
                status = 'Pending'
                c.execute('''INSERT INTO leave_applications (name, from_date, to_date, reason, status) VALUES (?, ?, ?, ?, ?)''',
                        (status))
                conn.commit()
        def back():
            root.destroy()
        # Create a function to refresh the leave applications list with the latest applications from the database



        # Create a function to approve a leave application

        # Create the GUI elements for the leave application form and applications list
        root = tk.Tk()
        root.title('Leave Application')
        root.maxsize(width=500,height=400)
        root.minsize(width=500,height=400)
        root.config(bg="#1A2238")

        app=Label(root,
                text='Leave application',
                font=('Garamond', 20,'bold'),bg='#FF6A3D',fg="white"
            ).pack(side=TOP, fill=X,pady=10)
        name_label = tk.Label(root, text='Name:', font=('Garamond', 12,'bold'),bg="#F4DB7D")
        name_label.place(x=150,y=100)
        name_entry = tk.Entry(root, font=('Garamond', 12))
        name_entry.place(x=220,y=100)


        from_date_label = tk.Label(
        root, text='From Date (dd/mm/yyyy):', font=('Garamond', 12,'bold'),bg="#F4DB7D")
        from_date_label.place(x=10,y=150)
        from_date_entry = tk.Entry(root, font=('Garamond', 12))
        from_date_entry.place(x=220,y=150)

        to_date_label = tk.Label(
            root, text='To Date (dd/mm/yyyy):', font=('Garamond', 12,'bold'),bg="#F4DB7D")
        # to_date
        to_date_label.place(x=30,y=200)
        to_date_entry = tk.Entry(root, font=('Garamond', 12))
        to_date_entry.place(x=220,y=200)

        reason_label = tk.Label(root, text='Reason:', font=('Garamond', 12,'bold'),bg="#F4DB7D")
        reason_label.place(x=150,y=250)
        reason_entry = tk.Entry(root, font=('Garamond', 12))
        reason_entry.place(x=220,y=250)

        submit_button = tk.Button(root, text='Submit', font=(
            'Garamond', 16,'bold'),bg="#9DAAF2", command=submit_application)
        submit_button.pack(pady=20)
        submit_button.place(x=150,y=300)
        back_button = tk.Button(root, text='back', font=(
            'Garamond', 16,'bold'),bg="#9DAAF2", command=back)
        back_button.pack(pady=20)
        back_button.place(x=250,y=300)

        applications_frame = tk.Frame(root)
        applications_frame.pack()

        # Refresh the leave applications list on startup

        # Run the main loop
        root.mainloop()

        # Close the database connection when the program is finished
        conn.close()

    def student_manager():
        root.destroy()
        hod=Tk()
        hod.title("Students")
        hod.maxsize(width=500,height=300)
        hod.minsize(width=500,height=300)
        hod.config(bg="#1A2238")
        hod.iconbitmap('logo.ico')
        headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
        sublabelfont = ("Noto Sans CJK TC", 15)
        labelfont = ('Garamond', 14)
        entryfont = ('Garamond', 12)
        t2=Label(hod,text="Enter your safety pin for Authentication",fg="#FF6A3D",bg="#1A2238",font = ("Garamond", 15, 'bold'))
        t2.place(x=100,y=50)
        #Hod pin = 5228
        CORRECT_PIN = "5228"
        def check_pin(pin_entry):
            if pin_entry.get() == CORRECT_PIN:
                login_successful()
            else:
                invalid_pin()
        # Define a function to display a "Login Successful" message
        def login_successful():
            # Close the login window
            # Close the login window
            t2=Label(hod,text="You logged in successfully")
        def invalid_pin():
            pin_entry.delete(0, "end") # Clear the PIN entry field
            error_label = Label(hod, text="Invalid PIN. Please try again.", fg="red")
            error_label.pack(padx=20, pady=5)
            error_label.place(x=180,y=250)
        pin_entry = Entry(hod, show="*")
        pin_entry.pack(padx=20, pady=5)
        pin_entry.place(x=200,y=100)
        #submit_button = Button(hod, text="Submit", command=login_successful)
        submit_button=Button(hod,text="Login",bg="#9DAAF2",bd = 1,fg="Black",command=lambda: check_pin(pin_entry),width=10,height=0,font=("Times new roman", 15))
        submit_button.pack(padx=10, pady=20)
        submit_button.place(x=200,y=150)
        exit=Button(
                hod,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
                command=hod.destroy
            )
        exit.place(x=350,y=250,width=55)

    def staff_manager():
        root.destroy()
        hod=Tk()
        hod.title("Staff Manager")
        hod.maxsize(width=500,height=300)
        hod.minsize(width=500,height=300)
        hod.config(bg="#1A2238")
        hod.iconbitmap('logo.ico')
        headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
        sublabelfont = ("Noto Sans CJK TC", 15)
        labelfont = ('Garamond', 14)
        entryfont = ('Garamond', 12)
        #Hod pin = 4556
        CORRECT_PIN = "2885"
        def check_pin(pin_entry):
            if pin_entry.get() == CORRECT_PIN:
                login_successful()
            else:
                invalid_pin()
        # Define a function to display a "Login Successful" message
        def login_successful():
            # Close the login window
            # Close the login window
            hod=Tk()
            hod.title("Staff Manager")
            hod.maxsize(width=1800,height=1080)
            hod.minsize(width=1000,height=1080)
            hod.config(bg="#1A2238")
            hod.iconbitmap('logo.ico')
            headlabelfont = ("Noto Sans CJK TC", 15, 'bold')   
            sublabelfont = ("Noto Sans CJK TC", 15)
            labelfont = ('Garamond', 14)    
            entryfont = ('Garamond', 12)
            def add():
                pass
            my_menu=Menu(hod)
            hod.config(menu=my_menu)
            file_menu=Menu(my_menu,bg="#FF6A3D",fg="White")#drop down color
            my_menu.add_cascade(label="Student",menu=file_menu)#creted top header menu
            #Adding drop down in each option for student
            file_menu.add_cascade(label="Add new student",command=add_new_student)
            file_menu.add_separator()#Adding a line after a block
            file_menu.add_cascade(label="Attendance",command=student_Attendance) 
            file_menu.add_separator()
            file_menu.add_cascade(label="Results",command=results)
            file_menu.add_separator()
            file_menu.add_cascade(label="Student leave",command=leave)
            file_menu.add_separator()
            file_menu.add_cascade(label="Student feedback",command=student_feedback)
            file_menu.add_separator()
            edit_menu=Menu(my_menu,bg="#FF6A3D",fg="White")
            my_menu.add_cascade(label="Class data",menu=edit_menu)
            #Adding drop down in each option for student
            #Adding a line after a block
            edit_menu.add_cascade(label="Add Assignment",command=file)
            edit_menu.add_separator()
            edit_menu.add_cascade(label="Add Results",command=add)
            edit_menu.add_separator()
            staff_menu=Menu(my_menu,bg="#FF6A3D",fg="White")
        def invalid_pin():
            pin_entry.delete(0, "end") # Clear the PIN entry field
            error_label = Label(hod, text="Invalid PIN. Please try again.", fg="red")
            error_label.pack(padx=20, pady=5)
            error_label.place(x=180,y=250)
        pin_entry = Entry(hod, show="*")
        pin_entry.pack(padx=20, pady=5)
        pin_entry.place(x=200,y=100)
        #submit_button = Button(hod, text="Submit", command=login_successful)
        submit_button=Button(hod,text="Login",bg="#9DAAF2",bd = 1,fg="Black",command=lambda: check_pin(pin_entry),width=10,height=0,font=("Times new roman", 15))
        submit_button.pack(padx=20, pady=20)
        submit_button.place(x=200,y=150)
        exit=Button(
                hod,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
                command=hod.destroy
            )
        exit.place(x=400,y=250,width=55)
        
    def file():
        file = Tk()
        file.geometry('1000x1080')
        file.maxsize(width=1800,height=1080)
        file.minsize(width=1000,height=1080)
        file.config(background="#1A2238")
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
            f1 = Frame(file, background="grey")
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
            f = Frame(file, background="white")
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
            f1 = Frame(file, background="grey")
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
            f1=Frame(file)
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
            f1 = Frame(file, width=350, height=300, background="lavender")
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


        lbl_heading = Label(file, text="File Management system",font=("bold",18),fg="gold2",bg='black')
        lbl_heading.grid(row=1, column=1, pady=20, padx=20)

        open_btn = Button(file, text="Open File",command=open_file, width=15,font=('bold',14))
        open_btn.grid(row=2, column=0,pady=20, padx=20)

        delete_btn = Button(file, text="Delete File",command=delete_file, width=15,font=('bold',14))
        delete_btn.grid(row=2, column=1,pady=20, padx=20)

        rename_btn = Button(file, text="Rename File", command=rename_file, width=15,font=('bold',14))
        rename_btn.grid(row=2, column=2,pady=20, padx=20)

        copy_move_btn = Button(file, text="Copy/Move File", command=copy_move_file, width=15,font=('bold',14))
        copy_move_btn.grid(row=2, column=3,pady=20, padx=20)

        create_folder_btn = Button(file, text="Create folder", command=create_folder, width=15,font=('bold',14))
        create_folder_btn.grid(row=3, column=0, pady=20, padx=20)

        deletefolder_btn = Button(file, text="Delete folder", command=deletefolder, width=15,font=('bold',14))
        deletefolder_btn.grid(row=3, column=1, pady=20, padx=20)

        rename_folder_btn = Button(file, text="Rename Folder", command=rename_folder, width=15,font=('bold',14))
        rename_folder_btn.grid(row=3, column=2,pady=20, padx=20)

        view_btn = Button(file, text="View folder contents", command=view_folder, width=15,font=('bold',14))
        view_btn.grid(row=3, column=3, pady=20, padx=20)

        exit_btn = Button(file, text="Exit", command=file.destroy, width=12,font=('bold',14))
        exit_btn.grid(row=4, column=1, pady=20, padx=20)

        file.mainloop()
    def add_new_student():
        def studentinfo():
            class Student_Information():
                    def __init__(self, master):
                            self.master = master
                            self.master.title('Student Information')
                            root.geometry('850x650')
                            root.maxsize(width=850,height=650)
                            root.config(bg="#1A2238")
                            root.iconbitmap('Logo.ico')
                            
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
                                                College_Std_info_BackEnd.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                                    self.gender.get())
                                                self.listbox.delete(0, END)
                                                self.listbox.insert(END, (self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
                                                                            self.gender.get()))
                                        
                                    '''def Display():
                                        self.listbox.delete(0, END)
                                        for row in College_Std_info_BackEnd.view():
                                                self.listbox.insert(END, row, str(' '))'''


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
                                                College_Std_info_BackEnd.delete(selected_tuple[0])
                                                Reset()
                                                #Display()


                                    def Search():
                                        self.listbox.delete(0, END)
                                        for row in College_Std_info_BackEnd.search(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), self.gender.get()):
                                                self.listbox.insert(END, row, str(' '))
                                                

                                    def Update():
                                        if(len(self.name.get()) != 0):
                                                College_Std_info_BackEnd.delete(selected_tuple[0])
                                                if(len(self.name.get()) != 0):
                                                        College_Std_info_BackEnd.insert(self.name.get(), self.father_name.get(), self.mother_name.get(), self.address.get(), self.mobileno.get(), self.email_address.get(), self.date_of_birth.get(), \
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
                                    self.BUTTON_DELETE = Button(self.Student_Frame_3, text ='DELETE', font = ('arial', 17, 'bold'), width = 8, command = Delete,bg="#9DAAF2")
                                    self.BUTTON_DELETE.grid(row = 0, column = 4, padx = 10, pady = 10)
                                    self.BUTTON_SEARCH = Button(self.Student_Frame_3, text ='SEARCH', font = ('arial', 17, 'bold'), width = 8, command = Search,bg="#9DAAF2")
                                    self.BUTTON_SEARCH.grid(row = 0, column = 5, padx = 10, pady = 10)
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
        studentinfo()
    def student_Attendance():
        pass
    def results():
        pass
    student_login = Button(root,text="Login",bg="#FF6A3D",fg="White",width=15,height=1,font=("Times new roman", 30),command=student_manager)
    student_login.place(x=500,y=600)
    root.mainloop()
root.mainloop()
