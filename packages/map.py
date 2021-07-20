from .box import Box
import copy


class Map:

    playerStr = 'S'
    boxStr = 'O'

    level = 1

    started = True
    finished = False

    doneBoxes = 0

    boxes_loc = [
        [
            [4, 4]
        ],

        [
            [4, 4],
            [4, 5],
            [3, 3]
        ]
    ]

    boxes_objects = []

    maps = [
        [
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', 'X', '8', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']

        ],

        [
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', '.', '.', '.', 'X', 'X', '.', '.', '.', '.', 'X'],
            ['X', 'X', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '.', '.', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', 'X'],
            ['X', '8', 'X', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
    ]

    def init_box(self):
        self.boxes_objects = []
        for box_loc in self.boxes_loc[self.level - 1]:
            box = Box(box_loc[1], box_loc[0], self.getMap())
            self.boxes_objects.append(box)

    def __init__(self):
        self.init_box()

    def getMap(self):
        return copy.deepcopy(self.maps[self.level-1])

    def applyMap(self, player):
        map = self.getMap()

        map[player.posY][player.posX] = self.playerStr

        newBoxes = []

        for box in self.boxes_objects:
            if not box.on_objective:
                map[box.posY][box.posX] = self.boxStr
                newBoxes.append(box)
            else:
                self.doneBoxes += 1

        self.boxes_objects = newBoxes

        if len(self.boxes_objects) < 1 and not self.finished:
            self.level += 1
            self.init_box()
            self.finish()

        return map

    def finish(self):
        self.finished = True

    def getBoxes(self):
        return self.boxes_objects

    def nextLevel(self):
        self.level += 1
        self.init_box()
