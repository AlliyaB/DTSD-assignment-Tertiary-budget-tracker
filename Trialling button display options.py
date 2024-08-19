try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.frame = tk.Frame(self)
        self.frame.pack()

        self.bottomframe = tk.Frame(self)
        self.bottomframe.pack(side=tk.BOTTOM)

        # book = open_workbook('programlist.xls')
        # sheet = book.sheet_by_index(0)

        # read header values into the list
        # keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

        self.keys = ['Key', 'ProgramName', 'Path']
        self.dict_list = [{'Path': r'C:\Windows\System32\notepad.exe', 'Program': 'Notepad', 'Key': 0.0},
                          {'Path': r'C:\Windows\System32\calc.exe', 'Program': 'Calculator', 'Key': 1.0}]

        # global dict_list
        # dict_list = []
        # for row_index in xrange(1, sheet.nrows):
        #    d = {keys[col_index]: sheet.cell(row_index, col_index).value
        #       for col_index in xrange(sheet.ncols)}
        #    dict_list.append(d)

        self.w = tk.DoubleVar()
        self.w.set(self.dict_list[0]['Key'])  # initialize

        for each_program in self.dict_list:
            self.c = tk.Radiobutton(self.master, text=each_program['Program'], variable=self.w, value=each_program['Key'])
            self.c.pack(anchor=tk.W)


        self.quitButton = tk.Button(
            self.bottomframe, text="QUIT", fg="red", command=self.frame.quit
            )
        self.quitButton.pack(side=tk.LEFT, anchor=tk.S)


        self.programRun = tk.Button(self.bottomframe, text="Run", command=self.programRun)
        self.programRun.pack(side=tk.LEFT, anchor=tk.S)

    def programRun(self):
        print('Pulled path: %s' % self.search_list_dict())

    def search_list_dict(self):
        try:
            return [item for item in self.dict_list if item['Key'] == self.w.get()][0]['Path']
        except IndexError:
            return ''

app = App()
app.mainloop()