import tkinter as tk
from data_handler import DataHandler

class RecentActivityPage(tk.Frame):
    def __init__(self, parent, controller):  
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#FFE8C8")
        self.data_handler = DataHandler("data")
        self.create_header()
        self.create_ui()

    def create_header(self):
        header_frame = tk.Frame(self, bg="#EC8F5E", height=50)
        header_frame.pack(side="top", fill="x")

        header_label = tk.Label(header_frame, text="Perpustakaan Digital", font=("Rockwell Condensed", 24), bg="#EC8F5E")
        header_label.pack(pady=10)

    def create_ui(self):
        self.activity_list_frame = tk.Frame(self, bg="white")
        self.activity_list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.load_recent_activities()

    def load_recent_activities(self):
        recent_activities = self.data_handler.get_recent_activities()
        for activity in recent_activities:
            self.display_activity(activity)

    def display_activity(self, activity):
        activity_frame = tk.Frame(self.activity_list_frame, bd=2, relief="groove", padx=5, pady=5, bg="white")
        activity_frame.pack(pady=5, fill="x")

        activity_label = tk.Label(activity_frame, text=activity, font=("Helvetica", 12), bg="white")
        activity_label.pack(anchor="w")
