import pygame


def keys_down(event, list_of_tank, invisible_mode):
    if len(list_of_tank) >= 2:
        if event.key == pygame.K_w:
            list_of_tank[0].movement = True
        if event.key == pygame.K_d:
            list_of_tank[0].spin_right = True
        if event.key == pygame.K_a:
            list_of_tank[0].spin_left = True
        if event.key == pygame.K_s and not list_of_tank[0].recharge:
            list_of_tank[0].trigger = True
            list_of_tank[0].recharge = True
            list_of_tank[0].time_to_recharge = pygame.time.get_ticks()
        if event.key == pygame.K_m and not invisible_mode[0]:
            invisible_mode[0] = True
        if event.key == pygame.K_n and invisible_mode:
            invisible_mode[0] = False

        if event.key == pygame.K_UP:
            list_of_tank[1].movement = True
        if event.key == pygame.K_RIGHT:
            list_of_tank[1].spin_right = True
        if event.key == pygame.K_LEFT:
            list_of_tank[1].spin_left = True
        if event.key == pygame.K_DOWN and not list_of_tank[1].recharge:
            list_of_tank[1].trigger = True
            list_of_tank[1].recharge = True
            list_of_tank[1].time_to_recharge = pygame.time.get_ticks()

    if len(list_of_tank) >= 3:
        if event.key == pygame.K_t:
            list_of_tank[2].movement = True
        if event.key == pygame.K_h:
            list_of_tank[2].spin_right = True
        if event.key == pygame.K_f:
            list_of_tank[2].spin_left = True
        if event.key == pygame.K_g and not list_of_tank[2].recharge:
            list_of_tank[2].trigger = True
            list_of_tank[2].time_to_recharge = pygame.time.get_ticks()

    if len(list_of_tank) == 4:
        if event.key == pygame.K_i:
            list_of_tank[3].movement = True
        if event.key == pygame.K_l:
            list_of_tank[3].spin_right = True
        if event.key == pygame.K_j:
            list_of_tank[3].spin_left = True
        if event.key == pygame.K_k and not list_of_tank[3].recharge:
            list_of_tank[3].trigger = True
            list_of_tank[3].time_to_recharge = pygame.time.get_ticks()


def keys_up(event, list_of_tank):
    if len(list_of_tank) >= 2:
        if event.key == pygame.K_w:
            list_of_tank[0].movement = False
        if event.key == pygame.K_d:
            list_of_tank[0].spin_right = False
        if event.key == pygame.K_a:
            list_of_tank[0].spin_left = False

        if event.key == pygame.K_UP:
            list_of_tank[1].movement = False
        if event.key == pygame.K_RIGHT:
            list_of_tank[1].spin_right = False
        if event.key == pygame.K_LEFT:
            list_of_tank[1].spin_left = False

    if len(list_of_tank) >= 3:
        if event.key == pygame.K_t:
            list_of_tank[2].movement = False
        if event.key == pygame.K_h:
            list_of_tank[2].spin_right = False
        if event.key == pygame.K_f:
            list_of_tank[2].spin_left = False

    if len(list_of_tank) == 4:
        if event.key == pygame.K_i:
            list_of_tank[3].movement = False
        if event.key == pygame.K_l:
            list_of_tank[3].spin_right = False
        if event.key == pygame.K_j:
            list_of_tank[3].spin_left = False
