from customtkinter import *
from app.database import Database
from app.localstorage import LocalStorage

class CreateForm (CTkFrame):
    def __init__(self, master, commands, **kwargs):
        super().__init__(master, width=620, height=370, **kwargs)

        self.controller = commands

        itemLabel = CTkLabel(self, text="Item")
        itemLabel.place(x=10, y=10)

        self.itemInput = CTkOptionMenu(self, values=self.items(), width=600)
        self.itemInput.place(relx=.5, y=35, anchor="n")

        supplierLabel = CTkLabel(self, text="Supplier")
        supplierLabel.place(x=10, y=70)

        self.supplierInput = CTkOptionMenu(self, values=self.suppliers(), width=600)
        self.supplierInput.place(relx=.5, y=95, anchor="n")

        dateLabel = CTkLabel(self, text="Date")
        dateLabel.place(x=10, y=130)

        self.monthInput = CTkEntry(self, placeholder_text="Month (1-12)", width=195)
        self.monthInput.place(x=10, y=155)

        self.dayInput = CTkEntry(self, placeholder_text="Day (1-31)", width=195)
        self.dayInput.place(x=10+200, y=155)

        self.yearInput = CTkEntry(self, placeholder_text="Year", width=200)
        self.yearInput.place(x=10+400, y=155)

        ammountLabel = CTkLabel(self, text="Amount")
        ammountLabel.place(x=10, y=190)

        self.ammount = CTkEntry(self, placeholder_text="Aa", width=600)
        self.ammount.place(relx=.5, y=215, anchor="n")

        expDateLabel = CTkLabel(self, text="Expiration Date")
        expDateLabel.place(x=10, y=250)

        self.expMonthInput = CTkEntry(self, placeholder_text="Month (1-12)", width=195)
        self.expMonthInput.place(x=10, y=275)

        self.expDayInput = CTkEntry(self, placeholder_text="Day (1-31)", width=195)
        self.expDayInput.place(x=10 + 200, y=275)

        self.expYearInput = CTkEntry(self, placeholder_text="Year", width=200)
        self.expYearInput.place(x=10 + 400, y=275)

        submitButton = CTkButton(self, text="SUBMIT", command=self.submit)
        submitButton.place(relx=.5, y=355, anchor="s")

    def submit(self):
        month = self.monthInput.get()
        day = self.dayInput.get()
        year = self.yearInput.get()
        ammount = self.ammount.get()
        expMonth = self.expMonthInput.get()
        expDay = self.expDayInput.get()
        expYear = self.expYearInput.get()

        if month == '' or day == '' or year == '' or ammount == '' or expMonth == '' or expDay == '' or expYear == '':
            return

        database = Database()
        database.query("SELECT id, quantity FROM items WHERE `name` = %s", (self.itemInput.get(),))

        item = database.getOne()
        itemId = item[0]
        originalQuantity = item[1]

        database.query("SELECT id FROM suppliers WHERE `name` = %s", (self.supplierInput.get(),))

        supplier = database.getOne()[0]

        storage = LocalStorage()
        user = storage.shelf['user']['id']

        database.query("INSERT INTO item_in(item_id, supplier_id, date, quantity, user_id, expiration_date) VALUES (%s, %s, %s, %s, %s, %s)", (itemId, supplier, year + '-' + month + '-' + day, ammount, user, expYear + '-' + expMonth + '-' + expDay))
        database.commit()


        database.query("UPDATE items SET quantity=%s WHERE id=%s", (
            int(originalQuantity) + int(ammount),
            itemId
        ))
        database.commit()


        self.controller.navigate('/movements')


    def suppliers(self):
        database = Database()
        database.query("Select name FROM suppliers")
        categoriesData = database.get()
        categoriesArray = [];

        for category in categoriesData:
            categoriesArray.append(category[0])

        return categoriesArray

    def items(self):
        database = Database()
        database.query("Select name FROM items")
        categoriesData = database.get()
        categoriesArray = [];

        for category in categoriesData:
            categoriesArray.append(category[0])

        return categoriesArray
