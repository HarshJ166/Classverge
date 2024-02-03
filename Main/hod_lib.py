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

def library():
    os.system('py College-Management_System\College_Library_Frontend.py')


lib=Button(text="College Library",width=20,height=1,font = ('Times New Roman',22,'bold'),bg="#FF6A3D",fg="White",command=library)