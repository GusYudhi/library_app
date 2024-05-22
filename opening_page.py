import tkinter as tk

class OpeningPage(tk.Frame):
    def __init__(self, parent, controller):  # Tambahkan parameter controller
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="lightblue")

        label = tk.Label(self, text="Selamat datang di Perpustakaan Digital", font=("Helvetica", 24), bg="lightblue")
        label.pack(expand=True)
        
        
