import os
from typing import List

SUPPORTED_EXTENSIONS = (".mp3", ".wav", ".ogg", ".flac")


def list_audio_files(directory: str) -> List[str]:
    """Return the audio files directly inside `directory`, sorted by name."""
    entries = [
        entry
        for entry in os.listdir(directory)
        if entry.lower().endswith(SUPPORTED_EXTENSIONS)
        and os.path.isfile(os.path.join(directory, entry))
    ]
    return sorted(entries, key=str.lower)
