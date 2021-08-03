import os, sys, subprocess
import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()
apps = []
#System Functions
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

#UI And Refresh Functions
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

def refreshApps():
    for widget in frame.winfo_children():
        widget.destroy()

    for app in apps:
        label = tk.Label(frame, text=app, bg="white")
        label.pack()

#Load up file
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        refreshApps()

counterLabel = tk.Label(root, text="Total Apps: {}".format(len(apps)), bg="white")
counterLabel.pack()

#Button Functions
def addApp():
    filename = filedialog.askopenfilename(initialdir="/Applications", title="Select File",
    filetypes=(("executables", "*.app"), ("all files", "*.*")))

    apps.append(filename)

    refreshApps()

def runApps():
    for app in apps:
        open_file(app)

def clearApps():
    apps = []
    refreshApps()

newApp = tk.Button(root, text="New App", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
newApp.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

deleteApps = tk.Button(root, text="Clear all Apps", padx=10, pady=5, fg="white", bg="#263D42", command=clearApps)
deleteApps.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')