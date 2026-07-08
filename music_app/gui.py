import os
import tkinter as tkr
from tkinter.filedialog import askdirectory

from music_app.library import list_audio_files
from music_app.player import PlaybackController


class MusicPlayerGUI:
    def __init__(self, root: tkr.Tk) -> None:
        self.root = root
        self.root.title("Life In Music")
        self.root.geometry("450x350")

        self.player = PlaybackController()
        self.now_playing = tkr.StringVar()

        self.play_list = tkr.Listbox(
            root, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE
        )

        song_title = tkr.Label(root, font="Helvetica 12 bold", textvariable=self.now_playing)
        song_title.pack()

        tkr.Button(
            root, width=5, height=3, font="Helvetica 12 bold", text="PLAY",
            command=self.play, bg="blue", fg="white",
        ).pack(fill="x")
        tkr.Button(
            root, width=5, height=3, font="Helvetica 12 bold", text="STOP",
            command=self.stop, bg="red", fg="white",
        ).pack(fill="x")
        tkr.Button(
            root, width=5, height=3, font="Helvetica 12 bold", text="PAUSE",
            command=self.pause, bg="purple", fg="white",
        ).pack(fill="x")
        tkr.Button(
            root, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE",
            command=self.unpause, bg="orange", fg="white",
        ).pack(fill="x")

        self.play_list.pack(fill="both", expand="yes")

    def load_directory(self) -> bool:
        """Prompt for a folder and populate the playlist. Returns False if canceled."""
        directory = askdirectory()
        if not directory:
            return False

        os.chdir(directory)
        for song in list_audio_files(directory):
            self.play_list.insert(tkr.END, song)
        return True

    def play(self) -> None:
        selection = self.play_list.curselection()
        if not selection:
            return
        track = self.play_list.get(selection[0])
        self.player.play(track)
        self.now_playing.set(track)

    def stop(self) -> None:
        self.player.stop()

    def pause(self) -> None:
        self.player.pause()

    def unpause(self) -> None:
        self.player.unpause()
