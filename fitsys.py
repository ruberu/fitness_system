import sqlite3
import getpass
conn = sqlite3.connect("fitsys.db")
c = conn.cursor()


####################################################signs up new user############################
def sign_up():
    c.execute("CREATE TABLE IF NOT EXISTS logins(uname TEXT NOT NULL UNIQUE, password TEXT NOT NULL,name TEXT, email TEXT, cnumber INTEGER)")
    conn.commit()
    c.execute("CREATE TABLE IF NOT EXISTS body(uname TEXT, height INTEGER, weight INTEGER, gender TEXT, mode INTEGER)")
    conn.commit()

    uname = input("username: ").lower()
    password = getpass.getpass("password: ")
    name = input("name: ")
    email = input("email: ").lower()

    try:
        cnumber = int(input("cellphone number: 0"))
    except:
        cnumber = int(input("enter correct cellphone number in integer format: 0"))

    while True:
        if len(uname) == 0:
            uname = input("username: ")
        else:
            break
    while True:        
        if len(password) == 0:
            password = getpass.getpass("password: ")
        else:
            break
    while True:
        if len(email) == 0:
            email = input("email: ")
        else:
            break
    while True:
        c.execute("SELECT uname FROM logins WHERE uname = '%s'"%uname)
        data = c.fetchall()

        if len(data) == 0:
            c.execute("INSERT INTO logins VALUES(?, ?, ?, ?, ?)", (uname, password, name, email, cnumber))
            conn.commit()
            c.execute("INSERT INTO body VALUES(?, ?, ?, ?, ?)", (uname, 0, 0, 'GENDER', 0))
            conn.commit()
            break    
        else:
            uname = input("Username not available. Enter new username: ")

    print("Congratulations, %s! You just have signed up!\n\n\n"%name)
    
    return uname

######################################################signs in############################################
def sign_in():
    username = input('Enter your username: ')
    password = getpass.getpass(prompt='Password:', stream = None)
    c.execute('SELECT * FROM logins WHERE uname = ? AND password = ?', (username,password,))
    if c.fetchall():
        print('Welcome')
    else:
        print('Login failed')
        uname=''
        while len(uname)==0:
            temp = input('Please enter your email address: ')
            c.execute("SELECT * FROM logins WHERE email = '%s' "%temp)
            emails = c.fetchall()
            if len(emails)>0:
                uname=(emails[0])[3]
                print('Welcome')
                continue
            else:
                print("Incorrect email")

    return username
 
#######################shows app information###############################
def about():
    print("\n\n             Fitnes System App")
    print("This program controls your body parameters and helps to manage schedule of physical exercises. Sign up and do sport!")
    print("Written in Python 3 programming language.")
    print("Authors:\nGulshen Kubra K.  [gulshen.kubra@iaau.edu.kg]\nSherkhan Naimanov [naiman.sk.jr@gmail.com]")
    print("Thanks for using our application!\n\n")

########################    edit ptofile  #################################
def editing(uname):
    print("Editing...")

    c.execute("SELECT * FROM logins WHERE uname = '%s' "%uname)
    data = c.fetchall()
    for i in data:
        print("Username     : %s"%i[0])
        print("Full Name    : %s"%i[2])
        print("Email address: %s"%i[3])
        print("CellNumber   : +(996)%i"%i[4])

    c.execute("SELECT * FROM body WHERE uname = '%s' "%uname)
    data1 = c.fetchall()
    for i in data1:
        print("Gender       : %s"%i[3])
        print("Height(cm)   : %i"%i[1])
        print("Weight(kg)   : %i"%i[2])

    mode = input("Continue editing? (Y/N)").lower()
    if mode == 'y':
    
        password = getpass.getpass("Password: ")
        name = input("Name: ")
        email = input("Email: ")
    
        while True:        
            if len(password) == 0:
                password = getpass.getpass("password: ")
            else:
                break

        while True:
            if len(email) == 0:
                email = input("email: ")
            else:
                break

        try:
            cnumber = int(input("Cell number: 0"))
        except:
            cnumber = int(input("enter correct cellphone number in integer format: 0"))
    
        try:
            height = int(input("Height(cm): "))
        except:
            height = int(input("enter correct height in integer format(cm): "))
        
        try:
            weight = int(input("Weight(kg): "))
        except:
            weight = int(input("enter correct weight in integer format(kg): 0"))

        gender = input("Gender(F/M): ").upper()

        BMI = float(weight/float(height / 100)/float(height / 100))
        print(BMI)

        if BMI < 18.5:
            modde = 1
        elif BMI >= 18.5 and BMI < 24.9:
            modde = 2
        elif BMI >= 24.9 and BMI < 29.9:
            modde = 3
        elif BMI >= 29.9:
            modde = 4

        c.execute("UPDATE logins SET password = '%s' WHERE uname = '%s' "%(password, uname))
        c.execute("UPDATE logins SET name = '%s' WHERE uname = '%s' "%(name, uname))
        c.execute("UPDATE logins SET email = '%s' WHERE uname = '%s' "%(email, uname))
        c.execute("UPDATE logins SET cnumber = %i WHERE uname = '%s' "%(cnumber, uname))
        c.execute("UPDATE body SET height = %i WHERE uname = '%s' "%(height, uname))
        c.execute("UPDATE body SET weight = %i WHERE uname = '%s' "%(weight, uname))
        c.execute("UPDATE body SET gender = '%s' WHERE uname = '%s' "%(gender, uname))
        c.execute("UPDATE body SET mode = '%s' WHERE uname = '%s' "%(modde, uname))
        
        conn.commit()



    conn.commit()
    print("\nProfile information has changed!\n")
    return uname

############################################ scheduling by ver #############################
def schedule(uname):
    c.execute("SELECT mode FROM body WHERE uname = '%s' "%uname)
    data = c.fetchall()
    data = (data[0])[0]
    conn.commit()
    return data

#############################################################################################

print("Welcome to Fitness Club!\n")
mode = input("Create new account[C] or sign in[S]?\n").lower()
uname = ""
if mode == 'c':
    uname = sign_up()
else:
    uname = sign_in()

print("Signed in as %s!\n"%uname)
while True:
    mode = input("\nselect mode [1]about  [2]edit profile  [3]schedule  [4]exit  :\n")
    if mode == '1':
        about()
    elif mode == '2':
        print(uname)
        uname = editing(uname)
    elif mode == '3':
        print("\nPhysical exercise schedule for %s :\n"%uname)
        ver = schedule(uname)
        if ver == 0:
            print("No courses are available!\nSchedule is not ready!\n")
        if ver == 2:
            print("thats is modde")
        if ver == 3:
            print("That is modde")

    elif mode == '4':
        break

c.close()
conn.close()
