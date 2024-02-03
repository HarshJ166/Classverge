import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys

fid = passw = conf_passw = name = roll = section = None


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
    tree.heading('#1', text="sid")
    tree.heading('#2', text="Name")
    tree.heading('#3', text="Roll")
    tree.heading('#4', text="Section")
    tree['height'] = 12


# update treeview (call this function after each update)
def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    cursor = conn.execute("SELECT SID, NAME, ROLL, SECTION FROM STUDENT")
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
    name = str(name_entry.get()).upper()
    roll = str(roll_entry.get())
    section = str(sec_entry.get()).upper()

    if fid == "" or passw == "" or \
        conf_passw == "" or name == "" or \
        roll == "" or section == "":
        messagebox.showwarning("Bad Input", "Some fields are empty! Please fill them out!")
        return

    if passw != conf_passw:
        messagebox.showerror("Passwords mismatch", "Password and confirm password didnt match. Try again!")
        return
  
    conn.execute(f"REPLACE INTO STUDENT (SID, PASSW, NAME, ROLL, SECTION)\
        VALUES ('{fid}','{passw}','{name}', '{roll}', '{section}')")
    conn.commit()
    update_treeview()
    
    fid_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    sec_entry.delete(0, tk.END)
    

# update a row in the database
def update_data():
    fid_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    sec_entry.delete(0, tk.END)
    try:
        # print(tree.selection())
        if len(tree.selection()) > 1:
            messagebox.showerror("Bad Select", "Select one student at a time to update!")
            return

        q_fid = tree.item(tree.selection()[0])['values'][0]
        cursor = conn.execute(f"SELECT * FROM STUDENT WHERE SID = '{q_fid}'")

        cursor = list(cursor)
        fid_entry.insert(0, cursor[0][0])
        name_entry.insert(0, cursor[0][2])
        roll_entry.insert(0, cursor[0][3])
        sec_entry.insert(0, cursor[0][4])
        
        conn.execute(f"DELETE FROM STUDENT WHERE SID = '{cursor[0][0]}'")
        conn.commit()
        update_treeview()

    except IndexError:
        messagebox.showerror("Bad Select", "Please select a student from the list first!")
        return


# remove selected data from databse and treeview
def remove_data():
    if len(tree.selection()) < 1:
        messagebox.showerror("Bad Select", "Please select a student from the list first!")
        return
    for i in tree.selection():
        # print(tree.item(i)['values'][0])
        conn.execute(f"DELETE FROM STUDENT WHERE SID = '{tree.item(i)['values'][0]}'")
        conn.commit()
        tree.delete(i)
        update_treeview()
def exit():
    subtk.destroy()





# main
if __name__ == "__main__":  

    '''
        DATABASE CONNECTIONS AND SETUP
    '''

    # connecting database
    conn = sqlite3.connect(r'files/timetable.db')

    # creating Tabe in the database
    conn.execute('CREATE TABLE IF NOT EXISTS STUDENT\
    (SID CHAR(10) NOT NULL PRIMARY KEY,\
    PASSW CHAR(50) NOT NULL,\
    NAME CHAR(50) NOT NULL,\
    ROLL INTEGER NOT NULL,\
    SECTION CHAR(5) NOT NULL)')


    '''
        TKinter WINDOW SETUP WITH WIDGETS
            * Label(1-11)
            * Entry(6)
            * ComboBox(1-2)
            * Treeview(1)
            * Button(1-3)
    '''

    # TKinter Window
    subtk = tk.Tk()
    subtk.geometry('1000x470')
    subtk.title('Add/Update Students')
    subtk.iconbitmap('logo.ico')
    subtk.config(bg = '#1A2238')

    # Label1
    tk.Label(
        subtk,
        text='List of Students',
        bg = '#1A2238',fg="#F4DB7D",
        font=('Consolas', 20, 'bold')
    ).place(x=620, y=50)

    # Label2
    tk.Label(
        subtk,
        text='Add/Update Students',
        bg = '#1A2238',fg="#F4DB7D",
        font=('Consolas', 20, 'bold')
    ).place(x=110, y=50)

    # Label3
    tk.Label(
        subtk,
        text='Add information in the following prompt!',
        font=('Consolas', 10, 'italic'),
        fg="#9DAAF2",bg = '#1A2238',
    ).place(x=110, y=85)

    # Label4
    tk.Label(
        subtk,
        text='Student id:',
        bg = '#1A2238',fg="#FF6A3d",
        font=('Consolas', 12)
    ).place(x=100, y=130)

    # Entry1
    fid_entry = tk.Entry(
        subtk,
        font=('Consolas', 12),
        width=20
    )
    fid_entry.place(x=260, y=130)

    # # Label5
    # tk.Label(
    #     subtk,
    #     text='Password:',
    #     font=('Consolas', 12)
    # ).place(x=100, y=170)

    # # Entry2
    # passw_entry = tk.Entry(
    #     subtk,
    #     font=('Consolas', 12),
    #     width=20,
    #     show="●"
    # )
    # passw_entry.place(x=260, y=170)

    # B1_show = tk.Button(
    #     subtk,
    #     text='○',
    #     font=('Consolas', 9, 'bold'),
    #     command=show_passw
    # )
    # B1_show.place(x=460,y=170)

    # # Label6
    # tk.Label(
    #     subtk,
    #     text='Confirm Password:',
    #     font=('Consolas', 12)
    # ).place(x=100, y=210)

    # # Entry3
    # conf_passw_entry = tk.Entry(
    #     subtk,
    #     font=('Consolas', 12),
    #     width=20,
    #     show="●"
    # )
    # conf_passw_entry.place(x=260, y=210)

    # Label7
    tk.Label(
        subtk,
        text='Student Name:',
        bg = '#1A2238',fg="#FF6A3d",
        font=('Consolas', 12)
    ).place(x=100, y=190)

    # Entry4
    name_entry = tk.Entry(
        subtk,
        font=('Consolas', 12),
        width=25,
    )
    name_entry.place(x=260, y=190)

    # Label8
    tk.Label(
        subtk,
        text='Roll no.:',
        bg = '#1A2238',fg="#FF6A3D",
        font=('Consolas', 12)
    ).place(x=100, y=250)

    # Entry5
    roll_entry = tk.Entry(
        subtk,
        font=('Consolas', 12),
        width=5,
    )
    roll_entry.place(x=260, y=250)

    # Label9
    tk.Label(
        subtk,
        text='Section:',
        bg = '#1A2238',fg="#FF6A3D",
        font=('Consolas', 12)
    ).place(x=100, y=310)

    # Entry6
    sec_entry = tk.Entry(
        subtk,
        font=('Consolas', 12),
        width=5,
    )
    sec_entry.place(x=260, y=310)

    # Button1
    B1 = tk.Button(
        subtk,
        text='Add Student',
        bg="#9DAAF2",fg ='Black',
        font=('Consolas', 12),
        command=parse_data
    )
    B1.place(x=150,y=400)

    # Button2
    B2 = tk.Button(
        subtk,
        text='Update Student',
        bg="#9DAAF2",fg = 'Black',
        font=('Consolas', 12),
        command=update_data
    )
    B2.place(x=350,y=400)

    # Treeview1
    tree = ttk.Treeview(subtk)
    create_treeview()
    update_treeview()

    # Button3
    B3 = tk.Button(
        subtk,
        text='Delete Student(s)',
        bg="#9DAAF2",fg = 'Black',
        font=('Consolas', 12),
        command=remove_data
    )
    B3.place(x=550,y=400)
    
    #Button4
    B4 = tk.Button(
        subtk,
        text='Exit',
        bg="#9DAAF2",fg = 'Black',
        font=('Consolas', 12),command=exit
    )
    B4.place(x=780,y=400)

    # looping Tkiniter window
    subtk.mainloop()
    conn.close() # close database after all operations
