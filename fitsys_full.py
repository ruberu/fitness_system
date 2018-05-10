from tkinter import*
import tkinter
from tkinter import messagebox
import random
import time
import sqlite3
import getpass
import math
conn = sqlite3.connect("fitsys.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS logins(uname TEXT NOT NULL UNIQUE, password TEXT NOT NULL,name TEXT, email TEXT, cnumber INTEGER)")
conn.commit()
c.execute("CREATE TABLE IF NOT EXISTS body(uname TEXT, height INTEGER, weight INTEGER, gender TEXT)")
conn.commit()
#---------------------app-window---------------------------------------
root = Tk()
root.title('FITNESS SYSTEM')
root.geometry('1000x600+80+80')
#--------------------------------HEADER-------------------------------------
header = Frame(root, width = 1000, height = 150, relief = SUNKEN)
header.pack(side = TOP)
localtime = time.asctime(time.localtime(time.time()))
headerinfo = Label(header, font =('arial', 40, 'bold'),text = 'THE  FITNESS  SYSTEM', 
                    fg = 'Steel Blue',relief=RIDGE,bd=2, anchor = 'w')
headerinfo.grid(row = 0, column = 0)
headerinfo = Label(header, font = ('arial',15,'bold'),text=localtime, 
                    fg = 'Steel Blue',relief=RIDGE, bd=2, anchor = 'w', padx=182)
headerinfo.grid(row = 1, column = 0)
#-------------------functions-----------------------------------------
def sign_in():
    frGreeting.pack_forget()
    frSignIn.pack()

def sign_up():
    frGreeting.pack_forget()
    frSignUp.pack()

def sign_in_c():
    frSignIn.pack_forget()
    frGreeting.pack()
    Uname.set('')
    Passw.set('')
    
def sign_up_c():
    frSignUp.pack_forget()
    frGreeting.pack()
    SUUname.set('')
    SUPassw.set('')
    SUName.set('')
    SUEmail.set('')
    SUNumber.set('')

def emailc():
    frEmail.pack_forget()
    frSignIn.pack()
    sEmail.set("")

def email_check():
    email=sEmail.get().lower()
    c.execute("SELECT * FROM logins WHERE email = '%s' "%email)
    if c.fetchall():
        messagebox.showinfo("Signed in", "You have successfully signed in! Welcome!")
        c.execute("SELECT uname FROM logins WHERE email = '%s' "%email)    
        temp=c.fetchall()
        temp=(temp[0])[0]
        file=open('fitsys.txt', 'w')
        file.write(temp)
        file.close()
        frEmail.pack_forget()
        frMain.pack()
    else:
        if messagebox.askretrycancel("Login failed", "Incorrect email address!"):
            sEmail.set('')
            hahabek=3
        else:
            frEmail.pack_forget()      
            Uname.set('')
            Passw.set('')
            frSignIn.pack()

    conn.commit()
        
def sign_in_s():
    username=Uname.get().lower()
    password=Passw.get()
    c.execute('SELECT * FROM logins WHERE uname = ? AND password = ?', (username,password,))
    if c.fetchall():
        messagebox.showinfo("Signed in", "You have successfully signed in! Welcome!")
        file=open('fitsys.txt', 'w')
        file.write(username)
        file.close()
        frSignIn.pack_forget()
        frMain.pack()
    else:
        if messagebox.askretrycancel("Login failed", "Incorrect username or password!"):
            hahabek=3
            Uname.set('')
            Passw.set('')
        else:
            sEmail.set('')
            frSignIn.pack_forget()
            frEmail.pack()

def sign_up_s():
    username=SUUname.get().lower()
    password=SUPassw.get()
    name=SUName.get()
    email=SUEmail.get().lower()
    cnumber=SUNumber.get()
    count=0
    if len(username)==0 or len(password)==0 or len(name)==0 or len(email)==0 or len(cnumber)==0:
        messagebox.showwarning('Empty', 'Please, fill all blanks!')
        count+=1
    if len(password)>0:
        try:
            cnumber=int(cnumber)
        except:
            messagebox.showwarning('Incorrect number', 'Please, enter only integer numbers for cellphone number!')
            count+=1
    if len(username)>0:
        c.execute("SELECT uname FROM logins WHERE uname = '%s'"%username)
        data = c.fetchall()
        if len(data)>0:
            messagebox.showwarning('Unavailable', 'Username is unavailable. Please, choose another username!')
            count+=1
    if count==0:
        c.execute("INSERT INTO logins VALUES(?, ?, ?, ?, ?)", (username, password, name, email, cnumber))
        conn.commit()
        c.execute("INSERT INTO body VALUES(?, ?, ?, ?)", (username, 1, 1, 'GENDER'))
        conn.commit()
        messagebox.showinfo("Success", "Congratulations, %s! You just have signed up!"%name)
        file=open('fitsys.txt', 'w')
        file.write(username)
        file.close()
        frSignUp.pack_forget()
        frMain.pack()

def about():
    frMain.pack_forget()
    frAbout.pack()

def about_c():
    frAbout.pack_forget()
    frMain.pack()

def editing():
    file=open('fitsys.txt','r')
    uname=file.read()
    c.execute("SELECT * FROM logins WHERE uname = '%s'"%uname)
    data = c.fetchall()
    Dname=(data[0])[2]
    Demail=(data[0])[3]
    Dnumber=(data[0])[4]   
    c.execute("SELECT * FROM body WHERE uname = '%s'"%uname)
    data = c.fetchall()
    Dheight=(data[0])[1]
    Dweight=(data[0])[2]
    Dgender=(data[0])[3]
    if Dgender=='GENDER':
        EdPassw.set("")
        EdPassw2.set("")
        EdName.set(Dname)
        EdEmail.set(Demail)
        EdNumber.set('0'+str(Dnumber))
        EdHeight.set("-")
        EdWeight.set("-")
        EdGender.set(-1)
    else:
        EdPassw.set("")
        EdPassw2.set("")
        EdName.set(Dname)
        EdEmail.set(Demail)
        EdNumber.set('0'+str(Dnumber))
        EdHeight.set(Dheight)
        EdWeight.set(Dweight)
        if Dgender=='M':
            EdGender.set(1)
        else:
            EdGender.set(2)

    frMain.pack_forget()
    frEdit.pack()
    conn.commit()


def editing_c():
    frEdit.pack_forget()
    frMain.pack()

def editing_s():
    file=open("fitsys.txt", 'r')
    uname=file.read()
    
    password=EdPassw.get()
    name=EdName.get()
    email=EdEmail.get().lower()
    cnumber=EdNumber.get()
    height=EdHeight.get()
    weight=EdWeight.get()
    gender=EdGender.get()
    password2=EdPassw2.get()

    count=0
    if len(password)==0 or len(name)==0 or len(email)==0 or len(cnumber)==0 or len(height)==0 or len(weight)==0:
        messagebox.showwarning('Empty', 'Please, fill all blanks!')
        count+=1
    if password!=password2:
        messagebox.showwarning('Re-entry', 'New passwords do not match!')
        count+=1
    if len(cnumber)>0:
        try:
            cnumber=int(cnumber)
        except:
            messagebox.showwarning('Incorrect format', 'Please, enter only integer numbers for cellphone number!')
            count+=1
    if len(height)>0:
        try:
            height=int(height)
        except:
            messagebox.showwarning('Incorrect format', 'Please, enter only integer numbers for height!')
            count+=1
    if len(weight)>0:
        try:
            weight=int(weight)
        except:
            messagebox.showwarning('Incorrect format', 'Please, enter only integer numbers for weight!')
            count+=1
    if gender==1:
        gender='M'
    else:
        gender='F'
    if count==0:
        c.execute("DELETE FROM logins WHERE uname = ?", (uname,))
        c.execute("DELETE FROM body WHERE uname = ?", (uname,))
        conn.commit()
        c.execute("INSERT INTO logins VALUES(?, ?, ?, ?, ?)", (uname, password, name, email, cnumber))
        conn.commit()
        c.execute("INSERT INTO body VALUES(?, ?, ?, ?)", (uname, height, weight, gender))
        conn.commit()
        messagebox.showinfo("Success", "Congratulations, %s! You just have edited personal information!"%name)
        file=open('fitsys.txt', 'w')
        file.write(uname)
        file.close()

        frEdit.pack_forget()
        frMain.pack()
    file.close()



def schedule():
    frMain.pack_forget()
    frSched.pack()

def sched_show():
    file=open('fitsys.txt', 'r')
    uname=file.read()
    c.execute("SELECT name FROM logins WHERE uname = '%s'"%uname)
    data = c.fetchall()
    Dname=(data[0])[0]
    c.execute("SELECT * FROM body WHERE uname = '%s'"%uname)
    data = c.fetchall()
    Dheight=(data[0])[1]
    Dweight=(data[0])[2]
    Dgender=(data[0])[3]
    if Dheight==1 or Dweight==1:
        messagebox.showinfo("Empty",'Schedule is not ready. Please, enter body parameters!')
        Sname.set('')
        Sheight.set('')
        Sweight.set('')
        Sgender.set('')
        Sbmi.set('')
        Sfr61.set('')
        Sfr62.set('')
        Sfr63.set('')
        Sfr64.set('')
        Sfr71.set('')
        Sfr72.set('')
        Sfr73.set('')
        Sfr74.set('')
        Sfr81.set('')
        Sfr82.set('')
        Sfr83.set('')
        Sfr84.set('')
        Sfr91.set('')
        Sfr92.set('')
        Sfr93.set('')
        Sfr94.set('')
        Sfr101.set('')
        Sfr102.set('')
        Sfr103.set('')
        Sfr104.set('')
        Sfr111.set('')
        Sfr112.set('')
        Sfr113.set('')
        Sfr114.set('')
        Sfr121.set('')
        Sfr122.set('')
        Sfr123.set('')
        Sfr124.set('')
        frSched.pack_forget()
        frEdit.pack()
    BMI = float(Dweight/float(Dheight / 100)/float(Dheight / 100))
    BMI=round(BMI, 1)
    Sname.set(Dname)
    Sheight.set(Dheight)
    Sweight.set(Dweight)
    Sgender.set(Dgender)
    Sbmi.set(BMI)
#--------------------tabling----------------------------
    if Dgender == 'M':
        if BMI<=18.5:
            Sfr61.set('15 mins')
            Sfr62.set('Jogging')
            Sfr63.set('15 mins')
            Sfr64.set('Jogging')

            Sfr71.set('10 mins')
            Sfr72.set('Walking')
            Sfr73.set('15 mins')
            Sfr74.set('Walking')

            Sfr81.set('')
            Sfr82.set('')
            Sfr83.set('5 mins')
            Sfr84.set('Squats')

            Sfr91.set('')
            Sfr92.set('')
            Sfr93.set('5 mins')
            Sfr94.set('Push ups')

            Sfr101.set('')
            Sfr102.set('')
            Sfr103.set('5 mins')
            Sfr104.set('Jump ropes')

            Sfr111.set('')
            Sfr112.set('')
            Sfr113.set('10 mins')
            Sfr114.set('Leg press')

            Sfr121.set('')
            Sfr122.set('')
            Sfr123.set('')
            Sfr124.set('')    
        elif BMI>18.5 and BMI<=24.5:
            Sfr61.set('20 mins')
            Sfr62.set('Jogging')
            Sfr63.set('20 mins')
            Sfr64.set('Jogging')

            Sfr71.set('5 mins')
            Sfr72.set('Walking')
            Sfr73.set('5 mins')
            Sfr74.set('Walking')

            Sfr81.set('')
            Sfr82.set('')
            Sfr83.set('5 mins')
            Sfr84.set('Squats')

            Sfr91.set('')
            Sfr92.set('')
            Sfr93.set('10 mins')
            Sfr94.set('Push ups')

            Sfr101.set('')
            Sfr102.set('')
            Sfr103.set('5 mins')
            Sfr104.set('Jump ropes')

            Sfr111.set('')
            Sfr112.set('')
            Sfr113.set('10 mins')
            Sfr114.set('Deadlifts')

            Sfr121.set('')
            Sfr122.set('')
            Sfr123.set('')
            Sfr124.set('')
        elif BMI>24.5 and BMI<=29.5:
            Sfr61.set('15 mins')
            Sfr62.set('Jogging')
            Sfr63.set('10 mins')
            Sfr64.set('Jogging')

            Sfr71.set('10 mins')
            Sfr72.set('Walking')
            Sfr73.set('5 mins')
            Sfr74.set('Walking')

            Sfr81.set('')
            Sfr82.set('')
            Sfr83.set('10 mins')
            Sfr84.set('Squats')

            Sfr91.set('')
            Sfr92.set('')
            Sfr93.set('5 mins')
            Sfr94.set('Push ups')

            Sfr101.set('')
            Sfr102.set('')
            Sfr103.set('10 mins')
            Sfr104.set('Jump ropes')

            Sfr111.set('')
            Sfr112.set('')
            Sfr113.set('5 mins')
            Sfr114.set('Deadlifts')

            Sfr121.set('')
            Sfr122.set('')
            Sfr123.set('5 mins')
            Sfr124.set('Leg presses')
        else:
            Sfr61.set('5 mins')
            Sfr62.set('Jogging')
            Sfr63.set('10 mins')
            Sfr64.set('Jogging')

            Sfr71.set('15 mins')
            Sfr72.set('Walking')
            Sfr73.set('5 mins')
            Sfr74.set('Walking')

            Sfr81.set('')
            Sfr82.set('')
            Sfr83.set('5 mins')
            Sfr84.set('Squats')

            Sfr91.set('')
            Sfr92.set('')
            Sfr93.set('10 mins')
            Sfr94.set('Leg presses')

            Sfr101.set('')
            Sfr102.set('')
            Sfr103.set('5 mins')
            Sfr104.set('Jump ropes')

            Sfr111.set('')
            Sfr112.set('')
            Sfr113.set('5 mins')
            Sfr114.set('Deadlifts')

            Sfr121.set('')
            Sfr122.set('')
            Sfr123.set('5')
            Sfr124.set('Scissors')
    elif Dgender == 'F':
        if BMI<=18.5:
            Sfr61.set('15 mins')
            Sfr62.set('Jogging')
            Sfr63.set('10 mins')
            Sfr64.set('Jogging')

            Sfr71.set('10 mins')
            Sfr72.set('Walking')
            Sfr73.set('15 mins')
            Sfr74.set('Walking')

            Sfr81.set('')
            Sfr82.set('')
            Sfr83.set('5 mins')
            Sfr84.set('Squats')

            Sfr91.set('')
            Sfr92.set('')
            Sfr93.set('5 mins')
            Sfr94.set('Push ups')

            Sfr101.set('')
            Sfr102.set('')
            Sfr103.set('5 mins')
            Sfr104.set('Jump ropes')

            Sfr111.set('')
            Sfr112.set('')
            Sfr113.set('30 mins')
            Sfr114.set('Fly yoga')

            Sfr121.set('')
            Sfr122.set('')
            Sfr123.set('')
            Sfr124.set('')    
        elif BMI>18.5 and BMI<=24.5:
            Sfr61.set('20 mins')
            Sfr62.set('Jogging')
            Sfr63.set('15 mins')
            Sfr64.set('Jogging')

            Sfr71.set('5 mins')
            Sfr72.set('Walking')
            Sfr73.set('10 mins')
            Sfr74.set('Walking')

            Sfr81.set('')
            Sfr82.set('')
            Sfr83.set('10 mins')
            Sfr84.set('Squats')

            Sfr91.set('')
            Sfr92.set('')
            Sfr93.set('5 mins')
            Sfr94.set('Push ups')

            Sfr101.set('')
            Sfr102.set('')
            Sfr103.set('5 mins')
            Sfr104.set('Jump ropes')

            Sfr111.set('')
            Sfr112.set('')
            Sfr113.set('30 mins')
            Sfr114.set('Fly fitness')

            Sfr121.set('')
            Sfr122.set('')
            Sfr123.set('')
            Sfr124.set('')
        elif BMI>24.5 and BMI<=29.5:
            Sfr61.set('15 mins')
            Sfr62.set('Jogging')
            Sfr63.set('20 mins')
            Sfr64.set('Jogging')

            Sfr71.set('10 mins')
            Sfr72.set('Walking')
            Sfr73.set('5 mins')
            Sfr74.set('Walking')

            Sfr81.set('')
            Sfr82.set('')
            Sfr83.set('10 mins')
            Sfr84.set('Squats')

            Sfr91.set('')
            Sfr92.set('')
            Sfr93.set('5 mins')
            Sfr94.set('Push ups')

            Sfr101.set('')
            Sfr102.set('')
            Sfr103.set('5 mins')
            Sfr104.set('Jump ropes')

            Sfr111.set('')
            Sfr112.set('')
            Sfr113.set('20 mins')
            Sfr114.set('Fly fitness')

            Sfr121.set('')
            Sfr122.set('')
            Sfr123.set('')
            Sfr124.set('')
        else:
            Sfr61.set('5 mins')
            Sfr62.set('Jogging')
            Sfr63.set('10 mins')
            Sfr64.set('Jogging')

            Sfr71.set('20 mins')
            Sfr72.set('Walking')
            Sfr73.set('15 mins')
            Sfr74.set('Walking')

            Sfr81.set('')
            Sfr82.set('')
            Sfr83.set('10 mins')
            Sfr84.set('Up and downs')

            Sfr91.set('')
            Sfr92.set('')
            Sfr93.set('10 mins')
            Sfr94.set('Knee rolls')

            Sfr101.set('')
            Sfr102.set('')
            Sfr103.set('10 mins')
            Sfr104.set('Workout with plates')

            Sfr111.set('')
            Sfr112.set('')
            Sfr113.set('20 mins')
            Sfr114.set('Yoga')

            Sfr121.set('')
            Sfr122.set('')
            Sfr123.set('')
            Sfr124.set('')
    file.close()

def sched_back():
    frSched.pack_forget()
    frMain.pack()
    Sname.set('')
    Sheight.set('')
    Sweight.set('')
    Sgender.set('')
    Sbmi.set('')
    Sfr61.set('')
    Sfr62.set('')
    Sfr63.set('')
    Sfr64.set('')
    Sfr71.set('')
    Sfr72.set('')
    Sfr73.set('')
    Sfr74.set('')
    Sfr81.set('')
    Sfr82.set('')
    Sfr83.set('')
    Sfr84.set('')
    Sfr91.set('')
    Sfr92.set('')
    Sfr93.set('')
    Sfr94.set('')
    Sfr101.set('')
    Sfr102.set('')
    Sfr103.set('')
    Sfr104.set('')
    Sfr111.set('')
    Sfr112.set('')
    Sfr113.set('')
    Sfr114.set('')
    Sfr121.set('')
    Sfr122.set('')
    Sfr123.set('')
    Sfr124.set('')
#-----------Greeting-the-first-page----------------------------------------------
frGreeting=Frame(root,width=1000, height=500)
btSignIn=Button(frGreeting,font=('arial',30),text='SIGN IN',command=sign_in,
bd=5,fg='steel blue',justify=CENTER,padx=108,pady=20,activeforeground='blue',
relief=GROOVE).pack(side=TOP, padx=100, pady=20)
btSignUp=Button(frGreeting,font=('arial',30),text='SIGN UP',bd=5,fg='steel blue',justify=CENTER,
padx=100,pady=20,activeforeground='blue',command=sign_up,relief=GROOVE).pack(side=TOP)
btExit=Button(frGreeting,font=('arial', 30),text='EXIT',bd=5,fg='steel blue',justify=CENTER,
padx=100,pady=20,activeforeground='blue',command=exit,relief=GROOVE).pack(side=BOTTOM,pady=50)
frGreeting.pack(side=TOP)
#----------------------Sign-In---------------------------------------
frSignIn=Frame(root, width=1000, height=500)
lbUname=Label(frSignIn, text='Enter username:',font=('Arial', 20,'bold'),
fg='Steel blue', anchor='w').grid(row=0,column=0,sticky=W, padx=20, pady=20)
lbPassw=Label(frSignIn, text='Enter password:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=1,column=0,sticky=W, padx=20, pady=20)
Uname=StringVar()
Passw=StringVar()
eUname=Entry(frSignIn,font=('Arial', 20), textvariable=Uname,relief=GROOVE, bd=5, fg='midnight blue').grid(row=0,column=1)
ePassw=Entry(frSignIn, font=('Arial', 20), textvariable=Passw,relief=GROOVE, bd=5,fg='midnight blue',show='*').grid(row=1,column=1)
btSignInS=Button(frSignIn,font=('arial',15),text='SIGN IN',command=sign_in_s,
bd=5, fg='steel blue',justify=CENTER,activeforeground='blue',
relief=GROOVE).grid(row=2,column=1,sticky=W)
btSignInC=Button(frSignIn,font=('arial',15),text='BACK',command=sign_in_c,
bd=5, fg='steel blue',justify=CENTER,activeforeground='blue',
relief=GROOVE).grid(row=2,column=1,sticky=E)
#--------------------login-with-email------------------------
frEmail=Frame(root, width=1000, height=500)
lbEmail=Label(frEmail, text='Enter email address:',font=('Arial', 20,'bold'),
fg='Steel blue', anchor='w').grid(row=0,column=0,sticky=W, padx=20, pady=20)
sEmail=StringVar()
eEmail=Entry(frEmail,font=('Arial', 20), textvariable=sEmail,relief=GROOVE, bd=5, fg='midnight blue').grid(row=1,column=0)
btEmail=Button(frEmail,font=('arial',15),text='LOG IN',command=email_check,
bd=5, fg='steel blue',justify=LEFT,activeforeground='blue',
relief=GROOVE).grid(row=2,column=0,sticky=W)
btEmailc=Button(frEmail,font=('arial',15),text='CANCEL',command=emailc,
bd=5, fg='steel blue',justify=RIGHT,activeforeground='blue',
relief=GROOVE).grid(row=2,column=0,sticky=E)
#----------------Sign-up----------------------
frSignUp=Frame(root, width=1000, height=500)
lbSUUname=Label(frSignUp, text='Username:',font=('Arial', 20,'bold'),
fg='Steel blue', anchor='w').grid(row=0,column=0,sticky=W, padx=20, pady=20)
lbSUPassw=Label(frSignUp, text='Password:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=1,column=0,sticky=W, padx=20, pady=20)
lbSUName=Label(frSignUp, text='Full Name:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=2,column=0,sticky=W, padx=20, pady=20)
lbSUEmail=Label(frSignUp, text='Email address:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=3,column=0,sticky=W, padx=20, pady=20)
lbSUnumber=Label(frSignUp, text='Cellphone Number:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=4,column=0,sticky=W, padx=20, pady=20)
SUUname=StringVar()
SUPassw=StringVar()
SUName=StringVar()
SUEmail=StringVar()
SUNumber=StringVar()
eSUUname=Entry(frSignUp,font=('Arial', 20), textvariable=SUUname,relief=GROOVE, bd=5, fg='midnight blue').grid(row=0,column=1)
eSUPassw=Entry(frSignUp, font=('Arial', 20), textvariable=SUPassw,relief=GROOVE, bd=5,fg='midnight blue',show='*').grid(row=1,column=1)
eSUName=Entry(frSignUp, font=('Arial', 20), textvariable=SUName,relief=GROOVE, bd=5,fg='midnight blue').grid(row=2,column=1)
eSUEmail=Entry(frSignUp, font=('Arial', 20), textvariable=SUEmail,relief=GROOVE, bd=5,fg='midnight blue').grid(row=3,column=1)
eSUNumber=Entry(frSignUp, font=('Arial', 20), textvariable=SUNumber,relief=GROOVE, bd=5,fg='midnight blue').grid(row=4,column=1)
btSignInS=Button(frSignUp,font=('arial',15),text='SIGN UP',command=sign_up_s,
bd=5, fg='steel blue',justify=CENTER,activeforeground='blue',
relief=GROOVE).grid(row=5,column=1,sticky=W)
btSignInC=Button(frSignUp,font=('arial',15),text='BACK',command=sign_up_c,
bd=5, fg='steel blue',justify=CENTER,activeforeground='blue',
relief=GROOVE).grid(row=5,column=1,sticky=E)
#--------------------about----------------------------------
frAbout=Frame(root, width=1000, height=500, bg='powder blue', relief=RAISED, bd=6)
lbApp=Label(frAbout, text='The Fitness System Application',bg='powder blue', fg='midnight blue',
font=("Helvetica", 35, 'bold')).pack(side=TOP, padx=50)
lbIns=Label(frAbout,
text='This program controls your body parameters\n and manages schedule of physical exercises.\nDo sport and be healthy!',
bg='powder blue',fg="midnight blue",
font=("Helvetica", 20,)).pack(side=TOP, pady=12)
lbLang=Label(frAbout,
text='Written in Python 3 programming language.',
bg='powder blue',fg="midnight blue",
font=("Helvetica", 20, 'italic')).pack(side=TOP, pady=7,)
lbLang=Label(frAbout,
text='Authors:\nGulshen Kubra K.  [gulshen.kubra@iaau.edu.kg]\nSherkhan Naimanov [naiman.sk.jr@gmail.com]',
bg='powder blue',fg="midnight blue",
font=("Helvetica", 15, 'italic')).pack(side=TOP, pady=7,)
lbLang=Label(frAbout,
text='Thanks for using our application!',
bg='powder blue',fg="midnight blue",
font=("Helvetica", 20, 'italic')).pack(side=TOP, pady=7,)
btAboutB=Button(frAbout, font=('arial',30),text='BACK',command=about_c,
bd=5,fg='steel blue',justify=CENTER,padx=20,pady=5,activeforeground='blue',
relief=GROOVE).pack(side=TOP,pady=5)
#--------------------Editing--------------------------------
frEdit=Frame(root, width=1000, height=500)
lbEdPassw=Label(frEdit, text='New password:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=1,column=0,sticky=W, padx=20, pady=10)
lbEdPassw2=Label(frEdit, text='Re-entry password:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=2,column=0,sticky=W, padx=20, pady=10)
lbEdName=Label(frEdit, text='Full Name:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=3,column=0,sticky=W, padx=20, pady=10)
lbEdEmail=Label(frEdit, text='Email address:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=4,column=0,sticky=W, padx=20, pady=10)
lbEdnumber=Label(frEdit, text='Cellphone Number:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=5,column=0,sticky=W, padx=20, pady=10)
lbEdHeight=Label(frEdit, text='Height[cm]:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=6,column=0,sticky=W, padx=20, pady=10)
lbEdWeight=Label(frEdit, text='Weight[kg]:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=7,column=0,sticky=W, padx=20, pady=10)
lbEdGender=Label(frEdit, text='Gender[M/F]:',font=('Arial', 20,'bold'),
fg='Steel blue',anchor='w').grid(row=8,column=0,sticky=W, padx=20, pady=10)
EdPassw=StringVar()
EdPassw2=StringVar()
EdName=StringVar()
EdEmail=StringVar()
EdNumber=StringVar()
EdHeight=StringVar()
EdWeight=StringVar()
EdGender=IntVar()
eEdPassw=Entry(frEdit, font=('Arial', 20), textvariable=EdPassw,relief=GROOVE, bd=5,fg='midnight blue',show='*').grid(row=1,column=1)
eEdPassw2=Entry(frEdit, font=('Arial', 20), textvariable=EdPassw2,relief=GROOVE, bd=5,fg='midnight blue',show='*').grid(row=2,column=1)
eEdName=Entry(frEdit, font=('Arial', 20), textvariable=EdName,relief=GROOVE, bd=5,fg='midnight blue').grid(row=3,column=1)
eEdEmail=Entry(frEdit, font=('Arial', 20), textvariable=EdEmail,relief=GROOVE, bd=5,fg='midnight blue').grid(row=4,column=1)
eEdNumber=Entry(frEdit, font=('Arial', 20), textvariable=EdNumber,relief=GROOVE, bd=5,fg='midnight blue').grid(row=5,column=1)
eEdHeight=Entry(frEdit, font=('Arial', 20), textvariable=EdHeight,relief=GROOVE, bd=5,fg='midnight blue').grid(row=6,column=1)
eEdWeight=Entry(frEdit, font=('Arial', 20), textvariable=EdWeight,relief=GROOVE, bd=5,fg='midnight blue').grid(row=7,column=1)
rdGenderM=Radiobutton(frEdit,fg='steel blue',padx=25,indicatoron=0,activeforeground='midnight blue',variable=EdGender,
highlightcolor='midnight blue',borderwidth=10,font=('Arial', 20),
text='Male', value=1).grid(sticky=W,row=8, column=1)
rdGenderF=Radiobutton(frEdit,fg='steel blue',padx=20,indicatoron=0,activeforeground='midnight blue',variable=EdGender,
highlightcolor='midnight blue',borderwidth=10,font=('Arial', 20),
text='Female', value=2).grid(sticky=E,row=8, column=1)
btEdS=Button(frEdit,font=('arial',15),text='SUBMIT',command=editing_s,
bd=5, fg='steel blue',justify=CENTER,activeforeground='blue',
relief=GROOVE).grid(row=9,column=0,sticky=W, padx=20,pady=10)
btEdB=Button(frEdit,font=('arial',15),text='BACK',command=editing_c,
bd=5, fg='steel blue',justify=CENTER,activeforeground='blue',
relief=GROOVE).grid(row=9,column=1,sticky=E,pady=10)
#--------------------schedule-------------------------------
frSched=Frame(root, width=1000, height=500)
Sname=StringVar()
Sheight=StringVar()
Sweight=StringVar()
Sgender=StringVar()
Sbmi=StringVar()
infoName=Label(frSched, text='Name:',font=('Arial', 20,'bold'), relief=RIDGE, bg='gray70',
width=8, height=1,fg='blue',anchor='w').grid(row=1,column=1,sticky=W)
infoName=Label(frSched, textvariable=Sname,font=('Arial', 20,'bold'), relief=RIDGE,
width=20, height=1,fg='Steel blue',anchor='w').grid(row=1,column=2,sticky=W)
infoHeight=Label(frSched, text='Height:',font=('Arial', 20,'bold'), relief=RIDGE,bg='gray70',
width=8, height=1,fg='blue',anchor='w').grid(row=2,column=1,sticky=W)
infoHeight=Label(frSched, textvariable=Sheight,font=('Arial', 20,'bold'), relief=RIDGE,
width=20, height=1,fg='Steel blue',anchor='w').grid(row=2,column=2,sticky=W)
infoWeight=Label(frSched, text='Weight:',font=('Arial', 20,'bold'), relief=RIDGE,bg='gray70',
width=8, height=1,fg='blue',anchor='w').grid(row=3,column=1,sticky=W)
infoWeight=Label(frSched, textvariable=Sweight,font=('Arial', 20,'bold'), relief=RIDGE,
width=20, height=1,fg='Steel blue',anchor='w').grid(row=3,column=2,sticky=W)
infoGender=Label(frSched, text='Gender:',font=('Arial', 20,'bold'), relief=RIDGE,bg='gray70',
width=8, height=1,fg='blue',anchor='w').grid(row=1,column=3,sticky=W)
infoGender=Label(frSched, textvariable=Sgender,font=('Arial', 20,'bold'), relief=RIDGE,
width=20, height=1,fg='Steel blue',anchor='w').grid(row=1,column=4,sticky=W)
infoBMI=Label(frSched, text='BMI:',font=('Arial', 20,'bold'), relief=RIDGE,bg='gray70',
width=8, height=1,fg='blue',anchor='w').grid(row=2,column=3,sticky=W)
infoBMI=Label(frSched, textvariable=Sbmi,font=('Arial', 20,'bold'), relief=RIDGE,
width=20, height=1,fg='Steel blue',anchor='w').grid(row=2,column=4,sticky=W)
btShow=Button(frSched,font=('arial',10),text='SHOW INFO AND SCHEDULE',command=sched_show,
bd=5, fg='blue',justify=CENTER,activeforeground='midnight blue', padx=30,
relief=GROOVE).grid(row=13,column=4,sticky=E,pady=10)
btBack=Button(frSched,font=('arial',10),text='BACK',command=sched_back,
bd=5, fg='blue',justify=CENTER,activeforeground='midnight blue', padx=30,
relief=GROOVE).grid(row=13,column=2,sticky=E,pady=10)
##############table-info###############
infoMorn=Label(frSched, text='Morning',font=('Arial', 20,'bold'), relief=RIDGE,bg='gray70',
width=20, height=1,fg='Midnight blue',anchor='w').grid(row=4,column=2,sticky=W, pady=20)
infoEven=Label(frSched, text='Evening',font=('Arial', 20,'bold'), relief=RIDGE,bg='gray70',
width=20, height=1,fg='Midnight blue',anchor='w').grid(row=4,column=4,sticky=W, pady=20)
infoDurationM=Label(frSched, text='Duration',font=('Arial', 20,'bold'),relief=RIDGE,bg='gray70',
width=8, height=1,fg='blue',anchor='w').grid(row=5,column=1,sticky=W)
infoExM=Label(frSched, text='Exercise',font=('Arial', 20,'bold'),relief=RIDGE,bg='gray70',
width=20, height=1,fg='blue',anchor='w').grid(row=5,column=2,sticky=W)
infoDurationE=Label(frSched, text='Duration',font=('Arial', 20,'bold'),relief=RIDGE,bg='gray70',
width=8, height=1,fg='blue',anchor='w').grid(row=5,column=3,sticky=W)
infoExE=Label(frSched, text='Exercise',font=('Arial', 20,'bold'),relief=RIDGE,bg='gray70',
width=20, height=1,fg='blue',anchor='w').grid(row=5,column=4,sticky=W)
################Schedule-frame-labels################
Sfr61=StringVar()
Sfr62=StringVar()
Sfr63=StringVar()
Sfr64=StringVar()
Sfr71=StringVar()
Sfr72=StringVar()
Sfr73=StringVar()
Sfr74=StringVar()
Sfr81=StringVar()
Sfr82=StringVar()
Sfr83=StringVar()
Sfr84=StringVar()
Sfr81=StringVar()
Sfr82=StringVar()
Sfr83=StringVar()
Sfr84=StringVar()
Sfr91=StringVar()
Sfr92=StringVar()
Sfr93=StringVar()
Sfr94=StringVar()
Sfr101=StringVar()
Sfr102=StringVar()
Sfr103=StringVar()
Sfr104=StringVar()
Sfr111=StringVar()
Sfr112=StringVar()
Sfr113=StringVar()
Sfr114=StringVar()
Sfr121=StringVar()
Sfr122=StringVar()
Sfr123=StringVar()
Sfr124=StringVar()

fr61=Label(frSched, textvariable=Sfr61,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=6,column=1,sticky=W)
fr62=Label(frSched, textvariable=Sfr62,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=6,column=2,sticky=W)
fr63=Label(frSched, textvariable=Sfr63,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=6,column=3,sticky=W)
fr64=Label(frSched, textvariable=Sfr64,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=6,column=4,sticky=W)
fr71=Label(frSched, textvariable=Sfr71,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=7,column=1,sticky=W)
fr72=Label(frSched, textvariable=Sfr72,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=7,column=2,sticky=W)
fr73=Label(frSched, textvariable=Sfr73,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=7,column=3,sticky=W)
fr74=Label(frSched, textvariable=Sfr74,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=7,column=4,sticky=W)

fr81=Label(frSched, textvariable=Sfr81,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=8,column=1,sticky=W)
fr82=Label(frSched, textvariable=Sfr82,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=8,column=2,sticky=W)
fr83=Label(frSched, textvariable=Sfr83,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=8,column=3,sticky=W)
fr84=Label(frSched, textvariable=Sfr84,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=8,column=4,sticky=W)

fr91=Label(frSched, textvariable=Sfr91,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=9,column=1,sticky=W)
fr92=Label(frSched, textvariable=Sfr92,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=9,column=2,sticky=W)
fr93=Label(frSched, textvariable=Sfr93,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=9,column=3,sticky=W)
fr94=Label(frSched, textvariable=Sfr94,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=9,column=4,sticky=W)

fr101=Label(frSched, textvariable=Sfr101,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=10,column=1,sticky=W)
fr102=Label(frSched, textvariable=Sfr102,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=10,column=2,sticky=W)
fr103=Label(frSched, textvariable=Sfr103,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=10,column=3,sticky=W)
fr104=Label(frSched, textvariable=Sfr104,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=10,column=4,sticky=W)

fr111=Label(frSched, textvariable=Sfr111,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=11,column=1,sticky=W)
fr112=Label(frSched, textvariable=Sfr112,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=11,column=2,sticky=W)
fr113=Label(frSched, textvariable=Sfr113,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=11,column=3,sticky=W)
fr114=Label(frSched, textvariable=Sfr114,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=11,column=4,sticky=W)

fr121=Label(frSched, textvariable=Sfr121,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=12,column=1,sticky=W)
fr122=Label(frSched, textvariable=Sfr122,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=12,column=2,sticky=W)
fr123=Label(frSched, textvariable=Sfr123,font=('Arial', 20,'bold'),relief=RIDGE,
width=8, height=1,fg='steel blue',anchor='w').grid(row=12,column=3,sticky=W)
fr124=Label(frSched, textvariable=Sfr124,font=('Arial', 20,'bold'),relief=RIDGE,
width=20, height=1,fg='steel blue',anchor='w').grid(row=12,column=4,sticky=W)
#--------------------Main-window--------------------------------------
frMain=Frame(root, width=1000, height=500)
btAbout=Button(frMain,font=('arial',30),text='ABOUT',command=about,
bd=5,fg='steel blue',justify=CENTER,padx=168,pady=20,activeforeground='blue',
relief=GROOVE).pack(side=TOP, padx=100, pady=15)
btEdit=Button(frMain,font=('arial',30),text='EDIT PROFILE',bd=5,fg='steel blue',justify=CENTER,
padx=100,pady=20,activeforeground='blue',command=editing, relief=GROOVE).pack(side=TOP)
btSchedule=Button(frMain,font=('arial',30),text='SCHEDULE',bd=5,fg='steel blue',justify=CENTER,
padx=126,pady=20,activeforeground='blue',command=schedule,relief=GROOVE).pack(side=TOP, pady=15)
btExit=Button(frMain,font=('arial', 30),text='EXIT',bd=5,fg='steel blue',justify=CENTER,
padx=100,pady=20,activeforeground='blue',command=exit,relief=GROOVE).pack(side=BOTTOM,pady=50)
#-------------------------------------------------------------------------------------------
root.mainloop()
c.close()
conn.close()
