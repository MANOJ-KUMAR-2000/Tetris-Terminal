import random


class Shape():
    
    shapes = {
        "S" : [[" "," "," "],["*","*"," "],[" ","*","*"]],
        "L" : [[" ","*"," "],[" ","*"," "],[" ","*","*"]],
        "T" : [["*","*","*"],[" ","*"," "],[" ","*"," "]],
        "SQ": [[" "," "," "],[" ","*","*"],[" ","*","*"]],
        "Z" : [[" "," "," "],["*","*"," "],[" ","*","*"]],
        "ML": [[" "," ","*"],[" "," ","*"],[" ","*","*"]],
        "I" : [[" ","*"," "],[" ","*"," "],[" ","*"," "]]
    }


    def __init__(self) -> None:
        self.randomShapeName = list(Shape.shapes.keys())[random.randrange(len(Shape.shapes.keys()))]
        self.block = Shape.shapes[self.randomShapeName]
        self.positions = self._setBlockPos()
        self._randomSpwanPos = random.randrange(2, 6)
        for i in range(len(self.positions)):
            self.positions[i][1] += self._randomSpwanPos


    def _setBlockPos(self):
        pos = []
        for i in range(3):
            for j in range(3):
                if self.block[i][j] == "*":
                    pos.append([i, j+1])
        return pos


    def _transpose(self):
        self.block = list(map(list, zip(*self.block)))


    def rotate(self, left=False, right=False):
        row_shape = []
        col_shape = []
        for i in self.positions:
            row_shape.append(i[0])
            col_shape.append(i[1])

        min_row = min(row_shape)
        min_col = min(col_shape)
        max_row = max(row_shape)
        max_col = max(col_shape)

        tmp = [[0 for x in range(max_col-min_col + 1)] for y in range(max_row-min_row+1)]
        for i in self.positions:
            xc = i[0]-min_row
            yc = i[1]-min_col
            tmp[xc][yc] = 1 
        if right:
            nbl = list(zip(*tmp[::-1]))
        if left:
            nbl = list(zip(*tmp[::-1]))[::-1]
            for i in range(len(nbl)):
                nbl[i] = nbl[i][::-1]
        ret = []
        for i in range(max_row-min_row+1):
            for j in range(max_col - min_col + 1):
                if(nbl[j][i] == 1):
                    ret.append([min_row+j, min_col+i])
        self.positions = ret
       

    def moveLeft(self):
        for i in range(len(self.positions)):
            self.positions[i][1] -= 1


    def moveRight(self):
        for i in range(len(self.positions)):
            self.positions[i][1] += 1


    def moveDown(self):
        for i in range(len(self.positions)):
            self.positions[i][0] += 1
