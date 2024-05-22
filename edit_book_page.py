import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from utils import extract_pdf_cover
from data_handler import DataHandler
import shutil
import os

class EditBookPage(tk.Frame):
    def __init__(self, parent, controller, book_info):  
        super().__init__(parent)
        self.controller = controller
        self.book_info = book_info
        self.configure(bg="#FFE8C8")

        self.data_handler = DataHandler("data")
        self.create_ui()
        
    def create_ui(self):
        content_frame = tk.Frame(self, bg="#FFE8C8")
        content_frame.pack(fill="both", expand=True, pady=(10, 0))  # Adjust padding to avoid overlap with header
        
        self.title_label = tk.Label(content_frame, text="Judul:", bg="#FFE8C8", font=("Times New Roman", 14))
        self.title_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.title_entry = tk.Entry(content_frame)
        self.title_entry.insert(0, self.book_info["title"])
        self.title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        self.author_label = tk.Label(content_frame, text="Penulis:", bg="#FFE8C8", font=("Times New Roman", 14))
        self.author_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.author_entry = tk.Entry(content_frame)
        self.author_entry.insert(0, self.book_info["author"])
        self.author_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        self.year_label = tk.Label(content_frame, text="Tahun:", bg="#FFE8C8", font=("Times New Roman", 14))
        self.year_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.year_entry = tk.Entry(content_frame)
        self.year_entry.insert(0, self.book_info["year"])
        self.year_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        self.save_button = tk.Button(content_frame, text="Simpan", command=self.save_book)
        self.save_button.grid(row=3, column=0, columnspan=2, padx=100, pady=5, sticky="we")
        
        content_frame.grid_columnconfigure(0, weight=0, minsize=50)  # Set weight and minsize for the first column
        content_frame.grid_columnconfigure(1, weight=1, minsize=100)  # Set weight and minsize for the second column

    def save_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        if title and author and year:
            book_info = {
                "title": title,
                "author": author,
                "year": year,
                "path": self.book_info["path"],
                "cover": self.book_info["cover"]
            }
            # Perbarui metadata buku
            self.data_handler.update_book(self.book_info["path"], book_info)
            # Catat aktivitas perubahan buku
            self.data_handler.log_activity(f"Mengedit buku '{title}'")
            messagebox.showinfo("Info", "Informasi buku berhasil diperbarui.")
        else:
            messagebox.showerror("Error", "Mohon lengkapi semua kolom.")