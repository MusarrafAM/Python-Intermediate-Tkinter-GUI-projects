from tkinter import *


window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

def milesToKm():
    miles = float(user_input.get())
    km = miles * 1.609
    rounded_km = round(km, 2)
    # label_display.config(text=f"{rounded_km}") # easy way to change the int to string.
    label_display.config(text=rounded_km)

# entry
user_input = Entry(width= 10)
user_input.grid(column=1, row=0)



# label 1 Miles
label_Miles = Label(text="Miles")
label_Miles.grid(column=2, row=0)
label_Miles.config(padx=10, pady=10)

# label 2 is equal to
label_equal_to = Label(text="is equal to")
label_equal_to.grid(column=0, row=1)
label_equal_to.config(padx=10, pady=10)



# label 3 display
label_display = Label(text="0")
label_display.grid(column=1, row=1)
label_display.config(padx=10, pady=10)




# label 3 KM
label_km = Label(text="Km")
label_km.grid(column=2, row=1)
label_km.config(padx=10, pady=10)




# Button Calculate
button_calc = Button(text="Calculate",command=milesToKm, bg="blue")
button_calc.grid(column=1, row=2)
button_calc.config(padx=10, pady=10)






window.mainloop()





