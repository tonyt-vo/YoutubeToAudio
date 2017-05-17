from __future__ import unicode_literals
import youtube_dl, os
from tkinter import *
from tkinter import filedialog, messagebox

class YouTubeMP3(Tk):

    def __init__(self):
        Tk.__init__(self)

        # GUI options.
        self.geometry("600x90")
        self.minsize(600,90)
        self.maxsize(600,90)

        # Default Options for downloading.
        self.options = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
        }
        # Music Path Label, Entry and Label to store location on disk.
        self.label = Label(self, text="Music Path").grid(row=0, column=0) # Label for music path
        self.music_path = StringVar()
        self.music_path_entry = Entry(self, textvariable=self.music_path ,width=75).grid(row=0,column=1)

        # Browse button to open file explore to choose a path.
        self.browse_button = Button(self, text="Browse", command=self.update_directory)
        self.browse_button.grid(row=0,column=3, sticky=W)

        # Playlist option for downloading playlist.
        self.playlist_option = False
        self.check_button = Checkbutton(text="Playlist", command=self.update_playlist_option)
        self.check_button.grid(row=2, column=1)

        # URL information of YouTube playlist or video.
        self.label = Label(self, text="URL").grid(row=1, column=0, sticky=E)
        self.url = StringVar()
        self.url = "URL of playlist or song"
        self.url_entry =  Entry(self, textvariable=self.url, width=75)
        self.url_entry.grid(row=1,column=1)

        # Download Button
        self.download_button = Button(self, text="Download", command=self.download)
        self.download_button.grid(row=1, column=3, sticky=W)

    # Updates the directory with a new path.
    def update_directory(self):
        path = filedialog.askdirectory()
        self.music_path.set(path)

    # Change the playlist option based on state of check button.
    def update_playlist_option(self):
        self.playlist_option = not self.playlist_option

    # Update the music path entry
    def update_entry(self, new_path):
        self.music_path_entry['text'] = new_path

    # Use this method as an intermediate to call other.
    def download(self):
        updated_path = self.music_path.get()
        self.download_song(self.url_entry.get(),self.playlist_option,updated_path)

    # Download Song given a url, playlist option and a path to music directory.
    def download_song(self,url, playlist, music_path):
        self.options['noplaylist'] = not playlist
        self.options['outtmpl'] = music_path + '\%(title)s' + ".mp3"
        if playlist:
            messagebox.showinfo("Playlist Option", "Depending on the size of the playlist, "
                                                   "this may take a moment. Please wait and do not exit.")
        with youtube_dl.YoutubeDL(self.options) as ydl:
            try: # Try to download
                ydl.download([url])
                notify_user = messagebox.askyesno("Download Complete", "Would you like to open music folder?")
                if notify_user:
                    os.system('start ' + music_path)
            except: # If anything happens, notify user and ensure all fields are filled correctly.
                messagebox.showinfo("Error", "Please try again and ensure all fields are filled correctly.")

# Run the application.
if __name__ == "__main__":
    app = YouTubeMP3()
    app.mainloop()
