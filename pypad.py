import tkinter as tk
from tkinter import filedialog, messagebox
import platform

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.textarea = tk.Text(root)
        self.textarea.pack(expand=True, fill='both')
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", accelerator=self.get_menu_shortcut("New"), command=self.new_file)
        file_menu.add_command(label="Open", accelerator=self.get_menu_shortcut("Open"), command=self.open_file)
        file_menu.add_command(label="Save", accelerator=self.get_menu_shortcut("Save"), command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator=self.get_menu_shortcut("Exit"), command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menubar)

    def get_menu_shortcut(self, menu_option):
        if platform.system() == "Darwin":  # macOS
            return f"Command+{menu_option[0]}"
        else:
            return f"Ctrl+{menu_option[0]}"

    def new_file(self, event=None):
        self.textarea.delete(1.0, 'end')
        root.title("Untitled - TextEditor")

    def open_file(self, event=None):
        file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.textarea.delete(1.0, 'end')
            self.textarea.insert('end', file.read())
            file.close()
            root.title(f"{file.name} - TextEditor")

    def save_file(self, event=None):
        file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            file.write(self.textarea.get(1.0, 'end-1c'))
            file.close()
            messagebox.showinfo("Information", "File saved successfully.")

    def exit_app(self, event=None):
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
            root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("TextEditor")
    root.geometry("800x600")

    editor = TextEditor(root)

    root.mainloop()