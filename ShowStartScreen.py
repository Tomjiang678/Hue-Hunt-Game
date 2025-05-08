import pygame
import sys
def show_start_screen(screen, font, high_score, small_font):
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Hue Hunt - 色调猎手")
    title = "HUE HUNT"
    rainbow_colors = [
        (255, 0, 0),  # 红
        (255, 127, 0),  # 橙
        (255, 243, 10),  # 黄
        (0, 255, 0),  # 绿
        (0, 255, 255), # 青
        (0, 0, 255),  # 蓝
        (148, 0, 211)  # 紫
    ]
    char_surfaces = []
    color_index = 0
    for char in title:
        if char == " ":
            char_surfaces.append(font.render(char, True, (255, 255, 255)))  # 空格用白色
        else:
            color = rainbow_colors[color_index % len(rainbow_colors)]
            char_surfaces.append(font.render(char, True, color))
            color_index += 1

    # 计算总宽度后居中显示
    total_width = sum(surf.get_width() for surf in char_surfaces)
    x = (screen.get_width() - total_width) // 2
    y = 200
    for surf in char_surfaces:
        screen.blit(surf, (x, y))
        x += surf.get_width()

    # 提示信息
    tip_text = small_font.render("Click the ball in color gradient order", True, (100, 100, 100))
    screen.blit(tip_text, ((screen.get_width() - tip_text.get_width()) // 2, 300))

    # 按钮
    button_width, button_height = 200, 80
    button_x = (screen.get_width() - button_width) // 2
    button_y = 450
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    pygame.draw.rect(screen, (0, 150, 200), button_rect)
    button_text = small_font.render("START", True, (255, 255, 255))
    screen.blit(button_text, (button_x + (button_width - button_text.get_width()) // 2,
                              button_y + (button_height - button_text.get_height()) // 2))

    high_score_text = small_font.render(f"Highest Score: {high_score}", True, (0, 0, 0))
    screen.blit(high_score_text, ((screen.get_width() - high_score_text.get_width()) // 2, 0.8 * screen.get_height()))

    pygame.display.flip()

    # 等待点击
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    waiting = False  # 退出初始页面，开始游戏
