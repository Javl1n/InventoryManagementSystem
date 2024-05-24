from customtkinter import *
from app.database import Database

class EditForm (CTkFrame):
    def __init__(self, master, commands, supplier, **kwargs):
        super().__init__(master, width=620, height=275, **kwargs)

        self.controller = commands

        self.supplier = supplier

        header = CTkLabel(self, text="Edit Supplier", font=('default', 24, 'bold'))
        header.place(relx=.5, y=10, anchor="n")

        nameLabel = CTkLabel(self, text="Name")
        nameLabel.place(x=10, y=35)

        self.nameInput = CTkEntry(self, placeholder_text=self.supplier[1], width=600)
        self.nameInput.place(relx=.5, y=60, anchor="n")

        addressLabel = CTkLabel(self, text="Address")
        addressLabel.place(x=10, y=95)

        self.addressInput = CTkEntry(self, placeholder_text=self.supplier[2], width=600)
        self.addressInput.place(relx=.5, y=120, anchor="n")

        contactLabel = CTkLabel(self, text="Contact:")
        contactLabel.place(x=10, y=155)

        self.contactInput = CTkEntry(self, placeholder_text=self.supplier[3], width=600)
        self.contactInput.place(relx=.5, y=180, anchor="n")

        submitButton = CTkButton(self, text="SAVE", command=self.submit)
        submitButton.place(relx=.985, y=240, anchor="e")

        deleteButton = CTkButton(self, text="DELETE", fg_color="red", command=self.delete)
        deleteButton.place(relx=.015, y=240, anchor="w")

    def submit(self):
        name = self.nameInput.get()
        address = self.addressInput.get()
        contact = self.contactInput.get()

        if name == '' or address == '' or contact == '':
            if name == '':
                name = self.supplier[1]
            if address == '':
                address = self.supplier[2]
            if contact == '':
                contact = self.supplier[3]

        db = Database()
        db.query("UPDATE `suppliers` SET name=%s, address=%s, contact=%s WHERE id=%s", (name, address, contact, self.supplier[0]))
        db.commit()

        self.controller.navigate('/suppliers/show')

    def delete(self):
        db = Database()
        db.query("DELETE FROM suppliers WHERE id = %s", (self.supplier[0],))
        db.commit()
        db.query('SELECT * FROM suppliers')
        supplierId = db.getOne()
        self.controller.navigate('/suppliers',{'supplier': supplierId})