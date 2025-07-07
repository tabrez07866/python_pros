import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please paste a YouTube URL.")
        return

    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Video downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video:\n{e}")

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader (yt-dlp)")
root.geometry("500x200")

title = tk.Label(root, text="🎬 YouTube Downloader", font=("Arial", 16, "bold"))
title.pack(pady=10)

url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.pack()

url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

download_btn = tk.Button(root, text="Download", command=download_video, bg="green", fg="white", font=("Arial", 12))
download_btn.pack(pady=10)

root.mainloop()
