from customtkinter import *

class Table(CTkFrame):
    def __init__(self, master, controller, columns, rows = None, **kwargs):
        super().__init__(master, width=1040, height=630,  **kwargs)

        for key, value in columns.items():
            CTkLabel(self, text=value['text'], font=('default', 12, 'bold')).place(x=value['x'], y=10)

        if rows is not None:
            for idy, row in enumerate(rows):
                for idx, value in enumerate(row):
                    CTkLabel(self, text=value, font=('default', 12, 'bold')).place(x=columns[idx]['x'], y=((idy + 2) * 20))
