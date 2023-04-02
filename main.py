from tkinter import*
from tkinter import ttk
# powerful GUI application software
from PIL import Image,ImageTk


class Face_recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")

        # first image
        img=Image.open(r"D:\PR_101\project images\student.jpeg")
        # high level image to low level image
        img=img.resize((500,130),Image.ANTIALIAS)
        # save image
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"D:\PR_101\project images\image 2.jpeg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image
        img2=Image.open(r"D:\PR_101\project images\image 3.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=560,height=130)

        # bg image
        img3=Image.open(r"D:\PR_101\project images\image bg.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_lbl,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student button
        img4=Image.open(r"D:\PR_101\project images\student.jpeg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_lbl,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Student Details",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=200,y=320,width=220,height=40)

        # Face Button
        img5=Image.open(r"D:\PR_101\project images\face detector.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5) 

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)
 
        b1_1=Button(bg_lbl,text="Face Detector",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=200,y=600,width=220,height=40)

        # Train Data
        img6=Image.open(r"D:\PR_101\project images\traindata.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_lbl,image=self.photoimg6,cursor="hand2")
        b1.place(x=520,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Train Data",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=520,y=320,width=220,height=40)

        # Photos
        img7=Image.open(r"D:\PR_101\project images\photos.jpeg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7) 

        b1=Button(bg_lbl,image=self.photoimg7,cursor="hand2")
        b1.place(x=520,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="Photos",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=520,y=600,width=220,height=40)

        # Attendance
        img8=Image.open(r"D:\PR_101\project images\attendance.jpeg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_lbl,image=self.photoimg8,cursor="hand2")
        b1.place(x=840,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Attendance",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=840,y=320,width=220,height=40)

        # Developer
        img9=Image.open(r"D:\PR_101\project images\developer.jpeg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9) 

        b1=Button(bg_lbl,image=self.photoimg9,cursor="hand2")
        b1.place(x=840,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="Developer",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=840,y=600,width=220,height=40)

        # Help desk
        img10=Image.open(r"D:\PR_101\project images\help desk.jpeg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_lbl,image=self.photoimg10,cursor="hand2")
        b1.place(x=1160,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Help desk",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=1160,y=320,width=220,height=40)

        # Exit
        img11=Image.open(r"D:\PR_101\project images\exit.jpeg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11) 

        b1=Button(bg_lbl,image=self.photoimg11,cursor="hand2")
        b1.place(x=1160,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="Exit",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=1160,y=600,width=220,height=40)






if __name__== "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()