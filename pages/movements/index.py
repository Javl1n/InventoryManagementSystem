from customtkinter import *
from components import navigation, table
from app.database import Database


class MovementPage(CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)

        self.controller = controller

        navigation.NavigationFrame(self, controller=controller).place(x=0, y=0)

        title = CTkLabel(self, text="MOVEMENTS", font=("default", 32, "bold")).place(y=20, x=220)
        add = CTkLabel(self, text="Add Movement: ", font=("default", 16)).place(y= 20, x=850)

        addIn = CTkButton(self, text="In", command=lambda: self.controller.navigate('/movements/in/create')).place(y=35, x=1040, anchor="center")
        addOut = CTkButton(self, text="Out", command=lambda: self.controller.navigate('/movements/out/create')).place(y=35, x=1190, anchor="center")

        inTitle = CTkLabel(self, text="IN", font=("default", 24, "bold")).place(y=70, x=450)
        headers = {
            0: {
                'x': 25,
                'text': "ID",
            },
            1: {
                'x': 70,
                'text': 'Item'
            },
            2: {
                'x': 200,
                'text': 'Date'
            },
            3: {
                'x': 340,
                'text': 'Qty.'
            },
            4: {
                'x': 390,
                'text': ''
            },
        }
        database = Database()
        database.query("SELECT item_in.id, items.name, item_in.date, item_in.quantity FROM item_in INNER JOIN items ON item_in.item_id = items.id")
        itemsQuery = database.get()
        items = itemsQuery
        button = {
            'text': 'view',
            'width': 100
        }
        class In():
            def __init__(self, controller):
                self.outer = controller
            def show(self, inId):
                self.outer.controller.navigate('/movements/in', {'moveIn': inId})

        self.moveInClass = In(self)
        self.table = table.Table(
            self,
            controller=self.moveInClass,
            columns=headers,
            rows=items,
            options=button,
            width=515, height=600
        ).place(y=100, x=220)

        outTitle = CTkLabel(self, text="OUT", font=("default", 24, "bold")).place(y=70, x=450 + 520)
        headers = {
            0: {
                'x': 25,
                'text': "ID",
            },
            1: {
                'x': 70,
                'text': 'Item'
            },
            2: {
                'x': 200,
                'text': 'Date'
            },
            3: {
                'x': 340,
                'text': 'Qty.'
            },
            4: {
                'x': 390,
                'text': ''
            },
        }
        database = Database()
        database.query("SELECT item_out.id, items.name, item_out.date, item_out.quantity FROM item_out INNER JOIN items ON item_out.item_id = items.id")
        items = database.get()
        button = {
            'text': 'view',
            'width': 100
        }

        class Out():
            def __init__(self, controller):
                self.outer = controller

            def show(self, outId):
                self.outer.controller.navigate('/movements/out', {'moveOut': outId})

        self.moveOutClass = Out(self)
        self.table = table.Table(
            self,
            controller=self.moveOutClass,
            columns=headers,
            rows=items,
            options=button,
            width=515, height=600
        ).place(y=100, x=220 + 520 + 5)