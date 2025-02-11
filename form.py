import tkinter as tk

class MyForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Форма на Tkinter")

        self.label = tk.Label(root, text="Введите имя:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="ОК", command=self.say_hello)
        self.button.pack()

    def say_hello(self):
        name = self.entry.get()
        print(f"Привет, {name}!")

root = tk.Tk()
app = MyForm(root)
root.mainloop()