import sys
import math
import pygame
from pygame.locals import *

from gamelib.util import *
from gamelib.gfxlib import *
from gamelib.gfxgame import *
from gamelib.gfxstore import *
from gamelib.aftermathgame import *

# Globals.
ScreenSize = [800, 600]
Debug = False
GameName = "THE AFTERMATH"

# Standard Init.
# pygame.mixer.init()
# pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption(GameName)

pygame.time.set_timer(ANIMEVENT, 30)
pygame.time.set_timer(LOGICEVENT, 30)

surface = CreateBackground(screen)
clear(surface)
Game = None
GFX = GFXStore()

# ------
# MAIN
# ------
def main():
    GameState = 1
    DrawText(surface, 10, 50, "Daftspaniel Presents...", 48, (255, 255, 255))
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    while GameState != -1:

        if GameState == 1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == ANIMEVENT:

                    DrawText(surface, 210, 250, GameName, 78, (255, 0, 0))
                    DrawText(surface, 211, 251, GameName, 78, (255, 156, 0))
                    DrawText(surface, 212, 252, GameName, 78, (255, 255, 255))

                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_SPACE]:
                        GameState = 3
                    if keystate[K_ESCAPE] == 1:
                        GameState = -1

            screen.blit(surface, (0, 0))
            pygame.display.flip()

        elif GameState == 3:

            clear(surface)
            pygame.display.flip()

            AGame = AftermathGame( surface, screen, (800,600), GFX)

            while GameState == 3:
                print("Game on")
                AGame.main_loop()
                GameState = 4

        elif GameState == 4:  # Game over!

            print("Game over")
            clear(surface)

            while GameState == 4:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        keystate = pygame.key.get_pressed()
                        if keystate[K_SPACE]:
                            GameState = 1
                            clear(surface)
                            pygame.time.wait(1000)
                    elif event.type == ANIMEVENT:
                        DrawText(surface, 210, 250, "Game Over", 78, (255, 0, 0))
                        DrawText(surface, 211, 251, "Game Over", 78, (255, 156, 0))
                        DrawText(surface, 212, 252, "Game Over", 78, (255, 255, 255))
                        screen.blit(surface, (0, 0))
                        pygame.display.flip()

        elif GameState == 5:  # Game Win

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == ANIMEVENT:
                    clear(surface)
                    DrawText(surface, 10, 50, "Well Done!", 48, (255, 0, 0))

                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_SPACE]:
                        GameState = 1
                        clear(surface)

            screen.blit(GameBG, (0, 0))
            pygame.display.flip()
