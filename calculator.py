from tkinter import Tk, StringVar, Entry, Button

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("400x600")
        master.config(bg="lightblue")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value=''
        Entry(width=16, bg='#fff', font=('Arial Bold', 24), textvariable=self.equation).place(x=0, y=0)
        
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result= eval(self.entry_value)
        self.entry_value = str(result)

root = Tk()
root.mainloop()