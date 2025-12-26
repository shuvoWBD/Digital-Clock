import tkinter as tk
from time import strftime

# ===== Main Window =====
root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x300")
root.configure(bg="#1a1a2e")  # dark gradient-like background

# ===== Labels =====
time_label = tk.Label(root, font=("Helvetica", 60, "bold"), bg="#1a1a2e", fg="#00FF00")
time_label.pack(pady=(30, 10))

date_label = tk.Label(root, font=("Helvetica", 24), bg="#1a1a2e", fg="#ADD8E6")
date_label.pack(pady=(0, 20))

# ===== Update function =====
def update_display():
    current_time = strftime('%I:%M:%S %p')          # 12-hour format
    current_date = strftime('%A, %d %B %Y')         # Day, date, month, year
    
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    # update every second
    root.after(1000, update_display)

# Start
update_display()
root.mainloop()