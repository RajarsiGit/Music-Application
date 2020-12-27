import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

def main():
    music_player = tkr.Tk()
    music_player.title("Life In Music")
    music_player.geometry("450x350")

    play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)

    pygame.init()
    pygame.mixer.init()

    def play():
        pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
        var.set(play_list.get(tkr.ACTIVE))
        pygame.mixer.music.play()
    def stop():
        pygame.mixer.music.stop()
    def pause():
        pygame.mixer.music.pause()
    def unpause():
        pygame.mixer.music.unpause()

    Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
    Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
    Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
    Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

    var = tkr.StringVar() 
    song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

    song_title.pack()
    Button1.pack(fill="x")
    Button2.pack(fill="x")
    Button3.pack(fill="x")
    Button4.pack(fill="x")

    directory = askdirectory()
    os.chdir(directory)
    song_list = os.listdir()

    for item in song_list:
        pos = 0
        play_list.insert(pos, item)
        pos += 1

    play_list.pack(fill="both", expand="yes")
    music_player.mainloop()

if __name__ == "__main__": 
    main()