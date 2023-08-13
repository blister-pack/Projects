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

        # button setup
        self.comboBox.currentIndexChanged.connect(self.player_image_move_change)
        self.play_button.clicked.connect(self.play_round)
        # ------------------------------------------------------

        self.selected_move = "Rock"

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

        self.selected_move = self.comboBox.currentText()

        if self.selected_move == "Rock":
            self.player_move_label.setPixmap(rock_img)
        elif self.selected_move == "Paper":
            self.player_move_label.setPixmap(paper_img)
        elif self.selected_move == "Scissors":
            self.player_move_label.setPixmap(scissors_img)

    def pc_move_image_change(self):
        pass

    def change_scores(self):
        pass

    # this game needs to be played differently than the original logic
    # originally, the logic was supposed to keep the game going until
    # someone reached a score of 3 - here it's more or less like playing
    # three small games (rounds) when the button is clicked
    def play_round(self):
        def reformat_selected_move():
            """
            function to manipulate the string to match
            the strings inside the logic, only then can I get the
            right move
            """

        if self.selected_move == "Rock":
            self.selected_move = "rock"
        elif self.selected_move == "Paper":
            self.selected_move = "paper"
        elif self.selected_move == "Scissors":
            self.selected_move = "scissor"

        # hope this doesn't cause conflicts with the image changing function
        # I still get the object associated with seleted_move and not
        # the string.......... what?

        reformat_selected_move()
        chosen_move = player_move(self.selected_move)
        print(chosen_move.data)
        pc_move = computer_move()
        print(pc_move.data)
        # I think I need to use the play_game function and am doing this wrong


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RockPaperScissorsApp()
    window.show()
    sys.exit(app.exec_())
