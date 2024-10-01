from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
""" here we create a new entry as a dictionary.  we then load that new_data dictionary into a
json file where all of the entries are stored."""

def save():


    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        #open the file in "read" mode
        #Try to open this json file
        try:
            with open("data.json", "r") as data_file:
        #reading old data
                data = json.load(data_file)
       #If that file is not found then we need to create the file
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        # If the file was found and already exists then we are going to proceed with this else-statement
        else:
            #Updating old data with new data
            data.update(new_data)

            # open the file in "write" mode
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent= 4)
        #finally after the above logic, we will then end with this following.
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search ------------------------------- #
def search():
    search_data = {}
    site = website_entry.get()
    print(site)
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=site,
                            message="No info found")

    else:
        if site in data:
            #print(f"username: {data[site]["email"]} \n Password: {data[site]["password"]}")
            messagebox.showinfo(title=site, message =f"username: {data[site]["email"]} \n Password: {data[site]["password"]}"  )
        else:
            messagebox.showinfo(title=site,
                                message="No info found")


        #try:
            #data = json.load(data_file)
            #print(type(data))
            #print(data[site])
            #print(f"username: {data[site]["email"]} \n Password: {data[site]["password"]}")
        #except KeyError:
        #    print("info not found")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "joe@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

find_password_button = Button(text="Search", width=15, command=search)
find_password_button.grid(row=1, column=2)

window.mainloop()