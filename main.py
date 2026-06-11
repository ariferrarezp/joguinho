import pygame

print('setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('setup End')

print('loop start')

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            quit()

