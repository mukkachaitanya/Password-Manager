try:
    from tkinter import *
    from Tkinter import ttk
except ImportError:
    from Tkinter import *
    import ttk

import Add
import hashlib
import encode
import List


LARGE_FONT = ("Verdana", 13)
BUTTON_FONT = ("Sans-Serif", 10, "bold")


class Login(Tk):
    """docstring for Login"""

    def __init__(self, *args):
        Tk.__init__(self, *args)
        Tk.iconbitmap(self, default='icon.ico')
        Tk.wm_title(self, "Password Manager")
        self.state = {
            "text": "Login to access password database.", "val": False}

        self.addLoginFrame()

        # Adding frames

    def addLoginFrame(self, *kwargs):
        login = Frame(self, padx=2, pady=2, bd=2)
        login.pack()

        loginLabel = Label(login, text=self.state['text'],
                           bd=10, font=LARGE_FONT, width=30)
        loginLabel.grid(row=0, columnspan=3)

        entry = ttk.Entry(login, show="*")
        entry.grid(row=1, column=1, pady=3)
        # _ marks an unused variable; used for lambda compatibility
        # Bind event for when enter is pressed in the Entry
        entry.bind('<Return>', lambda _: self.checkPwd(
            login, label=loginLabel, entry=entry, btn=submitBtn))

        s = ttk.Style()
        s.configure("Submit.TButton", font=BUTTON_FONT)
        submitBtn = ttk.Button(login, text="Submit", style="Submit.TButton",
                               command=lambda: self.checkPwd(
                                   login, label=loginLabel, entry=entry,
                                   btn=submitBtn))

        submitBtn.grid(row=2, column=1, pady=3)

    def checkPwd(self, frame, **kwargs):
        chk = kwargs['entry'].get()
        # if passwords match
        if hashlib.md5(chk).hexdigest() == encode.password:

            self.state['text'] = "Logged In"
            self.state['val'] = True
            # Using .config() to modift the args
            kwargs['label'].config(text=self.state['text'])
            kwargs['entry'].config(state=DISABLED)
            kwargs['btn'].config(state=DISABLED)

            # adding buttons
            self.addConfigBtn(frame)

        # If passwords don't match
        else:
            kwargs['label'].config(text=self.state['text'] + "\nTry Again!!!")

    def addConfigBtn(self, login):
        # configured buttons
        # btnList = (addBtn, listBtn, getBtn)

        # Creating temp references to images using temp1,2,3 so as to disallow
        # garbage collection problems
        btnList = ["Add", "List", "Search"]
        btnCmdList = [lambda: Add.AddWindow(self),
                      lambda: List.ListWindow(self),
                      quit]
        f = []  # Frames array
        img = []  # image array
        self.temp = []  # temp array

        for i in xrange(3):
            f.append(Frame(login, padx=2, width=50, height=50))
            f[i].grid(row=3, column=i)
            img.append(PhotoImage(
                file=btnList[i] + ".gif", width=48, height=48))
            self.temp.append(img[i])
            ttk.Button(f[i], image=img[i], text=btnList[i], compound="top",
                       style="Submit.TButton",
                       command=btnCmdList[i]).grid(sticky="NWSE")


if __name__ == '__main__':
    new = Login()
    new.mainloop()
