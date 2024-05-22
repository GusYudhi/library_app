import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from utils import extract_pdf_cover
from data_handler import DataHandler

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
        
        self.title_label = tk.Label(content_frame, text="Judul:", bg="#FFE8C8")
        self.title_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.title_entry = tk.Entry(content_frame)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        self.author_label = tk.Label(content_frame, text="Penulis:", bg="white")
        self.author_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.author_entry = tk.Entry(content_frame)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        self.year_label = tk.Label(content_frame, text="Tahun:", bg="white")
        self.year_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.year_entry = tk.Entry(content_frame)
        self.year_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        self.pdf_path = None
        self.cover_image_path = None

        self.pdf_button = tk.Button(content_frame, text="Pilih File PDF", command=self.select_pdf)
        self.pdf_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.cover_label = tk.Label(content_frame, bg="white")
        self.cover_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.save_button = tk.Button(content_frame, text="Simpan", command=self.save_book)
        self.save_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        
        for i in range(2):  # Add weight to columns for better resizing behavior
            content_frame.grid_columnconfigure(i, weight=1)

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
            book_info = {
                "title": title,
                "author": author,
                "year": year,
                "path": self.pdf_path,
                "cover": self.cover_image_path
            }
            self.data_handler.add_book(book_info)
            self.reset_form()
            tk.messagebox.showinfo("Info", "Buku berhasil ditambahkan.")
        else:
            tk.messagebox.showerror("Error", "Mohon lengkapi semua kolom dan pilih file PDF.")

    def reset_form(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.pdf_path = None
        self.cover_image_path = None
        self.pdf_button.config(text="Pilih File PDF")
        self.cover_label.config(image=None)
