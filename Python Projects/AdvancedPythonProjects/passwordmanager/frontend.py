from tkinter import * 

class PasswordManagerGUI:
    def __init__(self, master):
        master.title("password Manager")
        master.config(padx=80, pady=80)
        self.canvas = Canvas(height=225, width=225)
        self.img = PhotoImage(file='logo.png') 
        self.canvas.create_image(120,90,image=self.img)
        self.canvas.grid(row=0, column=1)

        # labels 
        self.website = Label(text='Website')
        self.website.grid(row=1, column=0)

        self.email = Label(text='email')
        self.email.grid(row=2, column=0)

        self.password = Label(text='password')
        self.password.grid(row=3, column=0)


        self.website_entry = Entry(width=45)
        self.website_entry.grid(row=1, column=1, columnspan=3, sticky='NESW')
        self.email_entry = Entry(width=45)
        self.email_entry.grid(row=2, column=1, columnspan=3, sticky='NESW')
        self.password_entry = Entry(width=40)
        self.password_entry.grid(row=3, column=1, columnspan=2, sticky='NESW')



        #buttons
        self.generate_password_btn = Button(text='Generate')
        self.generate_password_btn.grid(row=3,column=3, sticky='NSEW')
        self.add_password_btn = Button(text='Add')
        self.add_password_btn.grid(row=4,column=1, sticky='NSEW')
        self.clear_password_btn = Button(text='Clear')
        self.clear_password_btn.grid(row=4,column=2, sticky='NSEW')
        self.search_password_btn = Button(text='Search')
        self.search_password_btn.grid(row=4,column=3, sticky='NSEW')


def main():
    main_window = Tk()
    password_manager = PasswordManagerGUI(main_window)
    main_window.mainloop()