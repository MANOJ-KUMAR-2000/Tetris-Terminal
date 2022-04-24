class Board():

    def __init__(self, width=18, height=10) -> None:
        self.width = width
        self.height = height
        self.matrix = self._getIntialMatrix()
        self.score = 0


    def _getIntialMatrix(self):
        matrix = []
        matrix.append(["*"] * self.width)
        for _ in range(self.height-2):
            matrix.append(["*"] + [" "]*(self.width-2) + ["*"])
        matrix.append(["*"] * self.width)
        return matrix


    def checkLeftMove(self, blockPoss):
        for pos in blockPoss:
            if self.matrix[pos[0]][pos[1]-1] == "*":
                return False
        return True


    def checkRightMove(self, blockPoss):
        for pos in blockPoss:
            if self.matrix[pos[0]][pos[1]+1] == "*":
                return False
        return True


    def checkBottomMove(self, blockPoss):
        for pos in blockPoss:
            if self.matrix[pos[0]+1][pos[1]] == "*":
                return False
        return True


    def checkRowCompletion(self):
        flag = False
        for row_i in reversed(range(1, self.height-1)):
            if " " not in self.matrix[row_i]:
                del self.matrix[row_i]
                self.score += 10
                self.matrix.insert(1, ["*"] + [" "]*(self.width-2) + ["*"])
                flag = True
        return flag
                

    def checkGameOver(self, pos):
        cols = []
        for p in pos:
            cols.append(p[1])
        if "*" in self.matrix[1][min(cols):max(cols)]:
            return True
        return False


    def draw(self, blockPos):
        print(f"\nSCORE : {self.score}")
        temp_matrix = []

        for mat_row in self.matrix:
            temp_matrix.append(mat_row[::])

        for row_i in range(1, len(temp_matrix) - 1):
            for col_j in range(1, len(temp_matrix[0])-1):
                if [row_i, col_j] in blockPos:
                    temp_matrix[row_i][col_j] = "*"

        if not self.checkBottomMove(blockPos) and not self.checkRowCompletion():
            self.matrix.clear()
            for mat_row in temp_matrix:
                    self.matrix.append(mat_row[::])  
            
        for row_i in range(0, len(temp_matrix)):
            print("".join(temp_matrix[row_i]))
        

