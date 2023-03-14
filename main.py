import tkinter

window = tkinter.Tk()
window.title("Km to mile converter")
window.minsize(width=300, height=300)
window.config(padx= 30, pady=30)

# Entry for km
km_entry = tkinter.Entry()
km_entry.config(width= 10)
km_entry.grid(row=0, column=1)

# Label for km
km_label = tkinter.Label()
km_label["text"] = "Kilometres"
km_label.grid(row=0, column=2)

# Label for instruction to miles
km_instr = tkinter.Label()
km_instr["text"] = "is equal to"
km_instr.grid(row=1, column=0)

# Label for calculated miles
mile_label = tkinter.Label()
mile_label["text"] = "0"
mile_label.grid(row=1, column=1)

# Label for miles
miles_label = tkinter.Label()
miles_label["text"] = "Miles"
miles_label.config(padx=50, pady=50)
miles_label.grid(row=1, column=2)


# Button to calc
def calc_km_to_miles():
    value_in_miles = int(km_entry.get()) / 1.609
    mile_label["text"] = value_in_miles.__round__(2)


calc = tkinter.Button(text="Calculate", command=calc_km_to_miles)
calc.grid(row=2, column=1)

window.mainloop()
