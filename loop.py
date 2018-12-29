import pygame


class Loop:
    def loop(win, controller, sprites, condition=True):
        run = True

        while condition and run:
            pygame.time.delay(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            win.fill((0, 0, 0))

            controller.update()

            sprites.update()
            sprites.draw(win)

            pygame.display.update()