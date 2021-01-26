try:
    import Tkinter as tk
except:
    import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0, column=0)


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Start page", font=(
            'Helvetica', 18, "bold")).grid(row=0, column=0)
        tk.Button(self, text="Go to page one",
                  command=lambda: master.switch_frame(PageOne)).grid(row=1, column=0)
        tk.Button(self, text="Go to page two",
                  command=lambda: master.switch_frame(PageTwo)).grid(row=1, column=1)


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='blue')
        tk.Label(self, text="Page one", font=(
            'Helvetica', 18, "bold")).grid(row=0, column=0)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=1, column=0)


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="Page two", font=(
            'Helvetica', 18, "bold")).grid(row=0, column=0)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=1, column=0)


if __name__ == "__main__":
    app = SampleApp()
    #app.overrideredirect(True)
    #app.wm_attributes("-transparentcolor", "red")
    app.attributes("-alpha", 0.9)
    app.mainloop()
