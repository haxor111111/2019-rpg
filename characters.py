import game, pygame
class GameObject:

    def __init__(self, name, hp, damage, speed, inventory, width, height, x_pos, y_pos, image_path):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        self.name = name
        self.hp = hp
        self.speed = speed
        self.inventory = inventory
        self.damage = damage
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height


    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class player(GameObject):
    y_direction = 0
    x_direction = 0
    def __init__(self, name, hp, damage, speed, x_pos, y_pos, image_path):
        super().__init__(name, hp, damage, speed, [], 100, 100, x_pos, y_pos, image_path)

    def add(self, item):
        self.inventory.append(item)

    def move(self, y_direction, x_direction):

        if self.y_direction > 0:
            self.y_pos -= self.speed
        elif self.y_direction < 0:
            self.y_pos += self.speed
        if self.x_direction > 0:
            self.x_pos -= self.speed
        elif self.x_direction < 0:
            self.x_pos += self.speed


#spoder = player('spoder', 10, '5', 5, 1, 1, 'spoder.png')


#player_character.add(game.weapon_equipped)
#spoder.add('fangs')

#player_character.inventory = spoder.inventory + player_character.inventory
