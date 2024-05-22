import os
import json
import datetime

class DataHandler:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.metadata_file = os.path.join(self.data_folder, "metadata.json")
        self.activity_file = os.path.join(self.data_folder, "activities.json")

        # Buat folder data jika belum ada
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

        # Buat file metadata.json jika belum ada
        if not os.path.exists(self.metadata_file):
            with open(self.metadata_file, 'w') as file:
                json.dump([], file)

        # Buat file activities.json jika belum ada
        if not os.path.exists(self.activity_file):
            with open(self.activity_file, 'w') as file:
                json.dump([], file)

        self.load_metadata()
        self.load_activities()

    def load_metadata(self):
        try:
            with open(self.metadata_file, 'r') as file:
                self.metadata = json.load(file)
        except json.JSONDecodeError:
            self.metadata = []
            self.save_metadata()  # Menyimpan metadata dengan daftar kosong jika ada kesalahan

    def load_activities(self):
        try:
            with open(self.activity_file, 'r') as file:
                self.activities = json.load(file)
        except json.JSONDecodeError:
            self.activities = []
            self.save_activities()  # Menyimpan activities dengan daftar kosong jika ada kesalahan

    def save_metadata(self):
        with open(self.metadata_file, 'w') as file:
            json.dump(self.metadata, file, indent=4)

    def save_activities(self):
        with open(self.activity_file, 'w') as file:
            json.dump(self.activities, file, indent=4)

    def add_book(self, book_info):
        self.metadata.append(book_info)
        self.save_metadata()
        self.log_activity(f"Menambahkan buku '{book_info['title']}'")

    def get_all_books(self):
        return self.metadata

    def search_book(self, title):
        return [book for book in self.metadata if title.lower() in book['title'].lower()]

    def get_favorites(self):
        # Implementasi favorit bisa dengan menambahkan field 'favorite' di metadata
        return [book for book in self.metadata if book.get('favorite')]

    def log_activity(self, activity):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activities.append(f"{timestamp} - {activity}")
        self.save_activities()

    def get_recent_activities(self):
        return self.activities[-10:]  # Mengambil 10 aktivitas terbaru
