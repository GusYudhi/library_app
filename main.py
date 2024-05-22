import tkinter as tk
from opening_page import OpeningPage
from home_page import HomePage
from add_book_page import AddBookPage
from all_books_page import AllBooksPage
from recent_activity_page import RecentActivityPage

class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Perpustakaan Digital")
        self.geometry("800x600")
        self.attributes("-fullscreen", True)  # Mengatur fullscreen

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (OpeningPage, HomePage, AddBookPage, AllBooksPage, RecentActivityPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)  # Passing self as controller
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        print('selesai inisialisasi semmua halaman')
        self.show_opening_page()

    def show_opening_page(self):
        self.show_frame("OpeningPage")
        # beralih ke home_page setelah 3 detik
        self.after(3000, self.show_home_page)

    def show_home_page(self):
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
