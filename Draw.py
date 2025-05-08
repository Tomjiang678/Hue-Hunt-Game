import pygame
def draw_words(screen, font, screen_width, screen_height, words, y_position):
    # draw score on screen
    words_surface = font.render(str(words), True, (0, 0, 0))
    words_x = screen_width // 2
    words_y = screen_height * y_position / 10
    words_rect = words_surface.get_rect(center=(words_x, words_y))
    screen.blit(words_surface, words_rect)
    pygame.display.flip()
def draw_words_no_flip(screen, font, screen_width, screen_height, words, y_position):
    # draw score on screen
    words_surface = font.render(str(words), True, (0, 0, 0))
    words_x = screen_width // 2
    words_y = screen_height * y_position / 10
    words_rect = words_surface.get_rect(center=(words_x, words_y))
    screen.blit(words_surface, words_rect)


