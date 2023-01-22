

def creat_arena(file_name):
    list_of_rect = []
    archive = open(file_name, "r")
    lista_of_lines = archive.readlines()
    t1, t2, t3, t4 = 0, 0, 0, 0
    location1, location2, location3, location4 = 0, 0, 0, 0
    for line in range(len(lista_of_lines)):
        for column in range(len(lista_of_lines[line])):
            if lista_of_lines[line][column] == "2":
                w = 1
                h = 1
                while lista_of_lines[line][column + w] == "1":
                    w += 1
                while lista_of_lines[line + h][column] == "3":
                    h += 1
                rect = (((column * 5) + 20), ((line * 15) + 80), (w * 5), (h * 15))
                list_of_rect.append(rect)
            if lista_of_lines[line][column] == "a" and t1 == 0:
                t1 += 1
                location3 = (((column * 5) + 39), ((line * 15) + 99))
            if lista_of_lines[line][column] == "b" and t2 == 0:
                t2 += 1
                location1 = (((column * 5) + 39), ((line * 15) + 99))
            if lista_of_lines[line][column] == "c" and t3 == 0:
                t3 += 1
                location2 = (((column * 5) + 39), ((line * 15) + 99))
            if lista_of_lines[line][column] == "d" and t4 == 0:
                t4 += 1
                location4 = (((column * 5) + 39), ((line * 15) + 99))
    list_spawn_position = [location1, location2, location3, location4]

    archive.close()
    return list_of_rect, list_spawn_position
