import pygame, Implementation.Level


def main():
    pygame.init()
    level = Implementation.Level.Level("/home/kirill/Рабочий стол/Game/Levels/Level_test")
    timer = pygame.time.Clock()
    #TODO: MENU
    mainLoop = True
    while mainLoop:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            level.event(event)

        level.draw()
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()