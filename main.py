import pygame
import numpy as np
import random
import json
import os
import GenerateColorGradient as GCG
import Draw
import MoveBalls
import BackgroundColorChange
import ShowStartScreen
import TimeBar

# 文件路径
HIGH_SCORE_FILE = r"D:\HueHuntData\high_score.json"

# 初始化最高分
def get_high_score():
    # 检查文件是否存在
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'r') as f:
            return json.load(f).get("high_score", 0)
    return 0

# 保存最高分
def save_high_score(score):
    # 确保文件夹存在
    if not os.path.exists(os.path.dirname(HIGH_SCORE_FILE)):
        os.makedirs(os.path.dirname(HIGH_SCORE_FILE))  # 创建文件夹

    high_score = get_high_score()
    if score > high_score:
        # 更新最高分
        with open(HIGH_SCORE_FILE, 'w') as f:
            json.dump({"high_score": score}, f)
#init
pygame.init()
#init font
font = pygame.font.SysFont("Consolas",66, bold = True)
small_font = pygame.font.SysFont("Consolas",36, bold = True)
#init screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
ShowStartScreen.show_start_screen(screen, font, get_high_score(), small_font)
# init score
score = 0
playing = True
while playing:  #if clicking QUIT, playing = False, then the game quits
    #init ball_start_color and ball_end_color
    ball_start_color = (random.randint(50, 250), random.randint(50, 250), random.randint(50, 250)) #随机小球颜色
    color_error_ratio = 0.5
    ball_end_color = tuple(int(x * color_error_ratio) for x in ball_start_color)
    # init balls
    balls = []
    ball_velocities = []
    balls_num = min(max(score // 8 + 3 , 5), 20)  # 球数量随分数增加，但最大值为20
    #init balls_color
    balls_color = GCG.generate_color_gradient(ball_start_color, ball_end_color, balls_num)
    for i in range(balls_num):
        ball_radius = random.uniform(30, 100)
        ball_color = balls_color[i]
        vx = random.uniform(-1, 1) * min(score // 20 * 0.01, 0.25)
        vy = random.uniform(-1, 1) * min(score // 20 * 0.01, 0.25)
        while True:
            ball_x = random.uniform(ball_radius, SCREEN_WIDTH - ball_radius)
            ball_y = random.uniform(ball_radius, SCREEN_HEIGHT - ball_radius)
            new_ball = (ball_radius, ball_color, ball_x, ball_y)
            # 检查是否和已有的球重叠
            overlap = False
            for (r, _, x, y) in balls:
                dist = np.hypot(ball_x - x, ball_y - y)
                if dist < max(ball_radius , r):
                    overlap = True
                    break
            if not overlap:
                balls.append(new_ball)
                break
        ball_velocities.append((vx, vy))
    #mainloop
    running = True
    click_mode = None
    if score < 100:     # TOTAL_TIME will increase with the score
       TOTAL_TIME = 10
    elif 100 <= score <= 200:
        TOTAL_TIME = 20 - 2 * (20 - balls_num)
    else:
        TOTAL_TIME = 20
    start_ticks = pygame.time.get_ticks()
    while running:#if losing games, running = False, but still playing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 左键点击
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if balls:
                    if click_mode is None:
                        # 第一次点击，只允许点击第一个或最后一个球
                        first_ball = balls[0]
                        last_ball = balls[-1]
                        fx, fy, fr = first_ball[2], first_ball[3], first_ball[0]
                        lx, ly, lr = last_ball[2], last_ball[3], last_ball[0]

                        if np.hypot(mouse_x - fx, mouse_y - fy) <= fr:
                            del balls[0]
                            score += 1 * (score // 50 + 1)
                            click_mode = "forward"
                        elif np.hypot(mouse_x - lx, mouse_y - ly) <= lr:
                            del balls[-1]
                            score += 1 * (score // 50 + 1)
                            click_mode = "backward"
                        else:
                            running = False # 错误点击，游戏结束
                            Draw.draw_words(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, "failed!", 3)
                            pygame.time.wait(2000)
                            pygame.event.clear()
                            Draw.draw_words(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, f"your score is {score}", 5)
                            pygame.time.wait(2000)
                            pygame.event.clear()
                            save_high_score(score)
                            score = 0  # init score
                            ShowStartScreen.show_start_screen(screen, font, get_high_score(), small_font)  # return to start_interface


                    elif click_mode == "forward":
                        fx, fy, fr = balls[0][2], balls[0][3], balls[0][0]
                        if np.hypot(mouse_x - fx, mouse_y - fy) <= fr:
                            del balls[0]
                            score += 1 * (score // 50 + 1)
                        else:

                            running = False  # 点击非前端球，游戏结束
                            Draw.draw_words(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, "failed!", 3)
                            pygame.time.wait(2000)
                            pygame.event.clear()
                            Draw.draw_words(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, f"your score is {score}", 5)
                            pygame.time.wait(2000)
                            pygame.event.clear()
                            save_high_score(score)
                            score = 0 #init score
                            ShowStartScreen.show_start_screen(screen, font, get_high_score(), small_font)#return to start_interface


                    elif click_mode == "backward":
                        lx, ly, lr = balls[-1][2], balls[-1][3], balls[-1][0]
                        if np.hypot(mouse_x - lx, mouse_y - ly) <= lr:
                            del balls[-1]
                            score += 1 * (score // 50 + 1)
                        else:
                            running = False  # 点击非末端球，游戏结束
                            Draw.draw_words(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, "failed!", 3)
                            pygame.time.wait(2000)
                            pygame.event.clear()
                            Draw.draw_words(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, f"your score is {score}", 5)
                            pygame.time.wait(2000)
                            pygame.event.clear()
                            save_high_score(score)
                            score = 0  # init score
                            ShowStartScreen.show_start_screen(screen, font, get_high_score(), small_font)  # return to start_interface
        # fill screen
        if score <= 200:
            screen.fill((255, 255, 255))
        else:  #if score > 200, bg_color will change
            bg_color = BackgroundColorChange.change_background_color(pygame.time.get_ticks())
            screen.fill(bg_color)
        if score > 100: #if score > 100, balls will move
            balls, ball_velocities = MoveBalls.move_balls(balls, ball_velocities, SCREEN_WIDTH,
                                                          SCREEN_HEIGHT)
        # draw balls on screen
        for (radius, color, x, y) in balls:
            pygame.draw.circle(screen, color, (x, y), radius)
        # draw score on screen
        Draw.draw_words_no_flip(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, score, 1)
        if running: #if not running, timebar should keep still
            remaining = TimeBar.draw_timer_bar(screen, TOTAL_TIME, start_ticks, SCREEN_WIDTH, SCREEN_HEIGHT)
            if remaining <= 0:
                running = False
                Draw.draw_words(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, "Time's up!", 3)
                pygame.time.wait(2000)
                pygame.event.clear()
                Draw.draw_words(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, f"your score is {score}", 5)
                pygame.time.wait(2000)
                pygame.event.clear()
                save_high_score(score)
                score = 0
                ShowStartScreen.show_start_screen(screen, font, get_high_score(), small_font)
        # if no balls, win!
        if not balls:
            running = False
            Draw.draw_words(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT, "great!", 3)
            pygame.time.wait(1000)
            pygame.event.clear()

        #upgrade screen
        pygame.display.flip()

