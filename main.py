import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#000000"

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    back_ground = pygame.Surface(DISPLAY)

    #TODO: MENU
    mainLoop = True
    while mainLoop :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                mainLoop = False

        screen.blit(back_ground, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()