import tkinter as tk
from data_handler import DataHandler
import os
import tkinter.messagebox as messagebox

class AllBooksPage(tk.Frame):
    def __init__(self, parent, controller):  
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#FFE8C8")
        self.data_handler = DataHandler("data")
        self.create_ui()

    def create_ui(self):
        self.canvas = tk.Canvas(self, bg="#FFE8C8", highlightthickness=0)
        self.scrollbar_vertical = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar_horizontal = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#FFE8C8")

        self.canvas.configure(yscrollcommand=self.scrollbar_vertical.set, xscrollcommand=self.scrollbar_horizontal.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar_vertical.pack(side="right", fill="y")
        self.scrollbar_horizontal.pack(side="bottom", fill="x")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.load_all_books()

    def load_all_books(self):
        all_books = self.data_handler.get_all_books()
        for book in all_books:
            self.display_book(book)

    def display_book(self, book):
        book_frame = tk.Frame(self.scrollable_frame, bd=2, relief="groove", bg="#FFE8C8")
        book_frame.pack(padx=5, pady=5)

        cover_image = tk.PhotoImage(file=book['cover'])
        cover_label = tk.Label(book_frame, image=cover_image)
        cover_label.image = cover_image
        cover_label.pack()

        book_info_frame = tk.Frame(book_frame, bg="#FFE8C8")
        book_info_frame.pack(pady=5)

        title_label = tk.Label(book_info_frame, text=f"Judul: {book['title']}", font=("Times New Roman", 12), bg="#FFE8C8")
        title_label.pack(anchor="w")

        author_label = tk.Label(book_info_frame, text=f"Penulis: {book['author']}", font=("Times New Roman", 12), bg="#FFE8C8")
        author_label.pack(anchor="w")

        year_label = tk.Label(book_info_frame, text=f"Tahun: {book['year']}", font=("Times New Roman", 12), bg="#FFE8C8")
        year_label.pack(anchor="w")

        read_button = tk.Button(book_frame, text="Baca", command=lambda path=book['path']: self.read_book(path), font=("Times New Roman", 12), bg="#57f53b", width=10)
        read_button.pack(pady=2)

        delete_button = tk.Button(book_frame, text="Hapus", command=lambda book=book: self.confirm_delete(book), font=("Times New Roman", 12), bg="#f5663b", width=10)
        delete_button.pack(pady=2)

    def read_book(self, pdf_path):
        if os.path.exists(pdf_path):
            os.system(f"start {pdf_path}")
        else:
            tk.messagebox.showerror("Error", f"Tidak dapat menemukan file PDF di {pdf_path}")
            
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def confirm_delete(self, book):
        confirm = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus buku berjudul '{book['title']}'?")
        if confirm:
            self.delete_book(book)

    def delete_book(self, book):
        # Hapus file buku dari folder
        if os.path.exists(book['path']):
            os.remove(book['path'])

        # Hapus metadata buku dari data handler
        self.data_handler.delete_book(book)

        # Tampilkan pesan berhasil
        messagebox.showinfo("Info", f"Buku '{book['title']}' berhasil dihapus.")

        # Perbarui tampilan
        self.refresh_page()

    def refresh_page(self):
        # Hapus semua widget pada frame scrollable_frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Muat ulang semua buku
        self.load_all_books()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
