from tkinter import *

KM_MULTIPLIER = 1.609

# window
window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
# equal label
label_one = Label(text='is equal to')
label_one.grid(column=0, row=1)


def miles_to_km():
    miles = float(input_box.get())
    km = round(miles * KM_MULTIPLIER, 2)
    # label_two['text'] = km
    label_two['text'] = str(km)  # <--- learned something new
    # label_two['text'] = '{km}'.format(km=km)
    # label_two['text'] = f'{km}'


# entry
# input_box = Entry(width=7)
input_box = Entry(width=10)
input_box.insert(END, string='0')
input_box.grid(column=1, row=0)
# kilometres label one
label_two = Label(text='0')
label_two.grid(column=1, row=1)
# button
# calculate_btn = Button('Calculate')  # <-- don't do this!
calculate_btn = Button(text='Calculate', command=miles_to_km)
calculate_btn.grid(column=1, row=2)
# miles label
label_three = Label(text='Miles')
label_three.grid(column=2, row=0)
# kilometres label two
label_four = Label(text='Km')
label_four.grid(column=2, row=1)

window.mainloop()
