import tkinter as tk
from tkinter import Label, Entry, Button, Radiobutton

def convert_temperature():
    try:
        temperature = float(entry.get())
        unit = unit_var.get()

        if unit == "Celsius":
            converted_temperature = (temperature * 9/5) + 32
            result_label.config(text=f"Converted Temperature: {converted_temperature:.2f} °F")
        elif unit == "Fahrenheit":
            converted_temperature = (temperature - 32) * 5/9
            result_label.config(text=f"Converted Temperature: {converted_temperature:.2f} °C")
    except ValueError:
        result_label.config(text="Please enter a valid temperature.")

# Create the main window
app = tk.Tk()
app.title("Temperature Converter")

# Temperature Entry
Label(app, text="Enter Temperature:").grid(row=0, column=0, padx=5, pady=5)
entry = Entry(app)
entry.grid(row=0, column=1, padx=5, pady=5)

# Unit Selection
unit_var = tk.StringVar()
unit_var.set("Celsius")
celsius_radio = Radiobutton(app, text="Celsius", variable=unit_var, value="Celsius")
fahrenheit_radio = Radiobutton(app, text="Fahrenheit", variable=unit_var, value="Fahrenheit")
celsius_radio.grid(row=1, column=0, padx=5, pady=5)
fahrenheit_radio.grid(row=1, column=1, padx=5, pady=5)

# Convert Button
convert_button = Button(app, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Result Label
result_label = Label(app, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the Tkinter event loop
app.mainloop()