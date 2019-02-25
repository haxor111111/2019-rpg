class Item:
  def __init__(self, name, width, height, x_pos, y_pos, image_path)
		object_image = pygame.image.load(image_path)
		self.image = pygame.transform.scale(object_image, (width, height))
		self.name = name
		self.width = width
		self.height = height
		self.x_pos = x_pos
		self.y_pos = y_pos
		
	def draw(self, background):
    background.blit(self.image, (self.x_pos, self.y_pos))

class Weapon(Item):
	def __init__(self, name, damage, width, height, x_pos, y_pos, image_path)
		self.damage = damage
		super().__init__(name, width, height, x_pos, y_pos, image_path)
		
class HItem(Item):
	def __init__(self, name, hp, width, height, x_pos, y_pos, image_path)
		self.hp = hp
		super().__init__(name, width, height, x_pos, y_pos, image_path)
	
	def heal(self, hp):
		player_character.hp += self.hp
