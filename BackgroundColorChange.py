def change_background_color(t, speed=0.001):
    """
    t: 当前时间（可以是帧数、pygame.time.get_ticks()等）
    speed: 渐变速度，默认较慢
    返回一个浅色范围的 RGB 值
    """
    import math
    r = 200 + int(55 * math.sin(speed * t))
    g = 200 + int(55 * math.sin(speed * t + 2))  # 加偏移避免同步变化
    b = 200 + int(55 * math.sin(speed * t + 4))
    return (r, g, b)
