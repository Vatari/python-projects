from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import tkinter as tk
from tkinter import filedialog, messagebox

class TextEncryptorDecryptor:
    def __init__(self, root):
        self.root = root
        self.textarea = tk.Text(root)
        self.textarea.pack(expand=True, fill='both')
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Encrypt", accelerator="Ctrl+E", command=self.encrypt_file)
        file_menu.add_command(label="Decrypt", accelerator="Ctrl+D", command=self.decrypt_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menubar)

    def open_file(self, event=None):
        file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.textarea.delete(1.0, 'end')
            self.textarea.insert('end', file.read())
            file.close()
            root.title(f"{file.name} - Text Encryptor/Decryptor")

    def save_file(self, event=None):
        file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            file.write(self.textarea.get(1.0, 'end-1c'))
            file.close()
            messagebox.showinfo("Information", "File saved successfully.")

    def encrypt_file(self, event=None):
        text = self.textarea.get(1.0, 'end-1c')
        encrypted_text = self.encrypt_text(text)
        self.textarea.delete(1.0, 'end')
        self.textarea.insert('end', encrypted_text)
        messagebox.showinfo("Information", "Text encrypted successfully.")

    def decrypt_file(self, event=None):
        text = self.textarea.get(1.0, 'end-1c')
        decrypted_text = self.decrypt_text(text)
        self.textarea.delete(1.0, 'end')
        self.textarea.insert('end', decrypted_text)
        messagebox.showinfo("Information", "Text decrypted successfully.")

    def encrypt_text(self, text):
        key = b'32bytekeyforencryptingtext'  # 256-bit (32 bytes) key for AES-256
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(text.encode(), AES.block_size))
        return ciphertext.hex()

    def decrypt_text(self, text):
        key = b'32bytekeyforencryptingtext'  # 256-bit (32 bytes) key for AES-256
        cipher = AES.new(key, AES.MODE_CBC)
        decrypted = cipher.decrypt(bytes.fromhex(text))
        return unpad(decrypted, AES.block_size).decode()

    def exit_app(self, event=None):
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
            root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Text Encryptor/Decryptor")
    root.geometry("800x600")

    encryptor_decryptor = TextEncryptorDecryptor(root)

    root.mainloop()