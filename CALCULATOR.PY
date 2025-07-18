import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")
        master.geometry("400x550")
        master.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(master, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('Arial', 24, 'bold'), textvariable=self.input_text, width=22, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=20)

        btns_frame = tk.Frame(master, width=400, height=450, bg="grey")
        btns_frame.pack()

        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '%', '^'],
            ['⌫', '=', '', '']
        ]

        for i, row in enumerate(buttons):
            for j, btn in enumerate(row):
                if btn == '':
                    continue
                if btn == '=':
                    b = tk.Button(btns_frame, text=btn, fg="black", width=10, height=3, bd=0, bg="#2196F3", cursor="hand2",
                                  command=self.evaluate)
                elif btn == 'C':
                    b = tk.Button(btns_frame, text=btn, fg="black", width=10, height=3, bd=0, bg="#f44336", cursor="hand2",
                                  command=self.clear)
                elif btn == '⌫':
                    b = tk.Button(btns_frame, text=btn, fg="black", width=10, height=4, bd=0, bg="#FF9800", cursor="hand2",
                                  command=self.backspace)
                else:
                    b = tk.Button(btns_frame, text=btn, fg="black", width=9, height=2, bd=0, bg="red", cursor="hand2",
                                  command=lambda x=btn: self.button_click(x))
                b.grid(row=i, column=j, padx=1, pady=1)

    def button_click(self, item):
        if item == '^':
            self.expression += '**'
        else:
            self.expression += str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def evaluate(self):
        try:
            # Secure eval: only allow numbers and math operators
            allowed = set("0123456789+-*/().% ")
            if not set(self.expression.replace('**', '')).issubset(allowed):
                raise Exception("Invalid Input")
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception:
            messagebox.showerror("WRONG", "NO EXTENSHION IN THIS FORMAT DANISH RIGHT")
            self.input_text.set("")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()