try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import _support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = __(root)
    _support.init(root, top)
    root.mainloop()


w = None


def create___(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = __(w)
    _support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy___():
    global w
    w.destroy()
    w = None


class __:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("500x500+356+100")
        top.title("New Toplevel")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(width=425)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.0, rely=0.0, height=50, width=50)
        self.Button1.configure(text='''Button1''')

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.menubar.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            compound="left",
            font="TkMenuFont",
            foreground="#000000",
            label="刷新")


if __name__ == '__main__':
    vp_start_gui()
