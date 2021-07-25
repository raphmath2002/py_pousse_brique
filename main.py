from packages.player import Player
from packages.map import Map


import keyboard
import time


if __name__ == "__main__":
    map_object = Map()
    moves_cpt = 0
    restart_lvl_cpt = 0

    print('* X -> un mur\n* . -> espace vide\n* S -> votre personnage\n* O -> une boite\n* 8 -> objectif\n\nAppuyez sur (a) pour commencer, pour vous déplacer utilisez les touches directionelles')

    keyboard.wait('a')

    while(map_object.game_status):
        map = map_object.getMap()

        player = Player(map)

        map_object.applyMap(player)

        boxes = map_object.getBoxes()

        map_object.finished = False

        while (not map_object.finished):

            if keyboard.is_pressed('up'):
                if player.movePlayer('t', boxes, map):
                    moves_cpt += 1
                    map = map_object.applyMap(player)
            elif keyboard.is_pressed('down'):
                if player.movePlayer('b', boxes, map):
                    moves_cpt += 1
                    map = map_object.applyMap(player)
            elif keyboard.is_pressed('left'):
                if player.movePlayer('l', boxes, map):
                    moves_cpt += 1
                    map = map_object.applyMap(player)
            elif keyboard.is_pressed('right'):
                if player.movePlayer('r', boxes, map):
                    moves_cpt += 1
                    map = map_object.applyMap(player)
            if keyboard.is_pressed('r'):
                restart_lvl_cpt += 1
                oldLvl = map_object.level
                map_object.playByLevel(oldLvl)
            if keyboard.is_pressed('ctrl + r'):
                map_object.playByLevel(1)
            if (keyboard.is_pressed('q')):
                map_object.endGame()

            time.sleep(0.120)

    print('\n Fin du jeu, créé par p2sias\n* Total de coups : ' + str(moves_cpt) +
          '\n* Relances de niveau : '+str(restart_lvl_cpt))
