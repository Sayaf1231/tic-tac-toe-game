
#This code was an existing idea from the Channel BroCode in youtube But i have made
#a few changes and modifications in this code

#tkintrer is a GUi library it has stuff like buttons frames and etc to show in the GUI
from tkinter import *
import random

#I want a player vs player and player vs AI

#The board should be 3x3 
#[ [0,0]  [0,1]  [0,2]
#  [1,0]  [1,1]  [1,2]
#  [2,0]  [2,1]  [2,2]   ]

#The player should have one move per turn and then switch

#There should be a player win counter

#A confirmation checking tie or win game










board = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]
#has two players and when starts picks a random player between them
playerList = ["player1" , "player2"]
currentPlayer = random.choice(playerList)

playerIcon = ["X", "O"]

#choose two different icons for player1 and player2
assigned_icons = random.sample(playerIcon, 2)

player1_icon = assigned_icons[0]
player2_icon = assigned_icons[1]


def game():
    #will start a new game when pressed the button
    global currentPlayer
    currentPlayer = random.choice(playerList)
    label.config(text=(currentPlayer +"'" + " turn"))

    for x in range(3):
        for y in range(3):
            board[x][y]["text"] = ""
    

#the turn change or win decider
def turn(x,y):

    global currentPlayer

    #checks if there are no players and there are no winners
    if (board[x][y]["text"] == "" and game_winner() is False):
        #if no player and currentplayer is selected as player1 the
        if (currentPlayer == playerList[0]):
            #put the icon representing player1 on the box
            board[x][y]["text"] = player1_icon

            #if there is no winner on that turn then switch turns
            if (game_winner() is False):
                currentPlayer = playerList[1]
                #board[x][y]["text"] = player2_icon
                label.config(text= (playerList[1] +"'s" + " turn"))
            #if winner exist end game 
            elif (game_winner() is True):
                label.config(text= (playerList[0] +" is the winner"))

            elif (game_winner() == "T"):
                label.config(text="TIE GAME!!")

        else:
            #put the icon representing player1 on the box
            board[x][y]["text"] = player2_icon

            #if there is no winner on that turn then switch turns
            if (game_winner() is False):
                currentPlayer = playerList[0]
                #board[x][y]["text"] = player1_icon
                label.config(text= (playerList[0] +"'s" + " turn") )

            elif (game_winner() is True):
                label.config(text= (playerList[1] +" is the winner"))

            elif (game_winner() == "T"):
                label.config(text="TIE GAME!!")

#based on the conditions determine a winner/loser or tie game
def game_winner():
    #keeping track of space for tie game
    #if all spaces are filled and no result found then TIE
    empty_space = 9
    for R in range(3):
        for C in range(3):
            if(board[R][C]["text"] != "" and empty_space != 0):
                empty_space -= 1
    #so if the icons are similar in that row
    #if [0,0] == [0,1] == [0,2]
    #if [1,0] == [1,1] == [1,2]
    #if [2,0] == [2,1] == [2,2]
    for x in range(3):
        if(board[x][0]["text"] == board[x][1]["text"] == board[x][2]["text"] != ""):
            return True
    
    #if the icons are similar in that columm
    #if [0,0] == [1,0] == [2,0]
    #if [0,1] == [1,1] == [2,1]
    #if [0,2] == [1,2] == [2,2]
    for y in range(3):
        if(board[0][y]["text"] == board[1][y]["text"] == board[2][y]["text"] != ""):
            return True

    #if the icons are similar in that diag
    #if [0,0] == [1,1] == [2,2]
    #if [0,2] == [1,1] == [2,0]
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != ""):
            return True
    elif(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != ""):
            return True
    

    #if there is a tie that means all the spaces need to be used
    elif(empty_space == 0):
        return "T"
    else:
        return False



#this is to show the gui
window = Tk()
window.title("Tic-Tac-Toe")

#turn picker and lable that says whos turn it is
label = Label(text= currentPlayer+"'s" + " turn", font=("",20))
label.pack(side="top")

#game start and reset button
game_start_but = Button(text="Restart", font=("",15), command= game)
game_start_but.pack(side="top",anchor="ne")

#container 
frame = Frame(window)
frame.pack()

for X in range(0,3):
    for Y in range(0,3):
        board[X][Y] = Button(frame, text="",font=("",15), width=10, height=5
                             , command= lambda X=X,Y=Y: turn(X,Y))
        board[X][Y].grid(row=X, column=Y)

#main event to start the gui
window.mainloop()