import pygame
import characters, game

#in pixels
SCREEN_TITLE = 'RPG'
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

#colors use RGB
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (0, 255, 0)
#clock used to update events
clock = pygame.time.Clock()

class Game:
    TICK_RATE = 60 #equivalent to FPS

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        #creates pygame window with SCREEN_WIDTH and SCREEN_HEIGHT
        self.game_screen = pygame.display.set_mode((width, height))
        #fills background with GREEN_COLOR values
        self.game_screen.fill(GREEN_COLOR)
        #sets window SCREEN_TITLE
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False

        player_character = characters.player(game.player_name, 10, game.weapon_equipped_dmg, 5, 500, 500, 'player.png')
        while not is_game_over:
            #loop to grab all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #if event captured is a quit type event, then exit game loop
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player_character.y_direction = 1
                    elif event.key == pygame.K_a:
                        player_character.x_direction = 1
                    elif event.key == pygame.K_s:
                        player_character.y_direction = -1
                    elif event.key == pygame.K_d:
                        player_character.x_direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_w or event.key == pygame.K_s:
                        player_character.y_direction = 0
                        player_character.x_direction = 0


                print(event)
                print(player_character.x_direction)
                print(player_character.y_direction)

            self.game_screen.fill(GREEN_COLOR)
            player_character.move(player_character.y_pos, player_character.x_pos)
            player_character.draw(self.game_screen)

            pygame.display.update()
            # ticks clock to update the game
            clock.tick(self.TICK_RATE)

pygame.init() #initializes pygame

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

#player_image = pygame.image.load('player.png')
#player_image = pygame.transform.scale(player_image, (50, 50)) #resizes image to 50,50

#gameloop, runs until is_game_over = true

#quit pygame and program
pygame.quit()
quit()
