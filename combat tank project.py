import pygame
from modulos import list_of_objects
from combat_tank_colisao import collision_tank_or_ball
from combat_tank_colisao import collision_tank_ball
from config import *


def creat_tank(tank_photo):
    photo = pygame.Surface((tank_photo.get_width(), tank_photo.get_height()))
    photo.set_colorkey(orange)
    pygame.draw.rect(photo, orange, (0, 0, *tank_photo.get_size()))
    photo.blit(tank_photo, (0, 0))
    tanks_angle = 0
    vel = (speed_x_tanks, speed_y_tanks)
    speed_tank = pygame.math.Vector2(vel)
    recharge_time1 = 0 + 0
    balls_list = []
    variable = [
        photo, tanks_angle, [False, False, False, False, False], recharge_time1,
        speed_tank, balls_list, 3]
    return variable


# victory text
font = pygame.font.Font('assets/PressStart2P.ttf', 45)
victory_text1 = font.render("player green win", True, green, black)
victory_text2 = font.render("player red win", True, red, black)
victory_text1_rect = victory_text1.get_rect()
victory_text2_rect = victory_text2.get_rect()
victory_text1_rect.center = (450, 275)
victory_text2_rect.center = (450, 275)

# hud
hud_font = pygame.font.Font('assets/PressStart2P.ttf', 45)
hud1_text = hud_font.render("3", True, green, black)
hud2_text = hud_font.render("3", True, red, black)
hud1_text_rect = hud1_text.get_rect()
hud2_text_rect = hud2_text.get_rect()
hud1_text_rect.center = (70, 30)
hud2_text_rect.center = (830, 30)
score1 = 3
score2 = 3

# sounds
shoot_sound = pygame.mixer.Sound("assets/tiger.wav")
tank_explode = pygame.mixer.Sound("assets/tank_explode.wav")
bounce_ball = pygame.mixer.Sound("assets/bounce_ball.wav")
tank_walk = pygame.mixer.Sound("assets/tank_walk.wav")
time_sound = tank_walk.get_length()
time_stop = 0

pygame.init()


# screen
size = (900, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("combat tank")
screen.fill(orange)

speed_ball_x = 0
speed_ball_y = 0

# tank 1
archive = pygame.image.load("assets/tank1.png")
tank1 = creat_tank(archive)
tank1.insert(0, archive)
tank1.insert(2, spawn_x_tank_1)
tank1.insert(3, spawn_y_tank_1)
tank1.insert(4, spawn_x_tank_1)
tank1.insert(5, spawn_y_tank_1)
tank1.append(1)

# tank 2
archive = pygame.image.load("assets/tank2.png")
tank2 = creat_tank(archive)
tank2.insert(0, archive)
tank2.insert(2, spawn_x_tank_2)
tank2.insert(3, spawn_y_tank_2)
tank2.insert(4, spawn_x_tank_2)
tank2.insert(5, spawn_y_tank_2)
tank2.append(2)

list_two_tank = [tank1, tank2]
angle_tank = 0
image = 0
tank_animation_rect = 0
tank_animation_x, tank_animation_y, tank_enemy_photo, tank_enemy_rect = 0, 0, 0, 0

# objects
list_of_objects = list_of_objects(screen, yellow)

# wall
wall1 = pygame.draw.rect(screen, yellow, (0, 100, 900, 25))
wall2 = pygame.draw.rect(screen, yellow, (0, 625, 900, 25))
wall3 = pygame.draw.rect(screen, yellow, (0, 100, 25, 800))
wall4 = pygame.draw.rect(screen, yellow, (875, 100, 25, 800))

clock = pygame.time.Clock()

loop = True
recharge = False
respawn = False
no_animation = True
stop = False
victory1 = False
victory2 = False
time = 0

# game loop
while loop:
    list_two_tank[1][7][3] = False
    list_two_tank[0][7][3] = False
    respawn = False
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            loop = False

        # configuring game keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                loop = False
            if event.key == pygame.K_w:
                list_two_tank[0][7][0] = True
            if event.key == pygame.K_d:
                list_two_tank[0][7][1] = True
            if event.key == pygame.K_a:
                list_two_tank[0][7][2] = True
            if event.key == pygame.K_t and (not list_two_tank[0][7][4]):
                list_two_tank[0][7][3] = True
                list_two_tank[0][7][4] = True
                list_two_tank[0][8] = pygame.time.get_ticks()

            if event.key == pygame.K_UP:
                list_two_tank[1][7][0] = True
            if event.key == pygame.K_RIGHT:
                list_two_tank[1][7][1] = True
            if event.key == pygame.K_LEFT:
                list_two_tank[1][7][2] = True
            if event.key == pygame.K_l and (not list_two_tank[1][7][4]):
                list_two_tank[1][7][3] = True
                list_two_tank[1][7][4] = True
                list_two_tank[1][8] = pygame.time.get_ticks()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                list_two_tank[0][7][0] = False
            if event.key == pygame.K_d:
                list_two_tank[0][7][1] = False
            if event.key == pygame.K_a:
                list_two_tank[0][7][2] = False

            if event.key == pygame.K_UP:
                list_two_tank[1][7][0] = False
            if event.key == pygame.K_RIGHT:
                list_two_tank[1][7][1] = False
            if event.key == pygame.K_LEFT:
                list_two_tank[1][7][2] = False

    counter = pygame.time.get_ticks()
    screen.fill(orange)
    if no_animation and not victory1 and not victory2:
        for tank in list_two_tank:
            if stop:
                stop = False
                break
            tank_foto = tank[0]
            image = tank[1]
            origin_x = tank[2]
            origin_y = tank[3]
            tank_x = tank[4]
            tank_y = tank[5]
            angle_tank = tank[6]
            move = tank[7][0]
            giro_right = tank[7][1]
            giro_left = tank[7][2]
            tiro = tank[7][3]
            recharge = tank[7][4]
            recharge_time = tank[8]
            speed = tank[9]
            lista_de_bolas = tank[10]
            tank_life = tank[11]
            score = tank[12]
            if tank[12] == 1:
                tank_enemy_photo = list_two_tank[1][0]
                tank_enemy_rect = tank_enemy_photo.get_rect()
                tank_enemy_angle = list_two_tank[1][6]
                tank_enemy_surface = list_two_tank[1][1]
                tank_enemy_x = list_two_tank[1][4]
                tank_enemy_y = list_two_tank[1][5]
                tank_enemy_balls = list_two_tank[1][10]
                tank_enemy_rect.center = (tank_enemy_x, tank_enemy_y)
                tank_enemy_score = list_two_tank[1][12]
            else:
                tank_enemy_photo = list_two_tank[0][0]
                tank_enemy_rect = tank_enemy_photo.get_rect()
                tank_enemy_angle = list_two_tank[0][6]
                tank_enemy_surface = list_two_tank[0][1]
                tank_enemy_x = list_two_tank[0][4]
                tank_enemy_y = list_two_tank[0][5]
                tank_enemy_balls = list_two_tank[0][10]
                tank_enemy_rect.center = (tank_enemy_x, tank_enemy_y)
                tank_enemy_score = list_two_tank[0][12]

            if counter - recharge_time > time_to_recharge:
                tank[7][4] = False

            # tank1 movement
            if (giro_left and move) or (giro_right and move):
                tank[7][0] = False
                tank[7][1] = False
                tank[7][2] = False

            if move:
                tank[4] += speed[0]
                tank[5] += speed[1]
                if counter - time_stop > time_sound * 1000:
                    tank_walk.play()
                    time_stop = pygame.time.get_ticks()

            # ball movement
            for b in tank[10]:
                ball_x = b[2]
                ball_y = b[3]
                speed_ball_x = b[4]
                speed_ball_y = b[5]
                ball_rect = b[1]
                b[2] += b[4]
                b[3] += b[5]
                b[1].center = (b[2], b[3])
                screen.blit(b[0], b[1])

            # rotation of vector angle and image angle
            tank_foto = tank[0]
            image = tank[1]
            angle_tank = tank[6]
            speed = tank[9]
            if giro_right:
                tank[6] += -1
                if tank[6] <= -360:
                    tank[6] = 0
                tank[0] = pygame.transform.rotate(tank[1], tank[6])
                tank[9] = speed.rotate(1)
            if giro_left:
                tank[6] += 1
                if tank[6] >= 360:
                    tank[6] = 0
                tank[0] = pygame.transform.rotate(tank[1], tank[6])
                tank[9] = speed.rotate(-1)

            speed = tank[9]

            # taking tank1's location
            tank_rect = tank_foto.get_rect()
            tank_rect.center = (tank[4], tank[5])

            # tank collision with wall
            if tank_rect.colliderect(wall1):
                tank[5] += +(abs(speed[1]))
            if tank_rect.colliderect(wall2):
                tank[5] += -(abs(speed[1]))
            if tank_rect.colliderect(wall3):
                tank[4] += +(abs(speed[0]))
            if tank_rect.colliderect(wall4):
                tank[4] += -(abs(speed[0]))

            # tank collision and draw obstacle
            tank_x = tank[4]
            tank_y = tank[5]
            comparison_x = tank[4]
            comparison_y = tank[5]
            speed = tank[9]
            for element in list_of_objects:
                obstacle_bit = element[0]
                obstacle_rect_idx = element[1]
                pos = element[2]
                screen.blit(obstacle_bit, obstacle_rect_idx)
                size = obstacle_bit.get_size()
                if tank_rect.colliderect(obstacle_rect_idx):
                    tup = collision_tank_or_ball(
                        tank_x, tank_y, speed[0], speed[1], pos[0], pos[1], size[0], size[1], 0
                    )
                    if comparison_x != tup[0][0]:
                        tank[4] = tup[0][0]
                    if comparison_y != tup[0][1]:
                        tank[5] = tup[0][1]

            # ball collision with objects and wall
            lista_de_bolas = tank[10]
            for ball in tank_enemy_balls:
                ball_image = ball[0]
                ball_rect = ball[1]
                ball_x = ball[2]
                ball_y = ball[3]
                speed_ball_x = ball[4]
                speed_ball_y = ball[5]
                ball_life = ball[6]
                screen.blit(ball_image, ball_rect)
                for element in list_of_objects:
                    obstacle_bit = element[0]
                    obstacle_rect_idx = element[1]
                    pos = element[2]
                    size = obstacle_bit.get_size()
                    if ball_rect.colliderect(obstacle_rect_idx):
                        ball[6] -= 1
                        var = collision_tank_or_ball(
                            ball_x, ball_y, speed_ball_x, speed_ball_y, pos[0], pos[1], size[0], size[1], 1
                        )
                        bounce_ball.play()
                        ball[2] = var[0][0]
                        ball[3] = var[0][1]
                        ball[4] = var[1][0]
                        ball[5] = var[1][1]
                if ball_rect.colliderect(wall1) or ball_rect.colliderect(wall2):
                    ball[5] *= -1
                    ball[6] -= 1
                    bounce_ball.play()
                if ball_rect.colliderect(wall3) or ball_rect.colliderect(wall4):
                    ball[4] *= -1
                    ball[6] -= 1
                    bounce_ball.play()

                # turn animation True
                if ball_rect.colliderect(tank_rect):
                    respawn = collision_tank_ball(ball[4], ball[5], tank[4], tank[5], tank[11])
                    ball[6] = 0
                    no_animation = False
                    stop = True
                    tank_explode.play()
                    angle_tank = tank[6]
                    image = tank[1]
                    tank_animation_rect = tank[0].get_rect()
                    tank_animation_x = tank[4]
                    tank_animation_y = tank[5]
                    tank_p = tank[0]
                    tank[11] -= 1
                    time = pygame.time.get_ticks()

                if ball[6] <= 0:
                    tank_enemy_balls.remove(ball)

            if respawn:
                list_two_tank[0][4] = list_two_tank[0][2]
                list_two_tank[0][5] = list_two_tank[0][3]
                list_two_tank[1][4] = list_two_tank[1][2]
                list_two_tank[1][5] = list_two_tank[1][3]
                respawn = False

            if tiro:
                shoot_sound.play()
                # making tiro
                ball_image = pygame.image.load("assets/bala.png")
                speed_ball_x = speed_x_balls * speed[0]
                speed_ball_y = speed_y_balls * speed[1]
                ball_x = tank_x
                ball_y = tank_y
                ball_rect = pygame.draw.rect(screen, white, (0, 0, ball_image.get_width(), ball_image.get_height()))
                ball_rect.center = (ball_x, ball_y)
                ball_life = 6
                ball = [ball_image, ball_rect, ball_x, ball_y, speed_ball_x, speed_ball_y, ball_life]
                # noinspection PyTypeChecker
                tank[10].append(ball)

            screen.blit(tank_foto, tank_rect)
    if not no_animation and not victory1 and not victory2:
        if counter - time >= 2000:
            no_animation = True
        for obstacle in list_of_objects:
            obstacle_archive = obstacle[0]
            obstacle_rect = obstacle[1]
            screen.blit(obstacle_archive, obstacle_rect)
        angle_tank += 18
        tank_p = pygame.transform.rotate(image, angle_tank)
        tank_animation_rect.center = (tank_animation_x, tank_animation_y)
        screen.blit(tank_p, tank_animation_rect)
        screen.blit(tank_enemy_photo, tank_enemy_rect)
    if list_two_tank[1][11] <= 0:
        victory1 = True
    if list_two_tank[0][11] <= 0:
        victory2 = True

    # draw walls
    wall1 = pygame.draw.rect(screen, yellow, (0, 100, 900, 20))
    wall2 = pygame.draw.rect(screen, yellow, (0, 630, 900, 20))
    wall3 = pygame.draw.rect(screen, yellow, (0, 100, 20, 800))
    wall4 = pygame.draw.rect(screen, yellow, (880, 100, 20, 800))

    # draw hud
    hud1_text = hud_font.render(str(list_two_tank[0][11]), True, green, orange)
    hud2_text = hud_font.render(str(list_two_tank[1][11]), True, red, orange)
    screen.blit(hud1_text, hud1_text_rect)
    screen.blit(hud2_text, hud2_text_rect)

    if victory1:
        screen.fill(black)
        screen.blit(victory_text1, victory_text1_rect)
    if victory2:
        screen.fill(black)
        screen.blit(victory_text2, victory_text2_rect)

    # update screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
