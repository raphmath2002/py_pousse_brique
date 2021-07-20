class Player:
    map = None
    posX = None
    posY = None

    def __init__(self, map):
        self.map = map

        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x] == '.':
                    self.posX = x
                    self.posY = y

    def movePlayer(self, direction, boxes, map):
        t_dir = ''

        if direction == 't':
            canMove = True
            if self.map[self.posY - 1][self.posX] == 'X':
                canMove = False
            else:
                for box in boxes:
                    if self.posY - 1 == box.posY and self.posX == box.posX and not box.moveBox('t', map):
                        canMove = False

            if canMove:
                self.posY -= 1
                return True
            return False

        elif direction == 'b':
            canMove = True
            if self.map[self.posY + 1][self.posX] == 'X':
                canMove = False
            else:
                for box in boxes:
                    if self.posY + 1 == box.posY and self.posX == box.posX and not box.moveBox('b', map):
                        canMove = False

            if canMove:
                self.posY += 1
                return True
            return False
        elif direction == 'l':
            canMove = True
            if self.map[self.posY][self.posX - 1] == 'X':
                canMove = False
            else:
                for box in boxes:
                    if self.posY == box.posY and self.posX - 1 == box.posX and not box.moveBox('l', map):
                        canMove = False

            if canMove:
                self.posX -= 1
                return True
            return False
        else:
            canMove = True
            if self.map[self.posY][self.posX + 1] == 'X':
                canMove = False
            else:
                for box in boxes:
                    if self.posY == box.posY and self.posX + 1 == box.posX and not box.moveBox('r', map):
                        canMove = False

            if canMove:
                self.posX += 1
                return True
            return False
