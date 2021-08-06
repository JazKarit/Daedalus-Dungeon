import pygame

pygame.init()
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

class AnswerBox:

    def __init__(self, correct_answer, x, y, w, h, settings, screen):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = ''
        self.txt_surface = FONT.render(self.text, True, self.color)
        self.active = False
        self.settings = settings
        self.screen = screen
        self.correct_answer = correct_answer
        self.is_invisible = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                if round(float(self.text),1) == self.correct_answer:
                    return 'correct'
                else:
                    return 'wrong'
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[0:-1]
            else:
                self.text += event.unicode
            # Re-render the text.
            self.txt_surface = FONT.render(self.text, True, self.color)
            return 'no attempt'

    def update(self):
        # Resize the box if the text is too long.
        width = max(20, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        if not self.is_invisible:
            # Blit the text.
            self.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
            # Blit the rect.
            pygame.draw.rect(self.screen, self.color, self.rect, 2)