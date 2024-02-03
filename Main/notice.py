from tkinter import *
# Create the main window
def notice():
    root = Tk()
    root.title("Notice Board")
    root.geometry("500x500")

    # Create the label for the notice board
    notice_board_label = Label(root, text="Notice Board", font=("Arial", 16))
    notice_board_label.pack()

    # Create the text box for the notices
    notice_text_box = Text(root, height=10, width=50)
    notice_text_box.pack()

    # Create the button to submit a notice


    def submit_notice():
        notice = notice_text_box.get("1.0", END)
        # Here, you can add code to save the notice to a database or file
        print("Notice submitted:", notice)


    submit_button = Button(root, text="Submit Notice", command=submit_notice)
    submit_button.pack()

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