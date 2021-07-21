from packages.player import Player
from packages.map import Map

import keyboard
import time


def printMap(map, cpt, mapObj):
    print('\nNiveau : ' + str(mapObj.level))
    for y in range(len(map)):
        print(*map[y])
    print('Coups : ' + str(cpt))
    print('Boites sur objectif : ' + str(mapObj.doneBoxes))
    print('_______________________')
    print('* Rejouer (r)')
    print('* Quitter (q)')

    return map


if __name__ == "__main__":
    map_object = Map()

    while(map_object.game_status):
        map = map_object.getMap()

        player = Player(map)

        cpt = 0

        printMap(map_object.applyMap(player), cpt, map_object)

        boxes = map_object.getBoxes()

        map_object.finished = False

        while (not map_object.finished):

            if (keyboard.is_pressed('up')):
                if player.movePlayer('t', boxes, map):
                    cpt += 1
                    map = map_object.applyMap(player)
                    printMap(map, cpt, map_object)
            elif (keyboard.is_pressed('down')):
                if player.movePlayer('b', boxes, map):
                    cpt += 1
                    map = map_object.applyMap(player)
                    printMap(map, cpt, map_object)
            elif (keyboard.is_pressed('left')):
                if player.movePlayer('l', boxes, map):
                    cpt += 1
                    map = map_object.applyMap(player)
                    printMap(map, cpt, map_object)
            elif (keyboard.is_pressed('right')):
                if player.movePlayer('r', boxes, map):
                    cpt += 1
                    map = map_object.applyMap(player)
                    printMap(map, cpt, map_object)

            time.sleep(0.120)

    print('[**] GAME OVER [**]')
