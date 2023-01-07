import pygame

pygame.init()

matriz = []
var = 0
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# screen
size = (600, 680)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("breakout do lucas")

# creat player
player = pygame.image.load("assets/player_breakout.png")
pos_y = 650
pos_x = 300
move_left = False
move_right = False

# creat ball
ball = pygame.image.load("assets/ball_breakout.png")
ball_dx = 3
ball_dy = 3
ball_pos_x = 300
ball_pos_y = 340

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 30)
score_text = score_font.render('00', True, white, black)
score_text_rect = score_text.get_rect()
score_text_rect.center = (100, 50)
score = 0

# point text
point_font = pygame.font.Font('assets/PressStart2P.ttf', 30)
point_text = point_font.render('00', True, white, black)
point_text_rect = point_text.get_rect()
point_text_rect.center = (500, 50)
point = 0

# victory or defeat text
final_font = pygame.font.Font('assets/PressStart2P.ttf', 45)
victory_text = final_font.render("you win!", True, green, black)
defeat_text = final_font.render("you lose!", True, red, black)
victory_text_rect = victory_text.get_rect()
defeat_text_rect = defeat_text.get_rect()
victory_text_rect.center = (300, 340)
defeat_text_rect.center = (300, 340)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# import bricks
yellow_brick = pygame.image.load("assets/yellow_brick.png")
green_brick = pygame.image.load("assets/green_brick.png")
orange_brick = pygame.image.load("assets/orange_brick.png")
red_brick = pygame.image.load("assets/red_brick.png")


def creat_bricks(color, x, y):
    for b in range(14):
        square = [color, x, y]
        lista.append(square)
        x += 42


# creat bricks
lista = []
creat_bricks(yellow_brick, 5, 224)
creat_bricks(yellow_brick, 5, 211)
matriz.append(lista)
lista = []
creat_bricks(green_brick, 5, 198)
creat_bricks(green_brick, 5, 185)
matriz.append(lista)
lista = []
creat_bricks(orange_brick, 5, 172)
creat_bricks(orange_brick, 5, 159)
matriz.append(lista)
lista = []
creat_bricks(red_brick, 5, 146)
creat_bricks(red_brick, 5, 133)
matriz.append(lista)

loop = True
game_clock = pygame.time.Clock()

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False

    if point < 4:
        screen.fill(black)

        # balls collision with the wall
        if ball_pos_x >= 600 or ball_pos_x <= 0:
            ball_dx *= -1
            bounce_sound_effect.play()
            var = 0
        if ball_pos_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()
            var = 0
        if ball_pos_y >= 680:
            ball_pos_x = 300
            ball_pos_y = 340
            ball_dy *= -1
            scoring_sound_effect.play()
            point += 1
            var = 0

        # ball and paddle collision
        if (
            ball_pos_x + 10 >= pos_x and ball_pos_x <= pos_x + 40
            and ball_pos_y + 10 >= pos_y and ball_pos_y <= pos_y + 10
        ):
            ball_dy = 3
            ball_dy *= -1
            bounce_sound_effect.play()
            var = 0
            ball_pos_y = 639

        # paddle movement
        if move_left:
            pos_x -= 5
        else:
            pos_x += 0

        if move_right:
            pos_x += 5
        else:
            pos_x += 0

        # limit movement paddle
        if pos_x <= 0:
            pos_x = 0
        elif pos_x >= 560:
            pos_x = 560

        # balls movement
        ball_pos_x += ball_dx
        ball_pos_y += ball_dy

        # score and point update
        score_text = score_font.render(str(score), True, white, black)
        point_text = point_font.render(str(point), True, white, black)

        # draw objects
        screen.blit(player, (pos_x, pos_y))
        screen.blit(ball, (ball_pos_x, ball_pos_y))
        for line in range(len(matriz)):
            for brick in range(len(matriz[line])):
                # brick and ball collision
                if (
                    ball_pos_x + 10 >= matriz[line][brick][1] and ball_pos_x <= matriz[line][brick][1] + 40
                    and ball_pos_y + 10 >= matriz[line][brick][2] and ball_pos_y <= matriz[line][brick][2] + 10
                ):
                    bounce_sound_effect.play()
                    if var == 0:
                        ball_dy *= -1
                        matriz[line][brick][2] = 1000
                        var = 1
                        if line == 0:
                            score += 1
                        elif line == 1:
                            score += 3
                        elif line == 2:
                            score += 5
                        elif line == 3:
                            score += 7
                screen.blit(matriz[line][brick][0], (matriz[line][brick][1], matriz[line][brick][2]))
        screen.blit(score_text, score_text_rect)
        screen.blit(point_text, point_text_rect)

    # victory condition
    if score >= 448:
        screen.fill(black)
        screen.blit(victory_text, victory_text_rect)

    # defeat condition
    if point >= 4:
        screen.fill(black)
        screen.blit(defeat_text, defeat_text_rect)

    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
