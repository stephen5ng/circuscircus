#!/usr/bin/env python

import pygame
import pygame.freetype


SCALING_FACTOR = 6
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 32

pygame.init()
pygame.freetype.init()

pygame.font.get_init()

display_surface = pygame.display.set_mode(
   (SCREEN_WIDTH*SCALING_FACTOR, SCREEN_HEIGHT*SCALING_FACTOR))

pygame.display.set_caption('Circus Circus')

font2 = pygame.font.SysFont('COURIER', 15)
guess = ""
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text2 = font2.render(alphabet, True, (0, 255, 0))
textRect2 = text2.get_rect()

screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
   screen.fill((0, 0, 0))

   screen.blit(text2, textRect2)

   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         key = pygame.key.name(event.key).upper()
         print(f"{event.key} {pygame.key.name(event.key)} {pygame.K_ESCAPE}")
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
               text2 = font2.render(alphabet, True, (255, 255, 255))

      if event.type == pygame.QUIT:
         pygame.quit()
         quit()

      pygame.transform.scale(screen,
          display_surface.get_rect().size, dest_surface=display_surface)
      pygame.display.update()