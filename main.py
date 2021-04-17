import pygame
from game import Game
import math

pygame.init()

# generate first window
pygame.display.set_caption("Tree  Game ")
infoObject = pygame.display.Info()
print((infoObject.current_w, infoObject.current_h))

screen = pygame.display.set_mode((1080, 720))
print(screen.get_width())
# load the game
game = Game()

# load bg.jpg as background
background = pygame.image.load("assets/bg.jpg")

# load our banner
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

# load the button to launch the game
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)+100

running = True

while running:
    # apply the background
    screen.blit(background, (0, -200))

    # check if our game has started
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(banner, banner_rect)
        screen.blit(play_button,play_button_rect)

    # update the screen
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("end of pygame")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
