from tkinter import *

# Create a GUI window
window = Tk()

def from_kg():

    weight_kg = float(gram2_value.get())
    
    # Convert kg to gram, pound, and ounce
    gram = weight_kg * 1000
    pound = weight_kg * 2.20462
    ounce = weight_kg * 35.274
    
    text1.delete("1.0", END)
    text1.insert(END, gram)
    
    text2.delete("1.0", END)
    text2.insert(END, pound)
    
    text3.delete("1.0", END)
    text3.insert(END, ounce)

# Create the Label widgets
gram1 = Label(window, text="Enter the weight in Kg")
gram2_value = StringVar()
gram2 = Entry(window, textvariable=gram2_value)
gram3 = Label(window, text='Gram')
gram4 = Label(window, text='Pounds')
gram5 = Label(window, text='Ounce')

# Create the Text Widgets
text1 = Text(window, height=1, width=20)
text2 = Text(window, height=1, width=20)
text3 = Text(window, height=1, width=20)


button1 = Button(window, text="Convert", command=from_kg)


gram1.grid(row=0, column=0)
gram2.grid(row=0, column=1)
button1.grid(row=0, column=2)
gram3.grid(row=1, column=0)
gram4.grid(row=1, column=1)
gram5.grid(row=1, column=2)
text1.grid(row=2, column=0)
text2.grid(row=2, column=1)
text3.grid(row=2, column=2)

window.mainloop()
