from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil
import tkinter.messagebox
import threading


def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_mp4_mp3(video_url, file_path):
    mp4 = YouTube(video_url).streams.get_highest_resolution().download()
    # convert it into video file
    video_clip = VideoFileClip(mp4)
    # code for mp3
    audio_file = video_clip.audio
    file_name, _ext = os.path.splitext(os.path.basename(mp4))
    file_name = file_name + '-audio.mp3'
    audio_file.write_audiofile(file_name)
    audio_file.close()
    shutil.move(file_name, file_path)
    # code for mp3
    video_clip.close()
    shutil.move(mp4, file_path)
    tkinter.messagebox.showinfo("Success", "Download Completed")


def is_path_valid(path):
    return os.path.exists(path)


def download(video_url, file_path):
    if not is_path_valid(file_path):
        file_path = "C:\\Users\\habiba.ahmed\\Desktop"

    # download the highest resolution so the video will have the audio with it
    print("Downloading....")
    thread = threading.Thread(target=download_mp4_mp3(video_url, file_path))
    # Start the thread
    thread.start()
    # Wait for the thread to complete (if needed)
    # thread.join()


root = Tk()
root.title('Video Downloader')
canvas = Canvas(root, width=400, height=300)
canvas.pack()

app_label = Label(root, text="Video Downloader")
canvas.create_window(200, 20, window=app_label)

url_label = Label(root, text="Enter video URL")
url_entry = Entry(root)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

path_label = Label(root, text="select path to download, default desktop")
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 170, window=path_button)

download_button = Button(
    root, text="Download",
    command=lambda: download(url_entry.get(), path_label.cget("text"))
)
canvas.create_window(200, 250, window=download_button)

root.mainloop()
