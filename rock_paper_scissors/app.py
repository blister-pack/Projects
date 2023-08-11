from PyQt5.QtWidgets import QWidget
from logic import *
from rprpy import *
import sys
from PyQt5 import QtCore, QtWidgets

# for it to load the images I have to run it from its own folder and idk why
# works w full path........


class RockPaperScissorsApp(QtWidgets.QMainWindow, Ui_RockPaperScissors):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.logic = None

        # button setup
        self.comboBox.currentIndexChanged.connect(self.player_image_move_change)

        # ------------------------------------------------------

    def player_image_move_change(self):
        """
        this function changes the image that represents
        the player's choice for a move
        it's supposed to change when the player changes the move selected
        """
        rock_img = QtGui.QPixmap(
            "/home/blister-pack/Documents/code_projects/1WORK/Projects/rock_paper_scissors/sprites/rock.png"
        )
        paper_img = QtGui.QPixmap(
            "/home/blister-pack/Documents/code_projects/1WORK/Projects/rock_paper_scissors/sprites/paper.png"
        )
        scissors_img = QtGui.QPixmap(
            "/home/blister-pack/Documents/code_projects/1WORK/Projects/rock_paper_scissors/sprites/scissors.png"
        )

        selected_move = self.comboBox.currentText()
        if selected_move == "Rock":
            self.player_move_label.setPixmap(rock_img)
        elif selected_move == "Paper":
            self.player_move_label.setPixmap(paper_img)
        elif selected_move == "Scissors":
            self.player_move_label.setPixmap(scissors_img)

    def pc_move_image_change(self):
        pass

    def change_scores(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RockPaperScissorsApp()
    window.show()
    sys.exit(app.exec_())
