from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter as tk
import cv2
#import util
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
root = Tk()
root.title("Classverge")
root.geometry('1520x1080')
root.maxsize(width=1520,height=1080)
root.minsize(width=1520,height=1080)
root.config(bg="#1A2238")
root.iconbitmap('Logo.ico')
logo = PhotoImage(file="logo.png")
logo_label=Label(image=logo)
logo_label.place(x=410,y=100)
def studentdata():
    st=Tk()
    st.title("Students")
    st.maxsize(width=500,height=300)
    st.minsize(width=500,height=300)
    st.config(bg="#1A2238")
    st.iconbitmap('logo.ico')
    pin=Label(st,text="Enter your safety pin for Authentication",fg="#FF6A3D",bg="#1A2238",font = ("Garamond", 15, 'bold'))
    pin.place(x=100,y=50)
    CORRECT_PIN = "5228"
    def check_pin(pin_entry):
        if pin_entry.get() == CORRECT_PIN:
            login_successful()
        else:
            invalid_pin()
    def login_successful():
        def register():
            pass
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
    def invalid_pin():
        pin_entry.delete(0, "end") # Clear the PIN entry field
        error_label = Label(st, text="Invalid PIN. Please try again.", fg="red")
        error_label.pack(padx=20, pady=5)
        error_label.place(x=180,y=250)
    pin_entry = Entry(st, show="*")
    pin_entry.pack(padx=20, pady=5)
    pin_entry.place(x=200,y=100)
    #submit_button = Button(st, text="Submit", command=login_successful)
    submit_button=Button(st,text="Login",bg="#9DAAF2",bd = 1,fg="Black",command=lambda: check_pin(pin_entry),width=10,height=0,font=("Times new roman", 15))
    submit_button.pack(padx=20, pady=20)
    submit_button.place(x=200,y=150)
    exit=Button(
            st,text="Exit",font=('Garamond', 12),bg="#9DAAF2",
            command=st.destroy
        )
    exit.place(x=350,y=250,width=55)
    st.mainloop()
student= Button(root,text="Register As Student",bg="#FF6A3d",fg="#FFF",width=0,height=1,font=("Times new roman", 15),command=studentdata)
student.place(x=300,y=650)
root.mainloop()