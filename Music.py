import tkinter as tkr

from music_app.gui import MusicPlayerGUI


def main() -> None:
    root = tkr.Tk()
    gui = MusicPlayerGUI(root)

    if not gui.load_directory():
        root.destroy()
        return

    root.mainloop()


if __name__ == "__main__":
    main()
