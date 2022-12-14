from tkinter import *

username = str()
window = Tk()
window.title('LOGIN N4')
window.geometry('500x300')

#o username
lb1 = Label(window,text = 'Username:').place(x=100,y=20)
username_box = Entry(window, width=20)
username_box.place(x=165,y=20)
#o password
lb2 = Label(window,text = 'Password').place(x=100,y=50)
password_box = Entry(window,width=20,show='*')
password_box.place(x=165,y=50)

def checklogin():
    name = username_box.get()
    password = password_box.get()
    info = str(name) + ';' + str(password) 
    with open('info.txt', 'r') as f:
        checkname = f.readline()
        while(checkname!=''):
            if info in checkname:
                return 1
            checkname = f.readline()
        return 0

def login():
    global username
    name = username_box.get()
    password = password_box.get()
    tbdn = Label(window)
    tbdn.place(x=100, y=80)
    if (password == '' or name == ''):
        tbdn.configure(text = "Username or Password cannot be empty", fg = 'red')
    elif (' ' in name):
        tbdn.configure(text = "Username must not contain spaces(' ')", fg = 'red')
    elif (len(name)>20 or len(password)>20):
        tbdn.configure(text = "Username or Password up to 20 characters", fg = 'red')
    elif (len(name)<6 or len(password)<6):
        tbdn.configure(text = "Username or password must have at least 6 characters", fg='red')
    elif (checklogin()):
        tbdn.configure(text = 'Logged in successfully', fg='green')
        #username = name
        window.destroy()
    else:
        tbdn.configure(text="Username or password is incorrect", fg='red')

def create_account():
    lb1  = Label(window, text="Username:").place(x=100,y=140)
    user2 = Entry(window,width=20)
    user2.place(x=220, y=140)
    lb2 = Label(window, text="Password:").place(x=100, y=170)
    password1 = Entry(window,width=20, show = '*')
    password1.place(x=220, y=170)
    lb3 = Label(window, text="Confirm Password:").place(x=100, y=200)
    confirm_pw = Entry(window,width=20, show = '*')
    confirm_pw.place(x=220, y=200)
    tbdk = Label(window)
    tbdk.place(x=100, y=230)

    def check_signup():
        name = user2.get()
        infoname = str(name) + ';' 
        with open('info.txt', 'r') as f:
            checkname = f.readline()
            while(checkname!=''):
                if infoname in checkname:
                    return 0
                checkname = f.readline()
            return 1

    def create():
        newname = user2.get()
        newpw = password1.get()
        cfpw = confirm_pw.get()
        if (newname == '' or newpw == '' or cfpw == ''):
            tbdk.configure(text="Registration information cannot be left blank", fg='red')
        elif (len(newname)>20 or len(newpw)>20 or len(cfpw)>20):
            tbdk.configure(text = "Username or Password up to 20 characters", fg='red')
        elif (len(newname)<6 or len(newpw)<6 or len(cfpw)<6):
            tbdk.configure(text = "Username or Password must have at least 6 characters", fg='red')
        elif (" " in newname):
            tbdk.configure(text = "Username must not contain spaces", fg='red')
        elif (cfpw!=newpw):
            tbdk.configure(text = "Confirm password is incorrect", fg='red')
        elif (check_signup()):
            info = str(newname) + ';' + str(newpw)
            with open('info.txt', 'a') as f:
                lines = ['\n',info]
                f.writelines(lines)
            tbdk.configure(text = "Sign up successfully", fg='green')
            window.destroy()
        else:
            tbdk.configure(text = "Username already exists", fg='red')
            #nut sign up
    signup_button = Button(window, text = 'Sign up', command=create, fg='gold', bg='black').place(x=165,y=260)


#nut login
login_button = Button(window, text = 'Login',command=login, fg='gold', bg='black').place(x=165,y=110)
#nut create account
Createaccount_button = Button(window, text = 'Create account',command = create_account ,fg='gold', bg='black').place(x=240,y=110)


window.mainloop()