import pygame

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            from code.game.menu import Menu
            menu = Menu(self.window)
            menu.run()
            pass
            # for event in pygame.event.get():
               # if event.type == pygame.QUIT:
                #    pygame.quit()
                 #   quit()

