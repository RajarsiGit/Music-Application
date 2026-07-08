# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A minimal desktop music player built with Python: a Tkinter GUI drives playback controls, and `pygame.mixer` handles actual audio playback.

## Running

```
python Music.py
```

Requires `pygame` (install via `pip install -r requirements.txt`; Tkinter ships with standard CPython on Windows). On launch the app opens a directory picker (`askdirectory`) — the chosen directory becomes the working directory (`os.chdir`) and its supported audio files (`.mp3`, `.wav`, `.ogg`, `.flac`) are listed in the playlist box. Canceling the picker exits the app instead of crashing.

## Testing

```
python -m unittest discover -s tests -v
```

Only `music_app/library.py` (pure directory-scanning logic) is unit tested — the GUI and playback modules are thin wrappers around Tkinter/pygame and aren't covered.

## Building the Windows executable

The repo is set up for PyInstaller packaging via [Music.spec](Music.spec):

```
pyinstaller Music.spec
```

This produces `dist/Music.exe` (bundling `favicon.ico` as the icon). The `build/` and `dist/` directories are PyInstaller output, not source — don't hand-edit files there.

## Architecture

`Music.py` is a thin entry point: it creates the Tk root, builds `MusicPlayerGUI`, prompts for a directory, and starts the mainloop. The actual implementation lives in the `music_app/` package, split by concern:

- [music_app/library.py](music_app/library.py) — pure function `list_audio_files(directory)` that filters a directory to supported audio extensions and returns them sorted. No Tkinter/pygame dependency, which is why it's the only part with unit tests.
- [music_app/player.py](music_app/player.py) — `PlaybackController`, a thin wrapper around `pygame.mixer` exposing `play`/`stop`/`pause`/`unpause`.
- [music_app/gui.py](music_app/gui.py) — `MusicPlayerGUI`, builds the Tkinter widgets and wires button commands to a `PlaybackController` instance. `load_directory()` handles the folder picker and returns `False` if the user cancels.

Playback state (current track) is surfaced to the UI via a Tkinter `StringVar` (`now_playing`) bound to a label; there is no other state tracking (no queue position, no shuffle/repeat). `play()` uses `Listbox.curselection()` and no-ops if nothing is selected — it does not auto-advance to the next track.
