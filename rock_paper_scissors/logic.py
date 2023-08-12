from random import randint
from turtle import width
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Linked_rps:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None

    def append(self, data):
        # if it's empty it should do one thing,
        # if it's not it should do another

        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head

        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def connect(self):
        self.last_node.next = (
            self.head
        )  # this should turn it into a circular LL and break __repr__

    def __repr__(self) -> str:
        itr = self.head
        representation = ""

        while itr:
            representation += itr.data + " --> "
            itr = itr.next
            if itr.data == self.head.data:  # circular list can now be printed
                representation += itr.data
                break

        return representation


# DONE user must choose a move
# DONE computer must choose a move
# DONE the moves should work by choosing one object from the LL
# DONE make a game function that actually runs a game and counts scores
# DONE there must be a score counter to make the game stop
# DONE function that evaluates a round and returns its result
# DONE upload to git
# DONE make a GUI (PyQt)
# TODO make it run on Android
# TODO make the program get opponent's move from a website
# TODO mp3 sound
# DONE make circular list be printed but showing the connection to the head

L = Linked_rps()
L.append("rock")
L.append("scissor")
L.append("paper")
L.connect()
print(L)


# player move should be an input
def player_move(rps):
    # func should return chosen object
    moves = ["rock", "scissor", "paper"]

    if rps in moves:
        ind = moves.index(rps)
        move = L.head

        """
        if the move isn't rock, then the for loop serves
        to search for the right one in the linked list
        """
        for _ in range(ind):
            move = move.next

        return move


def computer_move():
    # func should return chosen object
    """
    function follows the same logic as player_move
    0 - rock; 1 - scissor; 2 - paper
    """
    rand_move = randint(0, 2)
    move = L.head

    for _ in range(rand_move):
        move = move.next

    return move


def check_round_win(move_player, move_pc):
    if move_player == move_pc:
        return "tie"
    elif move_player.next == move_pc:
        return True
    elif move_pc.next == move_player:
        return False


def play_game():
    """Game will be done when one reaches a score of 3"""
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        player_mov = input("rock, paper or scissor? ")
        player_choice = player_move(player_mov)
        computer_choice = computer_move()

        print(
            f"Computer played {computer_choice.data}\nYou played {player_choice.data}"
        )

        round_result = check_round_win(player_choice, computer_choice)
        if round_result == "tie":
            print("That round was a tie!\n")
        elif round_result == True:
            player_score += 1
            print("You won that round!\n")
        elif round_result == False:
            computer_score += 1
            print("You lost that one!\n")

        scores = f"Computer: {computer_score}\nPlayer {player_score}"
        print(scores)

    if computer_score == 3:
        print("You lose, loser!")
    elif player_score == 3:
        print("Congratulations, you win!... Absolutely nothing!")



if __name__ == "__main__":
    L = Linked_rps()
    L.append("rock")
    L.append("scissor")
    L.append("paper")

    print(L)
    L.connect()
    print(L.last_node.next.data)

    play_game()

