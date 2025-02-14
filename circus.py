#!/usr/bin/env python

import aiomqtt
import my_inputs
import platform
import pygame
from pygame import Color
import pygame.freetype
import sys
import hub75

SCALING_FACTOR = 9
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 32

# grab keyboard before pygame
if platform.system() != "Darwin":
    my_inputs.get_key()

pygame.init()
hub75.init()

pygame.freetype.init()

display_surface = pygame.display.set_mode(
    (SCREEN_WIDTH*SCALING_FACTOR, SCREEN_HEIGHT*SCALING_FACTOR))

pygame.display.set_caption('Circus Circus')

font_guess = pygame.freetype.Font("raize-13.pcf", 13)
font_small = pygame.freetype.Font("scientifica-11.bdf", 11)
guess = ""

screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

shifted = {
    "1": "!",
    "/": "?",
    "-": "_",
    "=": "+"
}
is_shifted = False
def get_key():
    global is_shifted
    if platform.system() != "Darwin":
        events = my_inputs.get_key()
        if not events:
            return
        for event in events:
            if event.ev_type == "Key":
                key = event.code[4:]
                if key == "SLASH":
                    key = "/"
                if "SHIFT" in key:
                    is_shifted = False if event.state == 0 else True
                elif event.state:
                    if len(key) == 1:
                        if key.isalpha():
                            yield key
                        elif is_shifted and key in shifted.keys():
                            yield shifted[key]
                    elif key == "DOT":
                        yield "."
                    elif key == "COMMA":
                        yield ","
                    elif key == "SPACE":
                        yield " "
                    else:
                        yield key
        return

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key).upper()
            if len(key) == 1:
                if key.isalpha():
                    yield key
                    continue
                is_shifted = pygame.key.get_mods() & (pygame.KMOD_LSHIFT | pygame.KMOD_RSHIFT)
                if not is_shifted and key.isnumeric():
                    continue
                if key in shifted.keys():
                    yield shifted[key]
                    continue
                if key == ".":
                    yield key
            else:
                yield key
        elif event.type == pygame.QUIT:
             pygame.quit()
             sys.exit(0)

while True:
    screen.fill((0, 0, 0))
    show_cursor = (pygame.time.get_ticks()*2 // 1000) % 2 == 0
    print_guess = guess + ("_" if show_cursor else " ")
    first_y = 0 if guess else 10
    # for some weird reason font.render skips the first empty space
    letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in guess:
        letters = letters.replace(x, ' ')
        # print(f"removing {x} '{letters}'")
    font_guess.render_to(screen, (0, first_y), print_guess[:16], Color("green"), Color("black"))
    font_guess.render_to(screen, (0, 10), print_guess[16:], Color("green"), Color("black"))
    font_small.render_to(screen, (-1, 21), letters[:9], Color("red"), Color("black"))
    font_small.render_to(screen, (40, 21), letters[9:], Color("red"), Color("black"))

    for key in get_key():
        if key == "ESCAPE":
            guess = ""
        elif key == "BACKSPACE":
            guess = guess[:-1]
        elif key == "SPACE":
            guess += ' '
        elif len(key) == 1:
            if not key.isalpha() or key not in guess:
               guess += key

    hub75.update(screen)
    pygame.transform.scale(screen,
    display_surface.get_rect().size, dest_surface=display_surface)
    pygame.display.update()


