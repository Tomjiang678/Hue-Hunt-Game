import pygame
def draw_timer_bar(screen, total_time, start_ticks, screen_width, screen_height):
    """
    total_time: 总时间（秒）
    start_ticks: 游戏开始时 pygame.time.get_ticks() 的值
    """
    # 计算剩余时间
    elapsed_ms = pygame.time.get_ticks() - start_ticks
    remaining_time = max(0, total_time - elapsed_ms / 1000)

    # 时间条的最大宽度
    max_bar_width = screen_width * 0.8
    bar_height = 20
    bar_width = int((remaining_time / total_time) * max_bar_width)

    # 位置
    bar_x = (screen_width - max_bar_width) // 2
    bar_y = 30

    # 绘制背景条（灰色）
    pygame.draw.rect(screen, (200, 200, 200), (bar_x, bar_y, max_bar_width, bar_height))
    # 绘制前景条（绿色，表示剩余时间）
    pygame.draw.rect(screen, (0, 200, 0), (bar_x, bar_y, bar_width, bar_height))

    return remaining_time  # 可以用于判断时间是否耗尽
