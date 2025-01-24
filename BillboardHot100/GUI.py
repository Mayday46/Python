import tkinter as tk
from tkinter import messagebox
from BillboardScraper import BillboardScraper
from BillboardToSpotify import BillboardToSpotify
from SpotifyPlaylistCreator import SpotifyPlaylistCreator
from key import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET  # Import Spotify credentials


def validate_date(date):
    # Ensure the date is in the format YYYY-MM-DD
    parts = date.split("-")
    if len(parts) != 3:
        messagebox.showerror("Error", "Date must be in the format YYYY-MM-DD.")
        return False

    year, month, day = parts
    # Check if year, month, and day are all integers
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        messagebox.showerror("Error", "Year, month, and day must be numbers.")
        return False

    # Check valid ranges for year, month, and day
    try:
        year = int(year)
        month = int(month)
        day = int(day)

        if not (1 <= month <= 12):
            raise ValueError("Invalid month.")
        if not (1 <= day <= 31):  # Simple range, does not handle month-specific limits
            raise ValueError("Invalid day.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return False

    return True


def create_playlist_from_gui():
    date = date_entry.get()
    
    if not validate_date(date):
        messagebox.showerror("Error", "Please enter a date.")
        return
    
    try:
        scraper = BillboardScraper(date)
        
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# GUI Layout
window = tk.Tk()
window.title("Billboard to Spotify")
window.geometry("400x200")

# Date Label
label = tk.Label(window, text="Enter the date (YYYY-MM-DD):", font = ("Arial", 12))
label.pack(pady = 10)

date_entry = tk.Entry(window, font = ("Arial", 12))
date_entry.pack(pady = 10)

submit_button = tk.Button(window, text = "Create Playlist", font = ("Arial", 12), command = create_playlist_from_gui)
submit_button.pack(pady = 10)


# Run the GUI Application
window.mainloop()

