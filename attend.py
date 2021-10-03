from tkinter import *
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time 
import pybase64

class attend:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("Attendance")
        self.root.resizable(False,False)

        title=Label(self.root,text="Lecture Details",font=("times new roman",40),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)

        self.var_lec_code=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()

        attend_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        attend_Frame.place(x=50,y=100,width=500,height=380)
        title=Label(attend_Frame,text="Student Details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        lbl_lec_code=Label(attend_Frame,text="Lecture Code",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_time=Label(attend_Frame,text="Time",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_date=Label(attend_Frame,text="Date",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        
        
        txt_lec_code=Entry(attend_Frame,font=("times new roman",15),textvariable=self.var_lec_code,bg='lightyellow').place(x=200,y=60)
        txt_time=Entry(attend_Frame,font=("times new roman",15),textvariable=self.var_time,bg='lightyellow').place(x=200,y=100)
        txt_date=Entry(attend_Frame,font=("times new roman",15),textvariable=self.var_date,bg='lightyellow').place(x=200,y=140)
    
       

        btn_open=Button(attend_Frame,text="Open",font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=60,y=280,width=180,height=30)

root=Tk()
obj=attend(root)
root.mainloop()