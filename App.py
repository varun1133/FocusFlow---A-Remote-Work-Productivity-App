import tkinter as tk
from tkinter import messagebox
import time
import threading

class FocusFlowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FocusFlow - Remote Work Productivity App")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.bg_color = "#f0f8ff"  # Soft blue
        self.text_color = "#2c3e50"  # Dark grey
        self.root.configure(bg=self.bg_color)
        
      
        self.timer_running = False
        self.work_duration = 25 * 60  # 25 minutes in seconds
        self.break_duration = 5 * 60  # 5 minutes in seconds
        self.current_timer = None
        self.is_work_time = True
        
        self.create_widgets()

    def create_widgets(self):
       
        self.title_label = tk.Label(
            self.root, text="FocusFlow", font=("Helvetica", 18, "bold"), bg=self.bg_color, fg=self.text_color
        )
        self.title_label.pack(pady=10)
        
        
        self.timer_label = tk.Label(
            self.root, text="25:00", font=("Helvetica", 36), bg=self.bg_color, fg=self.text_color
        )
        self.timer_label.pack(pady=20)
        
       
        self.start_button = tk.Button(
            self.root, text="Start", font=("Helvetica", 14), bg="#2ecc71", fg="white", command=self.start_timer
        )
        self.start_button.pack(pady=10)
       
        self.reset_button = tk.Button(
            self.root, text="Reset", font=("Helvetica", 14), bg="#e74c3c", fg="white", command=self.reset_timer
        )
        self.reset_button.pack(pady=10)
        
       
        self.status_label = tk.Label(
            self.root, text="Ready to focus!", font=("Helvetica", 14), bg=self.bg_color, fg=self.text_color
        )
        self.status_label.pack(pady=20)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_button.configure(state=tk.DISABLED)
            self.run_timer()

    def reset_timer(self):
        self.timer_running = False
        self.start_button.configure(state=tk.NORMAL)
        if self.current_timer:
            self.root.after_cancel(self.current_timer)
        self.timer_label.configure(text="25:00")
        self.status_label.configure(text="Ready to focus!")
        self.is_work_time = True

    def run_timer(self):
        duration = self.work_duration if self.is_work_time else self.break_duration
        self.update_timer(duration)

    def update_timer(self, remaining):
        minutes, seconds = divmod(remaining, 60)
        self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")
        if remaining > 0:
            self.current_timer = self.root.after(1000, self.update_timer, remaining - 1)
        else:
            self.timer_running = False
            self.start_button.configure(state=tk.NORMAL)
            if self.is_work_time:
                self.status_label.configure(text="Time for a break!")
                messagebox.showinfo("Break Time", "Take a 5-minute break!")
            else:
                self.status_label.configure(text="Back to work!")
                messagebox.showinfo("Work Time", "Let's get back to focusing!")
            self.is_work_time = not self.is_work_time
            self.run_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusFlowApp(root)
    root.mainloop()
