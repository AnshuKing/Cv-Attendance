import tkinter as tk
from tkinter import *
import sys
import os
import faces
import capture_faces
import faces_train    
def attendance():
    faces.main()

def images():
    capture_faces.main()

def train():
    faces_train.main()




master=tk.Tk()
master.title("Attendance System")
master.resizable(False, False)

capture_images = tk.Button(master, text="Capture Images",command=images)


take_attendace = tk.Button(master,text="Take Attendance",command=attendance)


train_data = tk.Button(master,text="Train Data",command=train)

l = Label(master, text="Facial Recogniton Based Attendace System")
l.pack()
capture_images.pack(side=tk.LEFT, padx = 10, pady = 10)
take_attendace.pack(side=tk.RIGHT, padx = 10, pady = 10)
train_data.pack(side=tk.RIGHT, padx = 10, pady = 10)




