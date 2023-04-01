from tkinter import*
from tkinter import ttk
# powerful GUI application software
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # first image
        img=Image.open(r"D:\PR_101\project images\IMG_20230308_114906.jpg")
        # high level image to low level image
        img=img.resize((500,130),Image.ANTIALIAS)
        # save image
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"D:\PR_101\project images\IMG_20230308_114906.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image
        img2=Image.open(r"D:\PR_101\project images\IMG_20230308_114906.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # bg image
        img3=Image.open(r"D:\PR_101\project images\7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        # left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=690,height=580)
  
        # Right lable frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=740,y=10,width=690,height=580)
        











if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()