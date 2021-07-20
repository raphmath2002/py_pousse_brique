class Box:
    posX = 0
    posY = 0
    map = []

    on_objective = False

    def __init__(self, x, y, map):
        self.posY = y
        self.posX = x
        self.map = map

    def checkObjective(self, map, dir):
        if dir == 't' and map[self.posY - 1][self.posX] == '8':
            self.in_objective()
        if dir == 'b' and map[self.posY + 1][self.posX] == '8':
            self.in_objective()
        if dir == 'l' and map[self.posY][self.posX - 1] == '8':
            self.in_objective()
        if dir == 'r' and map[self.posY][self.posX + 1] == '8':
            self.in_objective()

    def moveBox(self, direction, map):
        if direction == 't':
            if not (self.map[self.posY - 1][self.posX] == 'X') and not (map[self.posY - 1][self.posX] == 'O'):
                self.checkObjective(map, 't')
                self.posY -= 1
                return True
        elif direction == 'b':
            if not (self.map[self.posY + 1][self.posX] == 'X') and not (map[self.posY + 1][self.posX] == 'O'):
                self.checkObjective(map, 'b')
                self.posY += 1
                return True
        elif direction == 'l':
            if not (self.map[self.posY][self.posX - 1] == 'X') and not (map[self.posY][self.posX - 1] == 'O'):
                self.checkObjective(map, 'l')
                self.posX -= 1
                return True
        else:
            if not (self.map[self.posY][self.posX + 1] == 'X') and not (map[self.posY][self.posX + 1] == 'O'):
                self.checkObjective(map, 'r')
                self.posX += 1
                return True
        return False

    def in_objective(self):
        self.on_objective = True
