import tkinter as tk
from tkinter import filedialog

class myapps:
    def __init__(self,root:tk.Tk,tittle:str,text:str,backgrounds:str,foregrounds:str):
        self.root=root
        self.root.title(tittle)
        self.root.configure(background=backgrounds)
        self.text=tk.Text(background=backgrounds,foreground=foregrounds)
        self.text.pack(padx=10,pady=10)
        self.text.insert("1.0",text)






def views(tittle:str="view",text:str="hello world...\n",backgrounds:str="black",foregrounds:str="white"):
    root=tk.Tk()
    apps=myapps(root,tittle,text,backgrounds,foregrounds)
    root.mainloop()





f1=filedialog.askopenfile(mode="r",defaultextension="*.*",title="open file")
a=f1.read()
views(tittle="text view",text=a)
