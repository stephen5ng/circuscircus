#!/usr/bin/env python

import pygame
from pygame import Color
import pygame.freetype
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
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

shifted = {
   "1": "!",
   "/": "?",
   "-": "_",
   "=": "+"
}
while True:
   screen.fill((0, 0, 0))

   font_guess.render_to(screen, (0, 0), guess[:16], Color("green"), Color("black"))
   font_guess.render_to(screen, (0, 11), guess[16:], Color("green"), Color("black"))
   font_small.render_to(screen, (0, 23), alphabet[:8], Color("red"), Color("black"))
   font_small.render_to(screen, (40, 23), alphabet[8:], Color("red"), Color("black"))

   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         key = pygame.key.name(event.key).upper()
         print(f"{key} {event.key} {pygame.key.name(event.key)} {pygame.K_ESCAPE}")
         if event.key == pygame.K_ESCAPE:
            guess = ""
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            text2 = font2.render(alphabet, True, (0, 128, 0))
         if event.key == pygame.K_SPACE:
            key = ' '
         if len(key) == 1:
            if key in alphabet:
               guess += key
               alphabet = alphabet.replace(key, ' ')
            else:
               shift_bits = pygame.KMOD_LSHIFT | pygame.KMOD_RSHIFT
               if pygame.key.get_mods() & shift_bits and key in shifted.keys():
                  guess += shifted[key]
               else:
                  guess += key

      if event.type == pygame.QUIT:
         pygame.quit()
         quit()

      pygame.transform.scale(screen,
          display_surface.get_rect().size, dest_surface=display_surface)
      pygame.display.update()
      hub75.update(screen)