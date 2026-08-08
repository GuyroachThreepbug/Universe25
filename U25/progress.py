"""
a class that renders text as a progress bar. after creating of the
instance of the class by passing the font, message, color, and bgcolor.
you call the "render" method, and pass it a percentage from 0 to 100.

note that the uncompleted section of the text is drawn with the bgcolor,
the rest of the text is done using the given color, and highlights when
finished (progress >= 100)
"""
import os, sys, pygame, pygame.font, pygame.image
from pygame.locals import *

"""
TextProgress: a progress meter where the *text itself* fills in with color
as the percentage rises, instead of a separate bar.

Modernized for Python 3 / current pygame conventions from an older snippet.
"""

import pygame
from pygame.locals import Rect


class TextProgress:
    def __init__(self, font, message, color, bgcolor):
        self.font = font
        self.message = message
        self.color = color
        self.bgcolor = bgcolor

        # Derived colors: a dimmed version of `color`, and its inverse
        # (used as a throwaway "impossible" color for colorkey tricks).
        self.offcolor = tuple(c ^ 40 for c in color)
        self.notcolor = tuple(c ^ 0xFF for c in color)

        # Base filled-in text render (color doesn't matter here, it gets
        # replaced by colorkey logic below).
        self.text = font.render(message, True, (255, 0, 0), self.notcolor)
        self.text.set_colorkey(self.notcolor)

        # Outlined ("empty") version of the text.
        self.outline = self._text_hollow(font, message, color)

        # The "fill" surface: a dim background with a bright stripe through
        # the middle, sized to match the text.
        self.bar = pygame.Surface(self.text.get_size())
        self.bar.fill(self.offcolor)
        width, height = self.text.get_size()
        stripe = Rect(0, height // 2, width, height // 4)
        self.bar.fill(color, stripe)

        # Pixels-per-percent, so render() can convert 0-100 into a width.
        self.ratio = width / 100.0

    def _text_hollow(self, font, message, fontcolor):
        """Render `message` as a hollow/outlined version in `fontcolor`."""
        base = font.render(message, True, fontcolor, self.notcolor)
        size = base.get_width() + 2, base.get_height() + 2

        img = pygame.Surface(size)
        img.fill(self.notcolor)

        # Offset-blit the same text a few times to fake an outline.
        base.set_colorkey(self.notcolor)
        for offset in [(0, 0), (2, 0), (0, 2), (2, 2)]:
            img.blit(base, offset)

        # Blit the "true" text once more in the center, on top.
        img.blit(base, (1, 1))

        img.set_colorkey(self.notcolor)
        return img

    def render(self, percent=50):
        """Return a Surface showing the meter at `percent` (0-100) full."""
        percent = max(0, min(100, percent))
        surf = pygame.Surface(self.text.get_size())

        if percent < 100:
            surf.fill(self.bgcolor)
            fill_width = int(percent * self.ratio)
            fill_height = self.bar.get_height()
            surf.blit(self.bar, (0, 0), (0, 0, fill_width, fill_height))
        else:
            surf.fill(self.color)
            surf.blit(self.text, (0, 0))

        surf.blit(self.outline, (-1, -1))
        surf.set_colorkey(self.notcolor)
        return surf


# --- Demo -------------------------------------------------------------

if __name__ == "__main__":
    pygame.init()

    entry_info = "FRUSTRATION"  # the word that will "fill in"
    bigfont = pygame.font.Font(None, 60)
    white = (255, 255, 255)

    renderer = TextProgress(bigfont, entry_info, white, (40, 40, 40))

    win = pygame.display.set_mode((600, 100))
    clock = pygame.time.Clock()

    percent = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Slowly fill up for demo purposes, looping back to 0.
        percent = (percent + 1) % 101

        text = renderer.render(percent)
        win.fill((50, 100, 50))
        win.blit(text, (0, 0))
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()