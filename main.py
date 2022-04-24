from board import Board
from shape import Shape
import time
from utils import keyCheck


board = Board()
spwanNewBlock = True
print("TETRIS")
print(f"press \'b\' to quit.")
print("A S D to move")
print("Q & E to rotate\n")

input("Press enter to start\n")


while True:

    if spwanNewBlock:
        randomBlock = Shape()
        spwanNewBlock = not spwanNewBlock

    if not board.checkBottomMove(randomBlock.positions):
        spwanNewBlock = True

    if board.checkGameOver(randomBlock.positions):
        print("\n GAME OVER ! \n")
        break

    keyTapped = keyCheck()
    if "Q" in keyTapped:
        randomBlock.rotate(left=True)
    elif "E" in keyTapped:
        randomBlock.rotate(right=True)
    elif "A" in keyTapped and board.checkLeftMove(randomBlock.positions):
        randomBlock.moveLeft()
    elif "D" in keyTapped and board.checkRightMove(randomBlock.positions):
        randomBlock.moveRight()
    elif "S" in keyTapped and board.checkBottomMove(randomBlock.positions):
        randomBlock.moveDown()
    elif "B" in keyTapped:
        break

    board.draw(randomBlock.positions)
    time.sleep(0.3)

print(f"Your score : {board.score}")
