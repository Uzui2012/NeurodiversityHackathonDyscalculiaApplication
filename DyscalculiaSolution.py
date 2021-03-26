import pyperclip
import tkinter as tk
from PIL import ImageTk, Image  

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_background()
        self.create_widgets()

    def create_background(self, path="apple.png"):
        img1 = Image.open(path)
        #img1 = img1.resize((100,100), Image.ANTIALIAS)
        self.test_image = ImageTk.PhotoImage(img1)
        self.background = tk.Label(image=self.test_image)
        self.background.place(x=0, y=0)

    def create_widgets(self):
        
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.btn_update
        self.hi_there.pack(side="top")
        

    def btn_update(self):
        self.edit_text(pyperclip.paste())

    def edit_text(self, in_str):
        self.hi_there["text"] = in_str
        self.hi_there.pack(side="top")

#s = pyperclip.paste()
root = tk.Tk()
app = Application(master=root)
app.mainloop()
