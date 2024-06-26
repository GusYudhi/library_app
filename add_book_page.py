import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from utils import extract_pdf_cover
from data_handler import DataHandler
import shutil
import os

class AddBookPage(tk.Frame):
    def __init__(self, parent, controller):  
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#FFE8C8")

        self.data_handler = DataHandler("data")
        self.create_ui()
        
    def create_ui(self):
        content_frame = tk.Frame(self, bg="#FFE8C8")
        content_frame.pack(fill="both", expand=True, pady=(10, 0))  # Adjust padding to avoid overlap with header
        
        self.title_label = tk.Label(content_frame, text="Judul:", bg="#FFE8C8", font=("Times New Roman", 14))
        self.title_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.title_entry = tk.Entry(content_frame)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        self.author_label = tk.Label(content_frame, text="Penulis:", bg="#FFE8C8", font=("Times New Roman", 14))
        self.author_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.author_entry = tk.Entry(content_frame)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        self.year_label = tk.Label(content_frame, text="Tahun:", bg="#FFE8C8", font=("Times New Roman", 14))
        self.year_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.year_entry = tk.Entry(content_frame)
        self.year_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        self.pdf_path = None
        self.cover_image_path = None

        self.pdf_button = tk.Button(content_frame, text="Pilih File PDF", command=self.select_pdf)
        self.pdf_button.grid(row=3, column=0, columnspan=2, padx=100, pady=5, sticky="we")

        self.cover_label = tk.Label(content_frame, bg="white")
        self.cover_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.save_button = tk.Button(content_frame, text="Simpan", command=self.save_book)
        self.save_button.grid(row=5, column=0, columnspan=2, padx=100, pady=5, sticky="we")
        
        content_frame.grid_columnconfigure(0, weight=0, minsize=50)  # Set weight and minsize for the first column
        content_frame.grid_columnconfigure(1, weight=1, minsize=100)  # Set weight and minsize for the second column

    def select_pdf(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if pdf_path:
            self.pdf_path = pdf_path
            self.pdf_button.config(text="Ganti File PDF")
            self.cover_image_path = extract_pdf_cover(pdf_path)
            self.display_cover()

    def display_cover(self):
        if self.cover_image_path:
            cover_image = Image.open(self.cover_image_path)
            cover_image = cover_image.resize((100, 150), Image.ANTIALIAS)
            cover_photo = ImageTk.PhotoImage(cover_image)
            self.cover_label.config(image=cover_photo)
            self.cover_label.image = cover_photo

    def save_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        if title and author and year and self.pdf_path:
            books_dir = os.path.join("data", "books")
            if not os.path.exists(books_dir):
                os.makedirs(books_dir)

            new_file_path = os.path.join(books_dir, os.path.basename(self.pdf_path))
            shutil.copy(self.pdf_path, new_file_path)

            cover_image_path = extract_pdf_cover(new_file_path)

            book_info = {
                "title": title,
                "author": author,
                "year": year,
                "path": new_file_path,
                "cover": cover_image_path
            }

            # Tambahkan buku ke metadata
            self.data_handler.add_book(book_info)
            
            # Catat aktivitas penambahan buku
            self.data_handler.log_activity(f"Menambahkan buku '{title}'")

            self.reset_form()
            messagebox.showinfo("Info", "Buku berhasil ditambahkan.")
        else:
            messagebox.showerror("Error", "Mohon lengkapi semua kolom dan pilih file PDF.")


    def reset_form(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.pdf_path = None
        self.cover_image_path = None
        self.pdf_button.config(text="Pilih File PDF")
        self.cover_label.config(image=None)
