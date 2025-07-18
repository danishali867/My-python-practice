import tkinter as tk

def convert():
    temp = entry.get()

    if temp != "":
        celsius = float(temp)
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"Fahrenheit: {fahrenheit:.2f}")
    elif temp == "":
        result_label.config(text="Please enter a value")

# GUI window
window = tk.Tk()
window.title("Celsius to Fahrenheit")

# Input label & entry
tk.Label(window, text="Enter Celsius:").pack()
entry = tk.Entry(window)
entry.pack()


# Convert button
tk.Button(window, text="Convert", command=convert).pack()

# Result
result_label = tk.Label(window, text="")
result_label.pack()

# Start GUI
window.mainloop()