import pygame

pygame.font.init()

pygame.font.get_init()

display_surface = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Circus Circus')

font1 = pygame.font.SysFont('COURIER', 50)
font2 = pygame.font.SysFont('COURIER', 40)
guess = ""
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text1 = font1.render(guess, True, (0, 255, 0))
text2 = font2.render(alphabet, True, (0, 255, 0))

textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect1.center = (320, 250)
textRect2.center = (320, 300)

while True:
   display_surface.fill((0, 0, 0))

   # copying the text surface objects
   # to the display surface objects
   # at the center coordinate.
   display_surface.blit(text1, textRect1)
   textRect1.center = (320, 200)
   display_surface.blit(text2, textRect2)

   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         key = pygame.key.name(event.key).upper()
         print(f"{event.key} {pygame.key.name(event.key)} {pygame.K_ESCAPE}")
         if event.key == pygame.K_ESCAPE:
            guess = ""
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            text1 = font1.render(guess, True, (0, 255, 0))
            text2 = font2.render(alphabet, True, (0, 255, 0))
            textRect1 = text1.get_rect()
         if event.key == pygame.K_SPACE:
            key = ' '
         if len(key) == 1:
            if key in alphabet:
               guess += key
               alphabet = alphabet.replace(key, ' ')
               text1 = font1.render(guess, True, (0, 255, 0))
               text2 = font2.render(alphabet, True, (0, 255, 0))
               textRect1 = text1.get_rect()

      if event.type == pygame.QUIT:
         pygame.quit()
         quit()

      pygame.display.update()