from tkinter import*
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")

        self.user=StringVar()
        self.pwd=StringVar()

        frame = Frame(self.root, bd=10, relief=GROOVE)
        frame.place(x=450,y=150,height=350)

        title=Label(frame,text="Login System", font=("Time New Roman",30,"bold")).grid(row=0,columnspan=2,pady=20)

        lblusername=Label(frame,text="Username", font=("Time New Roman",20,"bold")).grid(row=1,column=0,pady=10,padx=10)
        txtusername = Entry(frame, bd=7, relief=GROOVE, textvariable=self.user, width=25,font="Arial 15 bold").grid(row=1,column=1,padx=10,pady=10)

        lblpass=Label(frame,text="Password", font=("Time New Roman",20,"bold")).grid(row=2,column=0,pady=10,padx=10)
        txtpass=Entry(frame, bd=7, relief=GROOVE, show="*", textvariable=self.pwd, width=25,font="Arial 15 bold").grid(row=2,column=1,padx=10,pady=10)

        btnLog=Button(frame,text="Login",font="Arial 15 bold",bd=7,width=10,command=self.logfun).place(x=10,y=250)
        btnReset=Button(frame,text="Reset",font="Arial 15 bold",bd=7,width=10,command=self.reset).place(x=170,y=250)
        btnCancel=Button(frame,text="Cancel",font="Arial 15 bold",bd=7,width=10,command=self.cancel).place(x=320,y=250)


    def logfun(self):
        if len(self.pwd.get())>=8 and len(self.pwd.get())<=15:
            if self.user.get()=="Me" and self.pwd.get()=="1234567890":
                #messagebox.showinfo("Info",f"Welcome {self.user.get()} and your password is: {self.pwd.get()}")
                self.root.destroy()
                import softwareUI
                softwareUI.FileSoft()
            else:
                messagebox.showerror("Error","Invalid username or password")
        else:
            messagebox.showerror("Error","Pasword must be in length of 8-15")

    def reset(self):
        self.user.set("")
        self.pwd.set("")

    def cancel(self):
        reply=messagebox.askyesno("Exit","Do you really want to exit?")
        if reply>0:
            self.root.destroy()
        else:
            return

root = Tk()
ob = Login(root)
root.mainloop()
