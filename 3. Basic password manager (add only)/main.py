from tkinter import *
from tkinter import messagebox  # it is not a claas so won't be imported by that * in the above line.
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    entry_password.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]  # here we in the list part we put the range.
    password_char = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_char + password_number

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)

    window.clipboard_clear()
    window.clipboard_append(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Error", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {username}\nPassword: {password}")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {username} | {password}\n")

            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize()
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# label1 website
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

# label2 Email/username
label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

# label3 Password
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries 1
entry_website = Entry(width=35)
entry_website.focus()
entry_website.grid(column=1, row=1, sticky="EW", columnspan=2)

# Entries 2 /Email
entry_username = Entry(width=35)
entry_username.insert(0, string="Musarraf@gmail.com")  # at the beginning => End =move curser final index , 0 = move the cursor initial letter.
entry_username.grid(column=1, row=2, columnspan=2, sticky="EW")

# Entries 3
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3, sticky="EW")

# button 1 Generate password
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

# button 2 Add
button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()





