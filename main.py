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
        img3=Image.open(r"D:\PR_101\project images\7707820f-8369-4633-863f-146b7d690e06.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_lbl,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student button
        img4=Image.open(r"D:\PR_101\project images\7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_lbl,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Student Details",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=200,y=320,width=220,height=40)

        # Face Button
        img5=Image.open(r"D:\PR_101\project images\7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5) 

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="Face Button",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=200,y=600,width=220,height=40)

        # Student button
        img6=Image.open(r"D:\PR_101\project images\7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_lbl,image=self.photoimg6,cursor="hand2")
        b1.place(x=520,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Student Details",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=520,y=320,width=220,height=40)

        # Face Detector
        img5=Image.open(r"D:\PR_101\project images\7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5) 

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2")
        b1.place(x=520,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="Face Detector",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=520,y=600,width=220,height=40)

        # Student button
        img5=Image.open(r"D:\PR_101\project images\7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2")
        b1.place(x=840,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Train Data",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=840,y=320,width=220,height=40)

        # Face Button
        img5=Image.open(r"D:\PR_101\project images\7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5) 

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2")
        b1.place(x=840,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=840,y=600,width=220,height=40)

        # Student button
        img5=Image.open(r"D:\PR_101\project images\7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2")
        b1.place(x=1160,y=100,width=220,height=220)

        b1_1=Button(bg_lbl,text="Student Details",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=1160,y=320,width=220,height=40)

        # Face Button
        img5=Image.open(r"D:\PR_101\project images\7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5) 

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2")
        b1.place(x=1160,y=380,width=220,height=220)

        b1_1=Button(bg_lbl,text="Face Button",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        b1_1.place(x=1160,y=600,width=220,height=40)






if __name__== "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()