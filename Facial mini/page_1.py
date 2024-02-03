import numpy as np
import cv2
import pickle
import os
from pyzbar.pyzbar import decode
from tkinter import *
from PIL import ImageTk, Image 
from datetime import datetime
import subprocess

def facerecognizer():
    # Open the main program file
    main_program_file = 'main.py'
    process = subprocess.Popen(['python', main_program_file])
    facetrain()
    face_cascade=cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
    eye_cascade=cv2.CascadeClassifier('cascades\data\haarcascade_eye.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")
    labels = {"person_name": 2}
    with open("labels.pickle",'rb') as f:
        og_labels=pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}
    cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while(True):
        #capture frame by frame
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
        #Axis for faces
        for (x,y,w,h) in faces:
            roi_gray=gray[y:y+h,x:x+w] #ycord-start, ycord-end
            roi_color=frame[y:y+h,x:x+w]
            #recognize? deep learned model predict keras tensorflow pytorch scikit learn
            id_,conf = recognizer.predict(roi_gray)
            if conf>=45:# and conf <=85:
                font=cv2.FONT_HERSHEY_SIMPLEX
                name=labels[id_]
                color=(255,255,255)
                stroke=2
                cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
            color=(255,0,0) #BGR 0-255
            stroke=2
            end_cord_x=x+w
            end_cord_y=y+h
            cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)
            eyes=eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        font=cv2.FONT_HERSHEY_SIMPLEX
        now = datetime.now()
        start = now.strftime("%Y-%m-%d %I:%M:%S")
        cv2.putText(frame,"Enter q to exit",(10,70), font, 1,(255,255,255),2,cv2.LINE_AA)
        cv2.putText(frame,start,(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
        #display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(20)&0xFF==ord('q'):
            break
    # When everything is done , release the capture
    cap.release()
    cv2.destroyWindow('frame')
def facetrain():
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    image_dir=os.path.join(BASE_DIR,"images")
    face_cascade=cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    current_id=0
    label_ids={}
    x_train=[]
    y_labels=[]
    for root,dirs,files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root,file)
                label=os.path.basename(root).replace(" ",".").lower()
                if not label in label_ids:
                    label_ids[label]=current_id
                    current_id += 1
                id_=label_ids[label]
                pil_image=Image.open(path).convert("L")#grayscale
                size=(550,550)
                final_image = pil_image.resize(size, Image.ANTIALIAS)
                image_array=np.array(final_image,"uint8")
                faces=face_cascade.detectMultiScale(image_array,minNeighbors=5)
                for (x,y,w,h) in faces:
                    roi=image_array[y:y+h,x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)
    with open("labels.pickle",'wb') as f:
        pickle.dump(label_ids,f)
    recognizer.train(x_train,np.array(y_labels))
    recognizer.save("trainner.yml")
def scan(name,value):
    face_cascade=cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
    eye_cascade=cv2.CascadeClassifier('cascades\data\haarcascade_eye.xml')
    cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
    loop2=0
    while loop2==0:
        #capture frame by frame
        ret,frame=cap.read()
        if(frame is not None):
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
        #Axis for faces
        for (x,y,w,h) in faces:
            roi_gray=gray[y:y+h,x:x+w] #ycord-start, ycord-end
            if(frame is not None):
                roi_color=frame[y:y+h,x:x+w]
            img_item='images/'+name+'/'+value+'.png'
            cv2.imwrite(img_item,roi_color)         
        loop1=0
        while loop1==0:
            #display the resulting frame
            try:
                cv2.imshow('frame',frame)
            except:
                loop1=1
                loop2=1
            try:
                f=open('images/'+name+'/'+value+'.png','r')
                f.close()
            except:
                pass
            else:
                cv2.waitKey(2000)
                cap.release()
                # cv2.destroyWindow('frame')
            if cv2.waitKey(2):
                break
def changenamestate(name):
    name2=name.lower()
    passname=name2.replace(" ","-")
    return passname
def checkperson(name):
    try:
        f=open('person/'+name+'.txt','r')
    except:
        return False
    else:
        f.close()
        return True

def createperson(name):
    f=open('person/'+name+'.txt','w')
    f.close()
    os.mkdir('images/'+name)
def getnoofpictures(name):
    val=0
    while val!=-1:
        val=val+1
        value=str(val)
        try:
            f=open('images/'+name+'/'+value+'.png','r')
        except:
            return val
        else:
            f.close()
def smallwindow():
	def display():
		n=entry_1.get()
		r.destroy()
		name=changenamestate(n)
		if checkperson(name):
			pass
		else:
			createperson(name)
		if getnoofpictures(name)<=10:
			while getnoofpictures(name)<=10:
				val=getnoofpictures(name)
				value=str(val)
				scan(name,value)
		else:
			val=getnoofpictures(name)
			value=str(val)
			scan(name,value)
		facetrain()
	r = Tk()
	r.geometry('215x75')
	r.title("Scan.")
	r.iconbitmap('gui_images/hacker.ico')
	label_1 = Label(r, text="Full Name:",width=20,font=("bold", 10))
	label_1.place(x=-45,y=10)
	entry_1 = Entry(r)
	entry_1.place(x=80,y=10)
	Button(r, text='Submit',width=10,bg='brown',fg='white', command=display).place(x=125,y=40)
	r.mainloop()
class secondpage:
    def __init__ (self,root):
        self.bg1=ImageTk.PhotoImage(file='gui_images/black_bg.png')
        self.my_canvas=Canvas(root,height=1400, width=1020)
        self.my_canvas.pack(fill = "both",expand=True)
        self.my_canvas.create_image(0,0, image=self.bg1,anchor="nw")
        self.my_canvas.create_text(650,95, text = "Face Recognition",font=("Times",55),fill='white')
        def change(e):
            self.bg5 = ImageTk.PhotoImage(file="gui_images/scan_big.png")
            self.b1.config(image = self.bg5)
            self.b1.image = self.bg5
        def change_1(e):	
            self.bg6 = ImageTk.PhotoImage(file="gui_images/recognize_big.png")
            self.b2.config(image = self.bg6)
            self.b2.image = self.bg6
        def change_back(e):
            self.bg5 = ImageTk.PhotoImage(file="gui_images/scan.png")
            self.b1.config(image = self.bg5)
            self.b1.image = self.bg5
        def change_back_1(e):	
            self.bg6 = ImageTk.PhotoImage(file="gui_images/recognize.png")
            self.b2.config(image = self.bg6)
            self.b2.image = self.bg6

        self.bg2 = ImageTk.PhotoImage(file='gui_images/scan.png')
        self.bg3 = ImageTk.PhotoImage(file='gui_images/recognize.png')
        
        self.my_canvas.create_text(375,500,text="SCAN",fill = "white" ,font=("Times",20,"bold"))
        self.my_canvas.create_text(875,500, text="RECOGNISE" ,fill = "white" ,font=("Times",20,"bold"))
        
        self.b1 = Button(root, image = self.bg2, command=smallwindow)#scan
        self.b2 = Button(root,  image = self.bg3, command=facerecognizer)#recognize
        def func11():
            root.destroy()
        def func22():
            pass
        self.b3 = Button(root, command=lambda: [func11(),func22()])#info
        self.b4 = Button(root, text="EXIT" ,font=("Times",15,"bold"),command=root.destroy)
        self.b1.configure(width=170,height=170,background = "black",activebackground = "#e60e5d",borderwidth=0)
        b1_window = self.my_canvas.create_window(293,250,anchor="nw",window=self.b1)
        self.b2.configure(width=170,height=170,background = "black",activebackground = "#e60e5d",borderwidth=0)
        b2_window = self.my_canvas.create_window(780,250,anchor="nw",window=self.b2)
        self.b3.configure(width=170,height=170,background = "black",activebackground = "#e60e5d",borderwidth=0)
        b3_window = self.my_canvas.create_window(1026,250,anchor="nw",window=self.b3)
        self.b4.configure(width=15,height=1,background = "#fff",activebackground = "#000",borderwidth=5)
        b4_window = self.my_canvas.create_window(1080,5,anchor="nw",window=self.b4)
	#creating an object to class
        self.b1.bind("<Enter>",change)
        self.b1.bind("<Leave>",change_back)
        self.b2.bind("<Enter>",change_1)
        self.b2.bind("<Leave>",change_back_1)
def page_2_run():
	root=Tk()#create root window
	root.title("Frame Tkinter Application") #Giving a title to ba
	root.iconbitmap('gui_images/hacker.ico')
	root.state("zoomed")
	mb=secondpage(root)
	root.mainloop()
class firstpage:
	def __init__ (self,root):
		self.bg5 = ImageTk.PhotoImage(file='gui_images/black_bg.png')
		self.my_canvas1=Canvas(root,height=1400, width=1020)
		self.my_canvas1.pack(fill = "both",expand=True)
		self.my_canvas1.create_image(0,0, image=self.bg5,anchor="nw")
		self.my_canvas1.create_text(120,45, text = "About",font=("Times","56"),fill='white')
		self.my_canvas1.create_text(30,105,text = """Facial recognition is a way of identifying or confirming an individual’s identity using their face. Facial recognition 
\nsystems can be used to identify people in photos, videos, or inreal-time . Facial recognition is a category of biometric 
\nsecurity. Other forms of biometric software include voice recognition, fingerprint recognition, and eye retina or iris 
\nrecognition. The technology is mostly used for security and law enforcement, though there is increasing interest in other 
\nareas of use. 
\n\nMany people are familiar with face recognition technology through the FaceID used to unlock iPhones (however, 
\nthis is only one application of face recognition). Typically, facial recognition does not rely on a massive database of 
\nphotos to determine an individual’s identity — it simply identifies and recognizes one person as the sole owner of the 
\ndevice, while limiting access to others. Beyond unlocking phones, facial recognition works by matching the faces 
\nof people walking past special cameras, to images of people on a watch list. The watch lists can contain pictures of 
\nanyone, including people who are not suspected of any wrong doing, and the images can come from anywhere — even 
\nfrom our social media accounts.
		""",fill='white',font=("Times","14","bold"),anchor="nw")
		def func1():
			root.destroy()
		def func2():
			page_2_run()
		self.b5 = Button(root, text="NEXT" ,fg = "black",font=("Times","14","bold"),command=lambda: [func1(), func2()])
		self.b5.configure(width=13,height=1,background = "#fff",activebackground = "#000",borderwidth=7)
		b5_window = self.my_canvas1.create_window(1050,580,anchor="nw",window=self.b5)
def page_1_run():
	root=Tk()#create root window
	root.title("Face Recognizer") #Giving a title to ba
	root.iconbitmap('gui_images/hacker.ico')
	root.state("zoomed")
	mb=firstpage(root)
	root.mainloop()
page_1_run()
