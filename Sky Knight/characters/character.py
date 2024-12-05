from pygame import sprite, transform, Rect


class Character(sprite.Sprite):

    def __init__(self, x: int, y: int, idle_images: list, walk_images: list, attack_images: list, death_images: list):
        super().__init__()
        self.image = idle_images[0]
        self.x = x
        self.y = y
        self.idle_images = idle_images
        self.walk_images = walk_images
        self.attack_images = attack_images
        self.death_images = death_images
        self.idle_index = 0
        self.walk_index = 0
        self.attack_index = 0
        self.hurt_index = 0

    @staticmethod
    def animation(direction, images, index, speed=0.1):
        index += speed
        if index > len(images):
            index = 0

        if direction:
            return images[int(index)], index

        return transform.flip(images[int(index)], True, False), index
