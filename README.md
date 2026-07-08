# Life In Music

A simple desktop music player built with Python, [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI, and [pygame](https://www.pygame.org/) for audio playback.

## Features

- Pick any folder on your machine and load its contents into a playlist
- Play, pause, unpause, and stop the selected track
- Lightweight, single-file implementation
- Packaged as a standalone Windows executable via PyInstaller

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
