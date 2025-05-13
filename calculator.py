from tkinter import Tk, StringVar, Entry, Button

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("328x480")
        master.config(bg="#0d1117")
        # master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        Entry(master, width=20, bg='#161b22', fg='#c9d1d9', bd=0, font=('Arial', 24),
              textvariable=self.equation, justify='right').place(x=14, y=20, height=50)

        buttons = [
            ('(', 10, 90), (')', 90, 90), ('%', 170, 90), ('/', 250, 90),
            ('7', 10, 155), ('8', 90, 155), ('9', 170, 155), ('*', 250, 155),
            ('4', 10, 220), ('5', 90, 220), ('6', 170, 220), ('-', 250, 220),
            ('1', 10, 285), ('2', 90, 285), ('3', 170, 285), ('+', 250, 285),
            ('0', 10, 350), ('.', 90, 350), ('=', 170, 350), ('C', 250, 350)
        ]

        for (text, x, y) in buttons:
            btn_color = "#21262d"
            fg_color = "#c9d1d9"

            if text == '=':
                btn_color = "#238636"
            elif text == 'C':
                btn_color = "#da3633"

            Button(master, text=text, width=5, height=2, bg=btn_color, fg=fg_color,
                   font=('Arial', 14), bd=0, command=lambda t=text: self.click(t)).place(x=x, y=y, width=68, height=55)

    def click(self, value):
        if value == "=":
            self.solve()
        elif value == "C":
            self.clear()
        else:
            self.show(value)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.entry_value = str(result)
            self.equation.set(self.entry_value)
        except:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()
