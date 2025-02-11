import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("UI Elements Example")

        # FlowLayoutPanel (аналог Frame с Pack)
        self.panel = tk.Frame(root)
        self.panel.pack(pady=10)

        # PictureBox (аналог Label с изображением)
        self.img_label = tk.Label(self.panel, text="Image will appear here", borderwidth=2, relief="solid")
        self.img_label.pack()

        # OpenFileDialog (диалог выбора файла)
        self.open_button = tk.Button(self.panel, text="Open Image", command=self.open_file)
        self.open_button.pack(pady=5)

        # DataGridView (аналог Treeview в ttk)
        self.tree = ttk.Treeview(root, columns=("A", "B", "C"), show="headings")
        self.tree.heading("A", text="Column 1")
        self.tree.heading("B", text="Column 2")
        self.tree.heading("C", text="Column 3")
        self.tree.pack(pady=10)

        # Заполнение таблицы тестовыми данными
        data = [("1", "Apple", "Red"), ("2", "Banana", "Yellow"), ("3", "Grapes", "Purple")]
        for item in data:
            self.tree.insert("", tk.END, values=item)

        # Обработчики событий
        self.tree.bind("<Double-1>", self.on_item_double_click)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", ("*.png", "*.jpg", "*.jpeg", "*.bmp"))]
        )
        if not file_path:  # Проверяем, выбрал ли пользователь файл
            return

        try:
            img = Image.open(file_path)
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(img)
            self.img_label.config(image=self.img, text="")
            self.img_label.image = self.img  # Сохранение ссылки на изображение
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")

    def on_item_double_click(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, "values")
            messagebox.showinfo("Row Selected", f"You selected: {values}")


root = tk.Tk()
app = App(root)
root.mainloop()