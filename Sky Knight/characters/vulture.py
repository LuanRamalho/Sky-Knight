import math

from pygame import Rect, transform

from characters.character import Character
from characters.knight import Knight


class Vulture(Character):
    __score = 0

    def __init__(self, x, y, idle, walk, attack, death, knight: Knight):
        super().__init__(x, y, idle, walk, attack, death)
        self.rect: Rect = self.image.get_rect(midbottom=(x, y)).inflate(0, -20)
        self.going_right = True if x < 0 else False
        self.knight = knight
        self.start_dying = False

    @property
    def get_score(self):
        return Vulture.__score

    @classmethod
    def reset_score(cls):
        cls.__score = 0

    def move(self):
        player_x, player_y = self.knight.coordinates

        dx = player_x - self.rect.x
        dy = player_y - self.rect.y

        if self.rect.x < player_x:
            self.rect.x += 2
            self.going_right = False
        elif self.rect.x > player_x:
            self.rect.x -= 2
            self.going_right = True

        if abs(dx) <= 600:
            if abs(dy) > 3:
                if self.rect.y < player_y:
                    self.rect.y += 2
                elif self.rect.y > player_y:
                    self.rect.y -= 2

                angle = math.atan2(dy, dx) if not self.going_right else math.atan2(dy, dx) + 160

                self.image = transform.rotate(self.image, math.degrees(-angle))

    def animate_movement(self):
        self.image, self.walk_index = self.animation(self.going_right, self.walk_images, self.walk_index)

    def after_collision(self):
        if not self.start_dying:
            if not self.knight.attacking:
                self.knight.hurt()
                self.kill()
            else:
                if len({self.going_right, self.knight.going_right}) == 1:
                    Vulture.__score += 1
                    self.die()

    def die(self):
        self.image, self.hurt_index = self.animation(self.going_right, self.death_images, self.hurt_index)
        self.start_dying = True

    def update(self):
        if self.start_dying:
            self.image, self.hurt_index = self.animation(self.going_right, self.death_images, self.hurt_index, 0.05)
            if self.hurt_index + 0.05 >= len(self.death_images):
                self.kill()
        else:
            self.animate_movement()
            self.move()
