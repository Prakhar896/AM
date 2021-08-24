import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Create window when login is successful
def login_success():
    password = tk.Tk()
    password.title("Password")

    # clear items in the entry boxes
    def clear():
        entry_site.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_pass.delete(0, tk.END)

    # add password into database   
    def add():
        # Create a database or connect to one that exists
        conn = sqlite3.connect('{}.db'.format(user))
        # Create a cursor instance
        c = conn.cursor()
        # Add New Record
        c.execute("INSERT INTO manager VALUES (:platform, :username, :password)",
                {
                        'platform': entry_site.get(),
                        'username': entry_name.get(),
                        'password': entry_pass.get(),
                        
                })
        
        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()
        # Clear entry boxes
        clear()
        # Clear The Treeview Table
        tv.delete(*tv.get_children())
        # Run to pull data from database on start
        query_database()

    # delete password from database        
    def delete():
   
        conn = sqlite3.connect('{}.db'.format(user))
        c = conn.cursor()
        selected = tv.focus()
        values = tv.item(selected, 'values')
        # Delete From Database
        c.execute("DELETE from manager WHERE oid=" + values[3])
       
        conn.commit()
        conn.close()
        clear()
        tv.delete(*tv.get_children())
        query_database()

    # edit information in database
    def edit():
        selected = tv.focus()
        values = tv.item(selected, 'values')
        rowid = values[3]

        conn = sqlite3.connect('{}.db'.format(user))
        c = conn.cursor()
        # update databse with information in the entry boxes
        sqlite_update = """UPDATE manager SET platform = ? ,username = ?,
                        password = ?
                        WHERE oid = ? """
        columnValues = (entry_site.get(),entry_name.get(),entry_pass.get(),rowid)
        c.execute(sqlite_update,columnValues) 
        
        conn.commit()
        conn.close()
        
        clear()
        tv.delete(*tv.get_children())
        query_database()

    # select records and input into entry boxes using double click
    def select(e):
        clear()
        # Grab record Number
        selected = tv.focus()
        # Grab record values
        values = tv.item(selected, 'values')
        # output to entry boxes
        entry_site.insert(0, values[0])
        entry_name.insert(0, values[1])
        entry_pass.insert(0, values[2])
        

    # Create a database or connect to one that exists
    conn = sqlite3.connect('{}.db'.format(user))
    c = conn.cursor()
    # Create Table
    c.execute("""CREATE TABLE if not exists manager (
            platform text,
            username text,
            password text)
            """)
    conn.commit()
    conn.close()

    # input data in databse into treeview
    def query_database():
        # Create a database or connect to one that exists
        conn = sqlite3.connect('{}.db'.format(user))
        # Create a cursor instance
        c = conn.cursor()
        c.execute("SELECT*,rowid FROM manager")
        records = c.fetchall()
        
        # Add our data to the screen
        global count
        count = 0
        for record in records:
            tv.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2],record[3]))
            count += 1
        conn.commit()
        conn.close()

    # creating layout of window
    frame_tree = tk.Frame(password)
    frame_tree.pack(fill="both", expand=True)

    # creating treeview
    tv = ttk.Treeview(frame_tree)
    tv['columns']=(1, 2, 3,4)
    tv.column('#0', width=0, stretch=tk.NO)
    tv.column(1)
    tv.column(2)
    tv.column(3)

    # this column contains the row id that will be needed
    # in editing/deleting password in the database
    tv.column(4,width = 0, stretch=tk.NO)
    tv.pack(side=tk.LEFT,padx = 5,pady = 5,fill="both", expand=True)

    tv.heading(1, text="Platform/Site")
    tv.heading(2, text="Username")
    tv.heading(3, text="Password")

    # adding scrollbar to treeview
    sb = ttk.Scrollbar(frame_tree, orient=tk.VERTICAL)
    sb.pack(side=tk.RIGHT,fill=tk.Y)

    tv.config(yscrollcommand=sb.set)
    sb.config(command=tv.yview)

    # layout for inputing password
    frame1 = tk.Frame(password)
    frame1.pack(side= tk.LEFT)
    frame2 = tk.Frame(password)
    frame2.pack(side= tk.LEFT)
    frame3 = tk.Frame(password)
    frame3.pack(side= tk.LEFT)
    frame4 = tk.Frame(password)
    frame4.pack(side= tk.LEFT)


    label_site = tk.Label(frame1, text = "Platform")
    label_site.pack(padx=10,pady=5)

    label_name = tk.Label(frame1, text = "Username")
    label_name.pack(padx=10,pady=5)

    label_pass = tk.Label(frame1, text = "Password")
    label_pass.pack(padx=10,pady=5)

    entry_site = tk.Entry(frame2,width = 40)
    entry_site.pack(padx=10,pady=5)

    entry_name = tk.Entry(frame2,width = 40)
    entry_name.pack(padx=10,pady=5)

    entry_pass = tk.Entry(frame2,width = 40)
    entry_pass.pack(padx=10,pady=5)

    # buttons will be used to access functions above
    bn_add= tk.Button(frame3, text = "Add Password",command = add)
    bn_add.pack(fill="both",padx=15,pady=3)

    bn_del = tk.Button(frame3, text = "Delete Password", command = delete)
    bn_del.pack(fill="both",padx=15,pady=3)

    bn_edit= tk.Button(frame4, text = "Edit Password",command = edit)
    bn_edit.pack(fill="both",padx=15,pady=3)

    bn_edit= tk.Button(frame4, text = "Clear Entries",command = clear)
    bn_edit.pack(fill="both",padx=15,pady=3)

    # Bind the treeview (using double click to select record
    tv.bind("<Double-Button-1>", select)

    # input data into treeview 
    query_database()
    password.mainloop()


    
# Registration of users (verification of password)
def add_user():
    conn = sqlite3.connect('USERS.db')
    c = conn.cursor()
    username = rg_entry_name.get()
    password = rg_entry_pass.get()
    password_2 = rg_entry_pass2.get()
    c.execute("SELECT * from users")
    rows = c.fetchall()
  
    #check if entry boxes are empty
    if password_2 == "" or username == "" or password == "":
        tk.messagebox.showwarning(title="Warning!",message="Please fill in the details!")
        rg_entry_name.delete(0, tk.END)
        rg_entry_pass.delete(0, tk.END)
        rg_entry_pass2.delete(0, tk.END)
        rg_screen.destroy()

    elif any(username in i for i in rows):
        tk.messagebox.showwarning(title="Invalid!",message="Repeated Username!")
        rg_entry_name.delete(0, tk.END)
        rg_entry_pass.delete(0, tk.END)
        rg_entry_pass2.delete(0, tk.END)
        rg_screen.destroy()
        
    elif password != password_2 :
        tk.messagebox.showwarning(title="Warning!",message="Password does not match")
        rg_screen.destroy()
    
    else:
   
        c.execute("INSERT INTO users VALUES(:username, :password)",
            {
                    'username': username,
                    'password': password,   
            })
        tk.messagebox.showwarning(title="Success!",message="Registration Successful! Please login.")
        rg_screen.destroy()
        
    entry_name.delete(0, tk.END)
    entry_pass.delete(0, tk.END)

    conn.commit()
    conn.close()
  

def register_window():
    global rg_entry_name,rg_entry_pass,rg_entry_pass2,rg_screen

    # layount for register window
    rg_screen = tk.Tk()
    rg_screen.title("Register")

    rg_page = tk.Frame(rg_screen)
    rg_page.pack()
    rg_frame = tk.Frame(rg_page)
    rg_frame.pack()

    rg_frame_label = tk.Frame(rg_frame)
    rg_frame_label.pack(side=tk.LEFT)
    rg_frame_entry = tk.Frame(rg_frame)
    rg_frame_entry.pack(side=tk.LEFT)

    rg_label_name = tk.Label(rg_frame_label, text = "Username")
    rg_label_name.pack(padx=10,pady=5)

    rg_label_pass = tk.Label(rg_frame_label, text = "Password")
    rg_label_pass.pack(padx=10,pady=5)

    rg_label_pass2 = tk.Label(rg_frame_label, text = "Password")
    rg_label_pass2.pack(padx=10,pady=5)

    rg_entry_name = tk.Entry(rg_frame_entry,width = 30)
    rg_entry_name.pack(padx=10,pady=5)

    rg_entry_pass = tk.Entry(rg_frame_entry,width = 30, show = "*")
    rg_entry_pass.pack(padx=10,pady=5)

    rg_entry_pass2 = tk.Entry(rg_frame_entry,width = 30, show = "*")
    rg_entry_pass2.pack(padx=10,pady=5)

    rg_regi_bn = tk.Button(rg_page,text= "Register",width=15, command=add_user)
    rg_regi_bn.pack(pady = 5,side=tk.RIGHT,padx=10)
    
    rg_screen.mainloop()
    

# Login
def login():
    global user
    conn = sqlite3.connect('USERS.db')
    c = conn.cursor()
    username = entry_name.get()
    password = entry_pass.get()
    cursor = c.execute('SELECT * from users where username="%s" and password="%s"'%(username,password))
    if username == "" or password == "":
        tk.messagebox.showwarning(title="Warning!",message="Please fill in the details!")
    #check if username and password are valid
    else:
      if cursor.fetchone():
        tk.messagebox.showwarning(title="Success!",message="Login Success.")
        user = username
        login_screen.destroy()
        login_success()
      else:
        tk.messagebox.showwarning(title="Invalid!",message="Please enter valid username or password.")
        entry_name.delete(0, tk.END)
        entry_pass.delete(0, tk.END)
    
    conn.commit()
    conn.close()

    
# create database that contains users' information
conn = sqlite3.connect('USERS.db')
c = conn.cursor()
c.execute("""CREATE TABLE if not exists users (
        username text,
        password text)
        """)
conn.commit()
conn.close()

# layount for login window
login_screen = tk.Tk()
login_screen.title("Login")

login_page = tk.Frame(login_screen)
login_page.pack()
login_frame = tk.Frame(login_page)
login_frame.pack()

frame_label = tk.Frame(login_frame)
frame_label.pack(side=tk.LEFT)
frame_entry = tk.Frame(login_frame)
frame_entry.pack(side=tk.LEFT)

label_name = tk.Label(frame_label, text = "Username")
label_name.pack(padx=10,pady=5)

label_pass = tk.Label(frame_label, text = "Password")
label_pass.pack(padx=10,pady=5)

entry_name = tk.Entry(frame_entry,width = 30)
entry_name.pack(padx=10,pady=5)

entry_pass = tk.Entry(frame_entry,width = 30, show = "*")
entry_pass.pack(padx=10,pady=5)

login_bn = tk.Button(login_page,text= "Login",width=15, command=login)
login_bn.pack(pady = 5,side=tk.LEFT,padx=10)

regi_bn = tk.Button(login_page,text= "Register here",width=15, command=register_window)
regi_bn.pack(pady = 5,side=tk.RIGHT,padx=10)

login_screen.mainloop()