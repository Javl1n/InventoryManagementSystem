from customtkinter import *

class Table(CTkFrame):
    def __init__(self, master, controller, columns, options, rows = None, width=1040, height=630, **kwargs):
        super().__init__(master, width=width, height=height,  **kwargs)
        for key, value in columns.items():
            CTkLabel(self, text=value['text'], font=('default', 12, 'bold')).place(x=value['x'], y=10)


        if rows is not None:
            for idy, row in enumerate(rows):
                for idx, value in enumerate(row):
                    CTkLabel(self, text=value, font=('default', 12, 'bold')).place(x=columns[idx]['x'], y=((idy + 1) * 40))
                if idy is not None:
                    if 'width' not in options.keys():
                        CTkButton(self, text=options['text'], command=lambda num=row[0]: controller.show(num) if controller.show(num) is not None else None).place(x=columns[list(columns)[-1]]['x'], y=((idy + 1) * 40))
                    else:
                        CTkButton(self, text=options['text'], width=options['width'], command=lambda num=row[0]: controller.show(num) if controller.show(num) is not None else None).place(x=columns[list(columns)[-1]]['x'], y=((idy + 1) * 40))
