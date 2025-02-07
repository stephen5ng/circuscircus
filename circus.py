#!/usr/bin/env python

import aiomqtt
import pygame
from pygame import Color
import pygame.freetype
import sys
import hub75

SCALING_FACTOR = 6
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 32

pygame.init()
hub75.init()

pygame.freetype.init()

display_surface = pygame.display.set_mode(
   (SCREEN_WIDTH*SCALING_FACTOR, SCREEN_HEIGHT*SCALING_FACTOR))

pygame.display.set_caption('Circus Circus')

font_guess = pygame.freetype.Font("bitmap-fonts/bitmap/raize/raize-13.pcf", 13)
font_small = pygame.freetype.Font("bitmap-fonts/bitmap/scientifica/scientifica-11.bdf", 11)
guess = ""

screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

shifted = {
   "1": "!",
   "/": "?",
   "-": "_",
   "=": "+"
}
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
   font_guess.render_to(screen, (0, 11), print_guess[16:], Color("green"), Color("black"))
   font_small.render_to(screen, (-1, 23), letters[:9], Color("red"), Color("black"))
   font_small.render_to(screen, (40, 23), letters[9:], Color("red"), Color("black"))

   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         key = pygame.key.name(event.key).upper()
         # print(f"{key} {event.key} {pygame.key.name(event.key)} {pygame.K_ESCAPE}")
         if event.key == pygame.K_ESCAPE:
            guess = ""
         if event.key == pygame.K_BACKSPACE:
            guess = guess[:-1]
         if event.key == pygame.K_SPACE:
            key = ' '
         if len(key) == 1:
            is_shifted = pygame.key.get_mods() & (pygame.KMOD_LSHIFT | pygame.KMOD_RSHIFT)
            if key.isalpha():
               if key not in guess:
                  guess += key
            elif not is_shifted and key.isnumeric():
               pass
            else:
               if pygame.key.get_mods() & is_shifted and key in shifted.keys():
                  guess += shifted[key]
               # else:
               #    guess += key

      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit(0)

   hub75.update(screen)
   pygame.transform.scale(screen,
   display_surface.get_rect().size, dest_surface=display_surface)
   pygame.display.update()
