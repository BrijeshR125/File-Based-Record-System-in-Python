from tkinter import*
from tkinter import ttk,messagebox
import time
import os
from datetime import *

class FileSoft:
    def __init__(self):
        self.root=Tk()
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")

        tittle=Label(self.root,text="File Based Record System",bd=10,relief=GROOVE,pady=10,font=("Times New Roman",35,"bold")).pack(fill=X)

        studentFrame=Frame(self.root,bd=10,relief=GROOVE)
        studentFrame.place(x=20,y=100)

        stitle=Label(studentFrame,text="Student Details",font=("Times New Roman",23,"bold")).grid(row=0,columnspan=4,pady=20)

        #All variables here
        self.s_id=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.address=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()

        sid=Label(studentFrame,text="Student ID",font=("Times New Roman",20,"bold")).grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txtid=Entry(studentFrame,bd=7,textvariable=self.s_id,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=1,column=1,padx=10,pady=20)

        sname=Label(studentFrame,text="Name",font=("Times New Roman",20,"bold")).grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txtname=Entry(studentFrame,bd=7,textvariable=self.name,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=2,column=1,padx=10,pady=20)

        sctc=Label(studentFrame,text="Contact No.",font=("Times New Roman",20,"bold")).grid(row=1,column=2,pady=10,padx=20,sticky="w")
        txtctc=Entry(studentFrame,bd=7,textvariable=self.contact,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=1,column=3,padx=10,pady=20)

        sdate=Label(studentFrame,text="Date (dd/mm/yyyy)",font=("Times New Roman",20,"bold")).grid(row=2,column=2,pady=10,padx=20,sticky="w")
        txtdate=Entry(studentFrame,bd=7,textvariable=self.date,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=2,column=3,padx=10,pady=20)

        scourse=Label(studentFrame,text="Course",font=("Times New Roman",20,"bold")).grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txtcourse=Entry(studentFrame,bd=7,textvariable=self.course,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=3,column=1,padx=10,pady=20)

        saddr=Label(studentFrame,text="Address",font=("Times New Roman",20,"bold")).grid(row=4,column=0,pady=10,padx=20,sticky="w")
        txtaddr=Entry(studentFrame,bd=7,textvariable=self.address,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=4,column=1,padx=10,pady=20)

        scity=Label(studentFrame,text="City",font=("Times New Roman",20,"bold")).grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txtcity=Entry(studentFrame,bd=7,textvariable=self.city,relief=GROOVE,width=22,font="Arial 15 bold").grid(row=5,column=1,padx=10,pady=20)

        sdr=Label(studentFrame,text="Select Degree",font=("Times New Roman",20,"bold")).grid(row=3,column=2,pady=10,padx=20,sticky="w")
        degreecombo=ttk.Combobox(studentFrame,textvariable=self.degree,width=20,state="readonly",font="Arial 15 bold")
        degreecombo["values"]=("BE/B. Tech","M. Tech","BCA","MCA")
        degreecombo.grid(row=3,column=3,padx=10,pady=10)
        
        sproof=Label(studentFrame,text="ID Proof",font=("Times New Roman",20,"bold")).grid(row=4,column=2,pady=10,padx=20,sticky="w")
        idcombo=ttk.Combobox(studentFrame,textvariable=self.proof,width=20,state="readonly",font="Arial 15 bold")
        idcombo["values"]=("Aadhar Card","Driving License","PAN Card","ID card")
        idcombo.grid(row=4,column=3,padx=10,pady=10)

        spaymode=Label(studentFrame,text="Payment mode",font=("Times New Roman",20,"bold")).grid(row=5,column=2,pady=10,padx=20,sticky="w")
        paymodecombo=ttk.Combobox(studentFrame,textvariable=self.payment,width=20,state="readonly",font="Arial 15 bold")
        paymodecombo["values"]=("Cash","Cheque","Debit/Credit Card","Internet Banking")
        paymodecombo.grid(row=5,column=3,padx=10,pady=10)

        btnFrame=Frame(self.root,bd=10,relief=GROOVE)
        btnFrame.place(x=10,y=620)

        btnAddSave=Button(btnFrame,text="Add/Save",font="Arial 15 bold",bd=7,width=18,command=self.save).grid(row=0,column=0,padx=12,pady=10)
        btnDelete=Button(btnFrame,text="Delete",font="Arial 15 bold",bd=7,width=18,command=self.delete).grid(row=0,column=1,padx=12,pady=10)
        btnClear=Button(btnFrame,text="Clear",font="Arial 15 bold",bd=7,width=18,command=self.clear).grid(row=0,column=2,padx=12,pady=10)
        btnLogout=Button(btnFrame,text="Logout",font="Arial 15 bold",bd=7,width=18,command=self.logout).grid(row=0,column=3,padx=12,pady=10)
        btnExit=Button(btnFrame,text="Exit",font="Arial 15 bold",bd=7,width=18,command=self.exit).grid(row=0,column=4,padx=12,pady=10)

        fileFrame=Frame(self.root,bd=10,relief=GROOVE)
        fileFrame.place(x=1030,y=100,width=300,height=500)

        ftitle=Label(fileFrame,text="All Files",font="Arial 20 bold",bd=5,relief=GROOVE).pack(side=TOP,fill=X)

        scrolly=Scrollbar(fileFrame,orient=VERTICAL)
        self.filelist=Listbox(fileFrame,yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.filelist.yview)
        self.filelist.pack(fill=BOTH,expand=1)
        
        self.filelist.bind("<ButtonRelease-1>",self.getData)
        self.showFiles()

        self.root.mainloop()
        
    def save(self):
        if self.validation()==1:
            present=0
            if self.s_id.get()=="":
                messagebox.showerror("Error","Student ID must be required")
            else:
                f=os.listdir("files/")
                if len(f)>0:
                    for i in f:
                        if i.split(".")[0]==self.s_id.get():
                            present=1
                    if present==1:
                        r=messagebox.askyesno("Update","File is already present \nDo you really want to update it?")
                        if r>0:
                            self.saveFiles()
                            messagebox.showinfo("Update","Record has been updated")
                            self.showFiles()
                    else:
                        self.saveFiles()
                        messagebox.showinfo("Saved","Record has been saved")
                        self.showFiles()
                else:
                    self.saveFiles()
                    messagebox.showinfo("Saved","Record has been saved")
                    self.showFiles()
        else:
            return

    def saveFiles(self):
        f=open(str("files/"+self.s_id.get())+".txt","w")
        f.write(
                str(self.s_id.get())+","+
                str(self.name.get())+","+
                str(self.course.get())+","+
                str(self.address.get())+","+
                str(self.city.get())+","+
                str(self.contact.get())+","+
                str(self.date.get())+","+
                str(self.degree.get())+","+
                str(self.proof.get())+","+
                str(self.payment.get())
                )
        f.close()

    def showFiles(self):
        files=os.listdir("files/")
        self.filelist.delete(0,END)
        if len(files)>0:
            for i in files:
                self.filelist.insert(END,i)

    def getData(self,ev):
        getCursor=self.filelist.curselection()
        f1=open("files/"+self.filelist.get(getCursor))
        values=[]
        for f in f1:
            values=f.split(",")
            
        self.s_id.set(values[0])
        self.name.set(values[1])
        self.course.set(values[2])
        self.address.set(values[3])
        self.city.set(values[4])
        self.contact.set(values[5])
        self.date.set(values[6])
        self.degree.set(values[7])
        self.proof.set(values[8])
        self.payment.set(values[9])

    def clear(self):
        self.s_id.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")

    def delete(self):
        present=0
        if self.s_id.get()=="":
            messagebox.showerror("Error","Student ID must be required")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.s_id.get():
                        present=1
                if present==1:
                    r=messagebox.askyesno("Delete","Do you really want to delete the record file?")
                    if r>0:
                        os.remove("files/"+self.s_id.get()+".txt")
                        messagebox.showinfo("Success","Record file deleted")
                        self.showFiles()
                else:
                    messagebox.showerror("Error","Record file not found")

    def exit(self):
        re=messagebox.askyesno("Exit","Do you really want to exit?")
        if re>0:
            self.root.destroy()
        else:
            return

    def logout(self):
        re=messagebox.askyesno("Logout","Do you really want to logout?")
        if re>0:
            self.root.destroy()
            import login
        else:
            return

    def validation(self):
        if self.name.get()=="":
            messagebox.showerror("Error","Name field is empty")
            return 0
        elif self.course.get()=="":
            messagebox.showerror("Error","Course field is empty")
            return 0
        elif self.address.get()=="":
            messagebox.showerror("Error","Address field is empty")
            return 0
        elif self.city.get()=="":
            messagebox.showerror("Error","City field is empty")
            return 0
        elif self.contact.get()=="":
            messagebox.showerror("Error","Contact field is empty")
            return 0
        elif len(self.contact.get())<10 or len(self.contact.get())>10:
            messagebox.showerror("Error","Contact must be of 10 digits")
            return 0
        elif self.date.get()=="":
            messagebox.showerror("Error","Date field is empty")
            return 0
        elif self.degree.get()=="":
            messagebox.showerror("Error","Please select degree from the list in Degree field")
            return 0
        elif self.proof.get()=="":
            messagebox.showerror("Error","Please select proof from the list in Proof field")
            return 0
        elif self.payment.get()=="":
            messagebox.showerror("Error","Please select payment mode from the list in Payment mode field")
            return 0
        else:
            return 1
