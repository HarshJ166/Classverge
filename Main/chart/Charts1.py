import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV file
data = pd.read_csv('C:/Users/meetj/Desktop/Classverge/Mini project/chart/read.csv')
# Get the name of the student from the user
Name = input("Enter the name of the student: ")
# Filter data for the entered student name
student_data = data[data['Name'] == Name]
# Check if there is any data for the entered student name
if student_data.empty:
    print(f"No data found for {Name}. Please try again.")
    exit()

# Create a bar chart of the student's performance data
fig, ax = plt.subplots()
ax.bar(student_data['Physics Marks'], student_data['Study Hours'])
ax.set_title(f"Performance for {Name}")
ax.set_xlabel('Physics Marks')
ax.set_ylabel('Study Hours')
plt.show()


