import pygame


def list_of_objects(screen, color):
    lista = []
    obstacle = pygame.image.load("assets/obstacle1.png")
    pos = (430, 120)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], *obstacle.get_size()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (430, 590)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], *obstacle.get_size()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (235, 355)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], *obstacle.get_size()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (625, 355)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], *obstacle.get_size()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    obstacle = pygame.image.load("assets/obstacle2.png")
    pos = (699, 177)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (139, 177)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (699, 551)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (139, 551)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    obstacle = pygame.image.load("assets/obstacle3.png")
    pos = (748, 287)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (130, 287)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    obstacle = pygame.image.load("assets/obstacle4.png")
    pos = (770, 287)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (770, 441)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (110, 287)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (110, 441)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    obstacle = pygame.image.load("assets/obstacle2.png")
    pos = (521, 227)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (521, 503)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (316, 227)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (316, 503)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    obstacle = pygame.image.load("assets/obstacle5.png")
    pos = (562, 249)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (562, 483)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (316, 249)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    pos = (316, 483)
    size = obstacle.get_size()
    obstacle_rect = pygame.draw.rect(screen, color, (pos[0], pos[1], obstacle.get_width(), obstacle.get_height()))
    var = (obstacle, obstacle_rect, pos, size)
    lista.append(var)
    return lista