import tkinter as tk
import pandas as pd
from tkinter import filedialog
import matplotlib.pyplot as plt

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
root.iconbitmap('logo.ico')
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
