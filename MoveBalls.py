def move_balls(balls, ball_velocities, screen_width, screen_height):
    moved_balls = []
    new_velocities = []
    for (i, (radius, color, x, y)) in enumerate(balls):
        vx, vy = ball_velocities[i]
        new_x = x + vx
        new_y = y + vy

        # 碰撞检测并反弹
        if new_x - radius <= 0 or new_x + radius >= screen_width:
            vx = -vx
        if new_y - radius <= 0 or new_y + radius >= screen_height:
            vy = -vy

        new_x = max(radius, min(new_x, screen_width - radius))
        new_y = max(radius, min(new_y, screen_height - radius))

        moved_balls.append((radius, color, new_x, new_y))
        new_velocities.append((vx, vy))

    return moved_balls, new_velocities

