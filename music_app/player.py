import pygame


class PlaybackController:
    """Thin wrapper around pygame.mixer for a single-track player."""

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()

    def play(self, filepath: str) -> None:
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()

    def stop(self) -> None:
        pygame.mixer.music.stop()

    def pause(self) -> None:
        pygame.mixer.music.pause()

    def unpause(self) -> None:
        pygame.mixer.music.unpause()
