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
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        img_left=Image.open(r"D:\PR_101\project images\IMG_20230308_114906.jpeg")
        img_left=img_left.resize((500,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150) 

        dep_label=Label(current_course_frame,text="Discipline",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CSE","ECE","ME","SM","Design")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # course
        dep_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Course","B.tech","B.des","M.tech","PHD")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        dep_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Year","2022","2021","2020","2019","2018")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # semester
        dep_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Semester","Semester 1","Semester 2")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
#       student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=260,width=720,height=300) 

        # student id
        studentId_label=Label(class_student_frame,text="StudentId:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        # student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # Roll no.
        
        Roll_no_label=Label(class_student_frame,text="Roll no",font=("times new roman",12,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # Gender
        
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DoB
        
        dob_label=Label(class_student_frame,text="Dob",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # EMAIL

        email_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone no

        phoneno_label=Label(class_student_frame,text="Phone number",font=("times new roman",12,"bold"),bg="white")
        phoneno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phoneno_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        phoneno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address

        address_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher Name 

        Teacher_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        Teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Teacher_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        Teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio Buttons
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn1=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=1)

        # buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        takephotosample_btn=Button(btn_frame1,text="Take Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white",width=35)
        takephotosample_btn.grid(row=1,column=0)

        updatephoto_btn=Button(btn_frame1,text="Update Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white",width=35)
        updatephoto_btn.grid(row=1,column=1)

        # Right lable frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=740,y=10,width=690,height=580)

        img_right=Image.open(r"D:\PR_101\project images\IMG_20230308_114906.jpeg")
        img_right=img_right.resize((500,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #==============Search System=======================
        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=700,height=70)

        
        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame  ,font=("times new roman",12,"bold"),width=14,state="readonly")
        search_combo["values"]=("Select","Roll No","PhoneNo")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",13,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Update",font=("times new roman",13,"bold"),bg="blue",fg="white",width=10)
        search_btn.grid(row=0,column=3,padx=4)

        delete_btn=Button(Search_frame,text="delete",font=("times new roman",13,"bold"),bg="blue",fg="white",width=10)
        delete_btn.grid(row=0,column=4,padx=4)

        #========================table frame====================
        Table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        Table_frame.place(x=5,y=210,width=700,height=350 )

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id","name","div","RollNo","Gender","dob","email","gender","phone","adrress","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)













if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()