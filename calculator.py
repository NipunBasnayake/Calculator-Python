from tkinter import Tk, StringVar, Entry, Button, Frame

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("360x560")
        master.config(bg="#0d1117")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""

        main_frame = Frame(master, bg="#0d1117")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        Entry(
            main_frame,
            bg="#161b22",
            fg="#c9d1d9",
            bd=0,
            font=("Arial", 28),
            textvariable=self.equation,
            justify="right",
        ).pack(fill="x", pady=(0, 30), ipady=15)

        button_frame = Frame(main_frame, bg="#0d1117")
        button_frame.pack(fill="both", expand=True)

        buttons = [
            ("C", 0, 0, "#da3633"),
            ("(", 1, 0, "#21262d"),
            (")", 2, 0, "#21262d"),
            ("/", 3, 0, "#2188ff"),
            ("7", 0, 1, "#21262d"),
            ("8", 1, 1, "#21262d"),
            ("9", 2, 1, "#21262d"),
            ("*", 3, 1, "#2188ff"),
            ("4", 0, 2, "#21262d"),
            ("5", 1, 2, "#21262d"),
            ("6", 2, 2, "#21262d"),
            ("-", 3, 2, "#2188ff"),
            ("1", 0, 3, "#21262d"),
            ("2", 1, 3, "#21262d"),
            ("3", 2, 3, "#21262d"),
            ("+", 3, 3, "#2188ff"),
            ("0", 0, 4, "#21262d", 2),
            (".", 2, 4, "#21262d"),
            ("=", 3, 4, "#238636"),
        ]

        for i in range(4):
            button_frame.columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)

        for button in buttons:
            if len(button) == 5:
                text, col, row, color, colspan = button
                btn = Button(
                    button_frame,
                    text=text,
                    bg=color,
                    fg="#ffffff",
                    font=("Arial", 16, "bold"),
                    bd=0,
                    cursor="hand2",
                    activebackground=self.darken_color(color),
                    activeforeground="#ffffff",
                    command=lambda t=text: self.click(t),
                )
                btn.grid(
                    row=row,
                    column=col,
                    columnspan=colspan,
                    sticky="nsew",
                    padx=5,
                    pady=5,
                )
            else:
                text, col, row, color = button
                btn = Button(
                    button_frame,
                    text=text,
                    bg=color,
                    fg="#ffffff",
                    font=("Arial", 16, "bold"),
                    bd=0,
                    cursor="hand2",
                    activebackground=self.darken_color(color),
                    activeforeground="#ffffff",
                    command=lambda t=text: self.click(t),
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    def darken_color(self, hex_color):
        """Darken a hex color for button press effect"""
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        factor = 0.8
        r = max(0, int(r * factor))
        g = max(0, int(g * factor))
        b = max(0, int(b * factor))

        return f"#{r:02x}{g:02x}{b:02x}"

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
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.entry_value = str(result)
            self.equation.set(self.entry_value)
        except:
            self.equation.set("Error")
            self.entry_value = ""


if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
