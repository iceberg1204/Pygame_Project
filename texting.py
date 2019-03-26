from helpers import helper_text_objects, helper_text_height


# Text class.
class Text:
    def __init__(self, surface, text, t_coords, t_color, t_bg=None):
        self.surface = surface
        self.text = text
        self.coords = t_coords
        self.color = t_color
        self.bg = t_bg

    # Drawing text.
    def draw_text(self):
        self.text_surf, self.text_rect = helper_text_objects(self.text, self.color, self.bg)
        self.surface.blit(self.text_surf, self.coords)

