try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    from Tkinter import *
    import ttk
import List

BUTTON_FONT = ("Sans-Serif", 10, "bold")


class SearchWindow(Toplevel):

    """docstring for Login"""

    def __init__(self, *args):
        Toplevel.__init__(self, *args)

        self.title("Search")

        self.frame = Frame(self, padx=2, pady=2, bd=3)
        self.frame.pack()

        # Using Tk 's variable tracing
        # Checkout http://stupidpythonideas.blogspot.in/2013/12/tkinter-validation.html
        self.namevar = StringVar()
        self.namevar.trace('w', self.onUpdate)
        search = ttk.Entry(self.frame, textvariable=self.namevar)
        search.grid(row=0, columnspan=2)
        search.focus_set()
        # Binding a <Return> pressed event
        search.bind('<Return>', lambda _:  self.self.onUpdate())

        s = ttk.Style()
        s.configure("Submit.TButton", font=BUTTON_FONT, sticky="e")

        searchBtn = ttk.Button(self.frame, text="Search",
                               style="Submit.TButton",
                               command=lambda:  self.onUpdate()
                               )
        searchBtn.grid(row=0, column=3, sticky="e")
        # Awesomeness here
        self.tree = List.getTreeFrame(self, bd=3)
        self.tree.pack()

    '''*args = [name, index, mode]
        Returend by the variable tracing'''
    def onUpdate(self, *args):
        # Search regex
        content = self.namevar.get()
        searchReg = re.compile(content, re.IGNORECASE)
        self.tree.updateList(searchReg)
        return True


if __name__ == "__main__":
    root = Tk()
    Tk.iconbitmap(root, default='icon.ico')
    Tk.wm_title(root, "Test")
    Label(root, text="Root window").pack()
    new = SearchWindow(root)
    root.mainloop()
