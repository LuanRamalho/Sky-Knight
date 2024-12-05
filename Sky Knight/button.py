import pygame


class Button:

    def __init__(self, screen, x, y, image, text, font):
        self.image = pygame.transform.scale(image, (int(image.get_width() * 5), int(image.get_height() * 5)))
        self.screen = screen
        self.rect = self.image.get_rect(topleft=(x, y))
        self.text = font.render(text, False, "Black")

    def check_for_pressed(self):
        mouse_position = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0] == 1:
            return True

    def update(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, (self.rect.x + self.text.get_width() / 2 - 0.5, self.rect.y - 0.5))
