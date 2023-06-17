from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter


class LibManageSys:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1200x500+0+0")

        #======================================================variable====================================================


        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="bisque1",fg="green",bd=20,relief=RIDGE,font=("verdana",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="bisque1")
        frame.place(x=0,y=130,width=1530,height=400)

        #=======================================Data Frame Left================================================



        DataFrameLeft=LabelFrame(frame,text="LIBRARY MEMBERSHIP INFORMATION",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("verdana",12,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_No.grid(row=1,column=1)


        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No",font=("arial",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastname=Label(DataFrameLeft,bg="powder blue",text="Last Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastname.grid(row=4,column=0,sticky=W)
        txtLastname=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastname.grid(row=4,column=1)


        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address 1",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address 2",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)


        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("arial",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)


        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="powder blue",text="Book Id:",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)


        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)
        


        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)



        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)



        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDateOverDue.grid(row=7,column=3)


        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="ActualPrice:",font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)



        





        #=====================================Dat Frame right=============================================


        


        DataFrameRight=LabelFrame(frame,text="BOOK DETAILS",bg="powder blue",bd=12,relief=RIDGE,font=("verdana",12,"bold"),padx=20)
        DataFrameRight.place(x=870,y=5,width=580,height=350)


        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),padx=2,pady=6,width=32,height=16)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        

        
        listBooks=["Python Crash Course","Learning Python, 5th Edition","Automate The Boring Stuff With Python","Python (2nd Edition)","Python For Data Analysis",
"Mastering Deep Learning Fundamentals With Python","Python Pocket Reference","Elements Of Programming Interviews In Python","Head First Python","Advanced Python","Python CookBook","MAchine Techno","Learn python Programming","Machine Learning","data science","Shell Scripting","Python Fundamentals"]
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Python Crash Course"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Barry")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")

            elif (x=="Learning Python, 5th Edition"):
                self.bookid_var.set("BKID7854")
                self.booktitle_var.set("Basics of Python")
                self.author_var.set("H C Verma")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.860")
            
            elif (x=="Automate The Boring Stuff With Python"):
                self.bookid_var.set("BKID4532")
                self.booktitle_var.set("Python understanding")
                self.author_var.set("Guido Van")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1000")
            
            elif (x=="Python (2nd Edition)"):
                self.bookid_var.set("BKID9043")
                self.booktitle_var.set("Python")
                self.author_var.set("Richard Stakes")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.2500")


        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)
        #==========================================BUTTONS FRAME===============================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="bisque1")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("verdana",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("verdana",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("verdana",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("verdana",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("verdana",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("verdana",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)



        #==========================================INFORMATION FRAME===============================================

        Framedetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="burlywood1")
        Framedetails.place(x=0,y=590,width=1530,height=210) 

        Table_frame=Frame(Framedetails,bd=6,relief=RIDGE,bg="burlywood1")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("MemberType","PRNNo","IDNo","FirstName","LastName","Address1","Address2","PostCode","Mobile","BookId","BookTitle","AuthorName","DateBorrowed","DateDue","DaysOnBook","LateReturnFine","DateOverDue","ActualPrice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("MemberType",text="Member Type")
        self.library_table.heading("PRNNo",text="PRN No")
        self.library_table.heading("IDNo",text="ID No")
        self.library_table.heading("FirstName",text="First Name")
        self.library_table.heading("LastName",text="Last Name")
        self.library_table.heading("Address1",text="Address 1")
        self.library_table.heading("Address2",text="Address 2")
        self.library_table.heading("PostCode",text="Post Code")
        self.library_table.heading("Mobile",text="Mobile")
        self.library_table.heading("BookId",text="Book Id")
        self.library_table.heading("BookTitle",text="Book Title")
        self.library_table.heading("AuthorName",text="Author Name")
        self.library_table.heading("DateBorrowed",text="Date Borrowed")
        self.library_table.heading("DateDue",text="Date Due")
        self.library_table.heading("DaysOnBook",text="Days On Book")
        self.library_table.heading("LateReturnFine",text="Late Return Fine")
        self.library_table.heading("DateOverDue",text="Date Over Due")
        self.library_table.heading("ActualPrice",text="ActualPrice")


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("MemberType",width=100)
        self.library_table.column("PRNNo",width=100)
        self.library_table.column("IDNo",width=100)
        self.library_table.column("FirstName",width=100)
        self.library_table.column("LastName",width=100)
        self.library_table.column("Address1",width=100)
        self.library_table.column("Address2",width=100)
        self.library_table.column("PostCode",width=100)
        self.library_table.column("Mobile",width=100)
        self.library_table.column("BookId",width=100)
        self.library_table.column("BookTitle",width=100)
        self.library_table.column("AuthorName",width=100)
        self.library_table.column("DateBorrowed",width=100)
        self.library_table.column("DateDue",width=100)
        self.library_table.column("DaysOnBook",width=100)
        self.library_table.column("LateReturnFine",width=100)
        self.library_table.column("DateOverDue",width=100)
        self.library_table.column("ActualPrice",width=100)

        self.fetch_data()

        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Nandini@912",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.member_var.get(),self.prn_var.get(),
                self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address1_var.get(),self.address2_var.get(),self.postcode_var.get(),
                self.mobile_var.get(),self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),
                self.daysonbook_var.get(),self.latereturnfine_var.get(),self.dateoverdue_var.get(),self.finalprice_var.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted successfully")    

    def update(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Nandini@912",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostCode=%s,Mobile=%s,BookId=%s,BookTitle=%s,AuthorName=%s,DataBorrowed=%s,DataDue=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDue=%s,ActualPrice=%s where PRN_NO=%s",(self.member_var.get(),
                self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.address1_var.get(),self.address2_var.get(),self.postcode_var.get(),
                self.mobile_var.get(),self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),
                self.daysonbook_var.get(),self.latereturnfine_var.get(),self.dateoverdue_var.get(),self.finalprice_var.get(),self.prn_var.get()))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member has been updated")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Nandini@912",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])
    
    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRNNo\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"IDNo\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"FirstName\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"LastName\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"PostCode\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"BookId\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"BookTitle\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"AuthorName\t\t"+self.author_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DateDue\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook\t\t"+self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"LateReturnFine\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"ActualPrice\t\t"+self.finalprice_var.get()+"\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)
    
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Managaement System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.show("Error","First select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Nandini@912",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")









if __name__=="__main__":
    root=Tk()
    obj=LibManageSys(root)
    root.mainloop()


