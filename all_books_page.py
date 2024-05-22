import tkinter as tk
from data_handler import DataHandler

class AllBooksPage(tk.Frame):
    def __init__(self, parent, controller):  
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#FFE8C8")
        self.data_handler = DataHandler("data")

        self.create_ui()

    def create_ui(self):
        self.book_list_frame = tk.Frame(self, bg="white")
        self.book_list_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.load_all_books()

    def load_all_books(self):
        all_books = self.data_handler.get_all_books()
        for book in all_books:
            self.display_book(book)

    def display_book(self, book):
        book_frame = tk.Frame(self.book_list_frame, bd=2, relief="groove", padx=5, pady=5, bg="white")
        book_frame.pack(pady=5, fill="x")

        cover_image = tk.PhotoImage(file=book['cover'])
        cover_label = tk.Label(book_frame, image=cover_image)
        cover_label.image = cover_image  # Keep a reference to avoid garbage collection
        cover_label.pack(side="left")

        book_info_frame = tk.Frame(book_frame, bg="white")
        book_info_frame.pack(side="left", padx=10)

        title_label = tk.Label(book_info_frame, text=f"Judul: {book['title']}", font=("Helvetica", 12), bg="white")
        title_label.pack(anchor="w")

        author_label = tk.Label(book_info_frame, text=f"Penulis: {book['author']}", font=("Helvetica", 12), bg="white")
        author_label.pack(anchor="w")

        year_label = tk.Label(book_info_frame, text=f"Tahun: {book['year']}", font=("Helvetica", 12), bg="white")
        year_label.pack(anchor="w")

        read_button = tk.Button(book_frame, text="Baca", command=lambda path=book['path']: self.read_book(path))
        read_button.pack(pady=2, side="right")

    def read_book(self, pdf_path):
        if os.path.exists(pdf_path):
            os.system(f"start {pdf_path}")
        else:
            tk.messagebox.showerror("Error", f"Tidak dapat menemukan file PDF di {pdf_path}")
