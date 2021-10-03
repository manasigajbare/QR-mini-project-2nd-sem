from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage


class QR_Generator:

    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Grnerator")
        self.root.resizable(False,False)

        title=Label(self.root,text="QR Code Generator",font=("times new roman",40),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)


        #=======Student Details window=========
        #=======variables=======
        self.var_stud_no=StringVar()
        self.var_stud_firstName=StringVar()
        self.var_stud_lastName=StringVar()
        self.var_stud_class=StringVar()

        stud_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        stud_Frame.place(x=50,y=100,width=500,height=380)
        stud_title=Label(stud_Frame,text="Student Details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        lbl_stud_no=Label(stud_Frame,text="Roll no.",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_stud_firstName=Label(stud_Frame,text="First Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_stud_lastName=Label(stud_Frame,text="Last Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_stud_class=Label(stud_Frame,text="Class",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)
        #lbl_file_name=Label(stud_Frame,text="Enter File Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=230)

        
        txt_stud_no=Entry(stud_Frame,font=("times new roman",15),textvariable=self.var_stud_no,bg='lightyellow').place(x=200,y=60)
        txt_stud_firstName=Entry(stud_Frame,font=("times new roman",15),textvariable=self.var_stud_firstName,bg='lightyellow').place(x=200,y=100)
        txt_stud_lastName=Entry(stud_Frame,font=("times new roman",15),textvariable=self.var_stud_lastName,bg='lightyellow').place(x=200,y=140)
        txt_stud_class=Entry(stud_Frame,font=("times new roman",15),textvariable=self.var_stud_class,bg='lightyellow').place(x=200,y=180)
       

        btn_generate=Button(stud_Frame,text="Generate",command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=60,y=280,width=180,height=30)
        btn_clear=Button(stud_Frame,text="Clear",command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=280,y=280,width=120,height=30)

        self.msg=''
        self.lbl_msg=Label(stud_Frame,text=self.msg,font=("goudy old style",18),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)

         #=======Qr window=========
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)
        qr_title=Label(qr_Frame,text="Student QR code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        self.qr_codel=Label(qr_Frame,text='No QR\nAvailable',font=("goudy old style",15),bg='#3f51b5',fg='white')
        self.qr_codel.place(x=35,y=100,width=180,height=180)

        btn_save=Button(qr_Frame,text="Save",command=self.save,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=75,y=300,width=100,height=30)
    
    def clear(self):
        self.var_stud_no.set('')
        self.var_stud_firstName.set('')
        self.var_stud_lastName.set('')
        self.var_stud_class.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_codel.config(image='')

    def generate(self):
        if self.var_stud_no.get()=='' or self.var_stud_firstName.get()=='' or self.var_stud_lastName.get()=='' or self.var_stud_class.get()=='':
             self.msg='All Fields are Required!! Or Enter the File Name'
             self.lbl_msg.config(text=self.msg,fg='red')   
        else:
            self.qr_data=(f"Roll No: {self.var_stud_no.get()}\nFirst Name: {self.var_stud_firstName.get()}\nLast Name: {self.var_stud_lastName.get()}\nclass: {self.var_stud_class.get()}\n")
            self.qr_code=qrcode.make(self.qr_data)
            self.qr_code=resizeimage.resize_cover(self.qr_code,[180,180])
            #====Qr code image update====
            self.img=ImageTk.PhotoImage(self.qr_code)
            self.qr_codel.config(image=self.img)
            #======notification=====
            self.msg='QR Codes are Generated Successfully!!'
            self.lbl_msg.config(text=self.msg,fg='green')
        



    def save(self):
        self.qr_code.save("Qr_codes/Rollno-"+str(self.var_stud_no.get())+'.png')
        self.msg='QR Code saved!!'
        self.lbl_msg.config(text=self.msg,fg='green')


root=Tk()
obj=QR_Generator(root)
root.mainloop()