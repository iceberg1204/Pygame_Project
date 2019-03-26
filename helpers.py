import pygame


def helper_text_objects(incoming_text, incoming_color, incoming_bg):  # Helper for text writing.
    pygame.font.init()
    if incoming_bg:
        fnt = pygame.font.Font('Poppkorn.ttf', 25)
        text_surface = fnt.render(incoming_text, False, incoming_color, incoming_bg)

    else:
        fnt = pygame.font.Font('Poppkorn.ttf', 30)
        text_surface = fnt.render(incoming_text, False, incoming_color)

    return text_surface, text_surface.get_rect()


def helper_text_height(font):  # Helper for getting text height.
    font_object = font.render('a', False, (0, 0, 0))
    font_rect = font_object.get_rect()

    return font_rect.height
