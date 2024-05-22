import tkinter as tk
from add_book_page import AddBookPage
from all_books_page import AllBooksPage
from recent_activity_page import RecentActivityPage
from data_handler import DataHandler
from utils import extract_pdf_cover
import os

class HomePage(tk.Frame):
    def __init__(self, parent, controller):  
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#FFE8C8")

        self.data_handler = DataHandler("data")
        self.create_ui()

    def create_ui(self):
        sidebar = tk.Frame(self, bg="#FFA62F", width=200)
        sidebar.pack(fill="y", side="left")

        home_button = tk.Button(sidebar, text="Beranda", command=self.show_home, font=("Helvetica", 14))
        home_button.pack(fill="x")

        add_book_button = tk.Button(sidebar, text="Tambahkan Koleksi Buku", command=self.show_add_book, font=("Helvetica", 14))
        add_book_button.pack(fill="x")

        all_books_button = tk.Button(sidebar, text="Semua Koleksi Buku", command=self.show_all_books, font=("Helvetica", 14))
        all_books_button.pack(fill="x")

        recent_activity_button = tk.Button(sidebar, text="Aktivitas Terbaru", command=self.show_recent_activity, font=("Helvetica", 14))
        recent_activity_button.pack(fill="x")

        self.content_frame = tk.Frame(self, bg="white")
        self.content_frame.pack(fill="both", expand=True, side="right")

        self.show_home()

    def show_home(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        search_frame = tk.Frame(self.content_frame, bg="#FFE8C8")
        search_frame.pack(fill="x")

        search_label = tk.Label(search_frame, text="Cari Buku:", bg="White", font=("Helvetica", 14))
        search_label.pack(side="left", padx=5)

        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side="left", padx=5, fill="x", expand=True)

        search_button = tk.Button(search_frame, text="Cari", command=self.search_book, font=("Helvetica", 14))
        search_button.pack(side="left", padx=5)

        self.favorites_frame = tk.Frame(self.content_frame, bg="#FFE8C8")
        self.favorites_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.load_favorites()

    def load_favorites(self):
        favorite_books = self.data_handler.get_favorites()
        for book in favorite_books:
            self.display_book(book, self.favorites_frame)

    def search_book(self):
        search_term = self.search_entry.get()
        search_results = self.data_handler.search_book(search_term)
        for widget in self.favorites_frame.winfo_children():
            widget.destroy()

        if search_results:
            for book in search_results:
                self.display_book(book, self.favorites_frame)
        else:
            no_result_label = tk.Label(self.favorites_frame, text="Tidak ditemukan buku dengan judul tersebut.", bg="#FFE8C8")
            no_result_label.pack()

    def display_book(self, book, parent):
        book_frame = tk.Frame(parent, bd=2, relief="groove", padx=5, pady=5, bg="#FFE8C8")
        book_frame.pack(pady=5, fill="x")

        cover_image = tk.PhotoImage(file=book['cover'])
        cover_label = tk.Label(book_frame, image=cover_image)
        cover_label.image = cover_image  # Keep a reference to avoid garbage collection
        cover_label.pack(side="left")

        book_info_frame = tk.Frame(book_frame, bg="#FFE8C8")
        book_info_frame.pack(side="left", padx=10)

        title_label = tk.Label(book_info_frame, text=f"Judul: {book['title']}", font=("Helvetica", 14), bg="#FFE8C8")
        title_label.pack(anchor="w")

        author_label = tk.Label(book_info_frame, text=f"Penulis: {book['author']}", font=("Helvetica", 14), bg="#FFE8C8")
        author_label.pack(anchor="w")

        year_label = tk.Label(book_info_frame, text=f"Tahun: {book['year']}", font=("Helvetica", 14), bg="#FFE8C8")
        year_label.pack(anchor="w")

        read_button = tk.Button(book_frame, text="Baca", font=("Helvetica", 14), command=lambda path=book['path']: self.read_book(path))
        read_button.pack(pady=2, side="right")

    def read_book(self, pdf_path):
        if os.path.exists(pdf_path):
            os.system(f"start {pdf_path}")
        else:
            tk.messagebox.showerror("Error", f"Tidak dapat menemukan file PDF di {pdf_path}")

    def show_add_book(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        AddBookPage(self.content_frame, self.data_handler).pack(fill="both", expand=True)

    def show_all_books(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        AllBooksPage(self.content_frame, self.data_handler).pack(fill="both", expand=True)

    def show_recent_activity(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        RecentActivityPage(self.content_frame, self.data_handler).pack(fill="both", expand=True)