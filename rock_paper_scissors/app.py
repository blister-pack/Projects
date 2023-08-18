from PyQt5.QtWidgets import QWidget
from logic import *
from rprpy import *
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

# for it to load the images I have to run it from its own folder and idk why
# works w full path........


class RockPaperScissorsApp(QtWidgets.QMainWindow, Ui_RockPaperScissors):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        rock_img_path = os.path.join("rock_paper_scissors/sprites", "rock.png")
        paper_img_path = os.path.join("rock_paper_scissors/sprites", "paper.png")
        scissors_img_path = os.path.join("rock_paper_scissors/sprites", "scissors.png")
        interrogation_img_path = os.path.join(
            "rock_paper_scissors/sprites", "interrogation.png"
        )

        self.rock_img = QtGui.QPixmap(rock_img_path)
        self.paper_img = QtGui.QPixmap(paper_img_path)
        self.scissors_img = QtGui.QPixmap(scissors_img_path)
        self.interrogation_img = QtGui.QPixmap(interrogation_img_path)

        # button setup
        self.comboBox.currentIndexChanged.connect(self.player_image_move_change)
        self.play_button.clicked.connect(self.play_round)
        # ------------------------------------------------------

        self.player_move_label.setPixmap(self.rock_img)
        # self.player_move_label.setPixmap(QtGui.QPixmap("rock_paper_scissors/sprites/rock.png"))
        self.selected_move = "Rock"
        self.pc_move_label.setPixmap(self.interrogation_img)

        self.player_score = 0
        self.pc_score = 0

    def player_image_move_change(self):
        """
        this function changes the image that represents
        the player's choice for a move
        it's supposed to change when the player changes the move selected
        """

        self.selected_move = self.comboBox.currentText()

        if self.selected_move == "Rock":
            self.player_move_label.setPixmap(self.rock_img)
        elif self.selected_move == "Paper":
            self.player_move_label.setPixmap(self.paper_img)
        elif self.selected_move == "Scissors":
            self.player_move_label.setPixmap(self.scissors_img)

    def pc_move_image_change(self):
        if self.pc_move.data == "rock":
            self.pc_move_label.setPixmap(self.rock_img)
        elif self.pc_move.data == "paper":
            self.pc_move_label.setPixmap(self.paper_img)
        elif self.pc_move.data == "scissor":
            self.pc_move_label.setPixmap(self.scissors_img)

    def change_scores(self, round_result):
        if round_result == True:
            self.player_score += 1
        elif round_result == False:
            self.pc_score += 1

        self.player_score_label.setText(str(self.player_score))
        self.pc_score_label.setText(str(self.pc_score))

    def winner_check(self):
        """right now this func is just a representation, ideally it will
        make a popup window stating the winner and exit the program"""

        if self.player_score == 3:
            self.winner_popup()
            window.close()
        if self.pc_score == 3:
            self.loser_popup()
            window.close()

    def winner_popup(self):
        message = QMessageBox()
        message.setWindowTitle("You won the game!!!")
        message.setText("YOU WON YAY")
        message.exec_()

    def loser_popup(self):
        message = QMessageBox()
        message.setWindowTitle("Computer Wins")
        message.setText("YOU LOST BOO")
        message.exec_()

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
        self.pc_move = computer_move()
        round_result = check_round_win(chosen_move, self.pc_move)

        print(chosen_move.data)
        print(self.pc_move.data)
        print(round_result)

        self.pc_move_image_change()
        self.change_scores(round_result)
        self.winner_check()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RockPaperScissorsApp()
    window.show()
    sys.exit(app.exec_())
