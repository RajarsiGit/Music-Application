import os
import tempfile
import unittest

from music_app.library import list_audio_files


class ListAudioFilesTests(unittest.TestCase):
    def test_filters_to_supported_extensions_and_sorts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            for name in ("b.mp3", "a.wav", "notes.txt", "cover.jpg", "c.flac"):
                open(os.path.join(tmp_dir, name), "w").close()

            self.assertEqual(
                list_audio_files(tmp_dir), ["a.wav", "b.mp3", "c.flac"]
            )

    def test_ignores_subdirectories(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.mkdir(os.path.join(tmp_dir, "nested.mp3"))
            open(os.path.join(tmp_dir, "track.mp3"), "w").close()

            self.assertEqual(list_audio_files(tmp_dir), ["track.mp3"])

    def test_empty_directory_returns_empty_list(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.assertEqual(list_audio_files(tmp_dir), [])


if __name__ == "__main__":
    unittest.main()
