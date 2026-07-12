# Life In Music

A minimal desktop music player built with Python: [Tkinter](https://docs.python.org/3/library/tkinter.html) drives the GUI, and [pygame](https://www.pygame.org/)'s `pygame.mixer` handles audio playback.

## Features

- Pick any folder on your machine and load its supported audio files into a playlist, sorted by name
- Play, pause, unpause, and stop the selected track
- Small, easy-to-read codebase split into focused modules (see [Project structure](#project-structure))
- Packaged as a standalone Windows executable via PyInstaller

## Known limitations

This is intentionally a minimal player, not a full-featured one:

- **Single track at a time** — there's no queue or playback position tracking beyond the currently loaded track.
- **No auto-advance** — playback does not move to the next track when one finishes; you select and press PLAY again.
- **No shuffle or repeat** modes.
- **Single selection only** — the playlist uses `tkinter.Listbox` in `SINGLE` select mode, so `PLAY` no-ops if nothing is selected.
- **One folder per session** — the working directory is chosen once at launch (via `askdirectory`) and the app `os.chdir`s into it; canceling the picker exits the app rather than crashing. There's no in-app way to switch folders without restarting.
- **Top-level files only** — `list_audio_files` scans the chosen directory itself, not subfolders.

## Requirements

- Python 3
- [pygame](https://www.pygame.org/)

Tkinter ships with the standard CPython installer on Windows, so no separate install is needed for it.

## Installation

```bash
git clone https://github.com/<your-username>/Music-Application.git
cd Music-Application
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python Music.py
```

On launch, a folder picker will open — select the directory containing your audio files. Supported files (`.mp3`, `.wav`, `.ogg`, `.flac`) in that folder are loaded into the playlist, sorted by name. Select a track and use the on-screen controls:

| Button    | Action                        |
|-----------|--------------------------------|
| PLAY      | Loads and plays the selected track |
| STOP      | Stops playback                |
| PAUSE     | Pauses the current track      |
| UNPAUSE   | Resumes a paused track        |

## Project structure

```
Music.py           # entry point
music_app/
  library.py        # pure directory-scanning/filtering logic
  player.py          # pygame.mixer wrapper
  gui.py              # Tkinter widgets and wiring
tests/
  test_library.py    # unit tests for music_app/library.py
```

### How it fits together

- **`Music.py`** is a thin entry point: it creates the Tk root, builds `MusicPlayerGUI`, prompts for a directory via `load_directory()`, and starts the mainloop. If the user cancels the folder picker, `load_directory()` returns `False` and the app exits cleanly instead of starting with an empty playlist.
- **`music_app/library.py`** exposes one pure function, `list_audio_files(directory)`, which filters a directory down to files ending in `.mp3`, `.wav`, `.ogg`, or `.flac` and returns them sorted case-insensitively by name. It has no Tkinter or pygame dependency, which is why it's the only part covered by unit tests.
- **`music_app/player.py`** defines `PlaybackController`, a thin wrapper around `pygame.mixer` exposing `play(filepath)`, `stop()`, `pause()`, and `unpause()`. It initializes `pygame` and `pygame.mixer` on construction.
- **`music_app/gui.py`** defines `MusicPlayerGUI`, which builds the Tkinter widgets (playlist `Listbox`, now-playing `Label`, and PLAY/STOP/PAUSE/UNPAUSE buttons) and wires each button to a `PlaybackController` instance. The currently playing track name is surfaced through a Tkinter `StringVar` (`now_playing`) bound to the label — there is no other playback state tracked.

## Running tests

```bash
python -m unittest discover -s tests -v
```

## Building a standalone executable

The project includes a [PyInstaller](https://pyinstaller.org/) spec file, `Music.spec`, which bundles the app with its icon (`favicon.ico`) into a single `.exe`:

```bash
pip install pyinstaller
pyinstaller Music.spec
```

The built executable is output to `dist/Music.exe`.

## License

Distributed under the [MIT License](LICENSE).
