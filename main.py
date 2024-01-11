
import tkinter
import customtkinter
from pytube import YouTube

def startdownload():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink)
        video = ytobject.streams.get_highest_resolution()
        video.download()
    except:
        print("YouTube link is invalid")
    print("Download Complete!")

# system settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

#Add UI stuff
title = customtkinter.CTkLabel(app, text = "Insert a youtube Link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startdownload)
download.pack(pady=10, padx=10)

# Run App
app.mainloop();
