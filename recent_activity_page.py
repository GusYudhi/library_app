import tkinter as tk
from data_handler import DataHandler

class RecentActivityPage(tk.Frame):
    def __init__(self, parent, controller):  
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#FFE8C8")
        self.data_handler = DataHandler("data")
        self.create_ui()

    def create_ui(self):
        self.activity_list_frame = tk.Frame(self, bg="#FFE8C8")
        self.activity_list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.load_recent_activities()

    def load_recent_activities(self):
        recent_activities = self.data_handler.get_recent_activities()
        for activity in recent_activities:
            self.display_activity(activity)

    def display_activity(self, activity):
        activity_frame = tk.Frame(self.activity_list_frame, bd=2, relief="groove", padx=5, pady=5, bg="#FFE8C8")
        activity_frame.pack(pady=5, fill="x")

        activity_label = tk.Label(activity_frame, text=activity, font=("Times New Roman", 14), bg="#FFE8C8")
        activity_label.pack(anchor="w")
