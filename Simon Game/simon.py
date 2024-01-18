#Simon Game
import tkinter
from tkinter import StringVar, ACTIVE, NORMAL, DISABLED
import random

#Window
root = tkinter.Tk()
root.title("Simon Game")
root.iconbitmap("simon.ico")
root.geometry("400x400")
root.resizable(0,0)

#Fonts and Colors
game_font1 = ("Arial", 12)
game_font2 = ("Arial", 8)
white = "#c6cbcd"
white_light = "#fbfcfc"
magenta = "#90189e"
magenta_light = "#f802f9"
cyan = "#078384"
cyan_light = "#00fafa"
yellow = "#9ba00f"
yellow_light = "#f7f801"
root_color = "#2eb4c6"
game_color = "#f6f7f8"
root.config(bg=root_color)

#Global variables for the game
time = 500
score = 0
game_sequence = []
player_sequence = []

# THE FUNCTIONS

def pick_sequences():
    """Pick the next value in the sequence.  Do not allow for repeated values."""
    while True:
        value = random.randint(1,4)
        #Sequence is size 0, so take the value regardless
        if len(game_sequence) == 0:
            game_sequence.append(value)
            break
        #Make sure the current value is not the same as the lat value in the sequence
        elif value != game_sequence[-1]:
            game_sequence.append(value)
            break

        #Now that the value is added tı the sequence, play the sequence
    play_sequence()

def play_sequence():
    #Change button label
    change_label("Playing!")

    delay = 0
    for value in game_sequence:
        if value == 1:
            root.after(delay, lambda:animate(white_button))
        elif value == 2:
            root.after(delay, lambda:animate(magenta_button))
        elif value == 3:
            root.after(delay, lambda:animate(cyan_button))
        elif value == 4:
            root.after(delay, lambda:animate(yellow_button))
    
        delay += time

def animate(button):
    """Animate a given button by chaining its color"""
    button.config(state = ACTIVE)
    root.after(time, lambda:button.config(state = NORMAL))

def change_label(message):
    start_button.config(text=message)

    if message == "Wrong!":
        start_button.config(bg="red")
    else:
        start_button.config(bg=game_color)

def set_difficulty():
    """Use radio buttons to set difficulty"""
    global time

    if difficulty.get() == "Easy":
        time = 1000
    elif difficulty.get() == "Medium":
        time = 500
    else:
        tiöe = 200

def press(value):
    """Simulate pressing a button for player"""
    player_sequence.append(value)

    if len(player_sequence) == len(game_sequence):
        check_round()

def check_round():
    """Determine if the player entered the correct sequence of button presses for a round"""
    global player_sequence
    global game_sequence
    global score

    if player_sequence == game_sequence:
        change_label("Correct")
        score += len(player_sequence) + int(1000/time)
        root.after(500, pick_sequences)
    else:
        change_label("Wrong!")
        score = 0
        disable()
        # The game is over , so wipe the game sequence
        game_sequence = []
        root.after(2000, lambda:change_label("New Game"))

    #Regardless of win or lose for a round, wipe the players sequence
    player_sequence = []

    #Update score label
    score_label.config(text="Score: " + str(score))

def disable():
    """Disable all the buttons so they can't accidentally be pressed"""
    white_button.config(state=DISABLED)
    magenta_button.config(state=DISABLED)
    cyan_button.config(state=DISABLED)
    yellow_button.config(state=DISABLED)

def enable():
    """enable all the buttons to start the game and pick the first value in the sequence"""
    white_button.config(state=NORMAL)
    magenta_button.config(state=NORMAL)
    cyan_button.config(state=NORMAL)
    yellow_button.config(state=NORMAL)

    #Pick a  value
    pick_sequences()

#Define Layout and Make Frames
info_frame = tkinter.Frame(root, bg = root_color)
game_frame = tkinter.LabelFrame(root, bg = game_color)
info_frame.pack(pady=(10,20))
game_frame.pack()

#Layout for the into frame
start_button = tkinter.Button(info_frame, text = "New Game", font = game_font1, bg = game_color, command= enable)
score_label = tkinter.Label(info_frame, text = "Score: "+ str(score), font = game_font1,bg=root_color)
start_button.grid(row=0,column=0,padx=20,ipadx=30)
score_label.grid(row=0, column=1)

#Layout for game frame
#Game Buttons
white_button = tkinter.Button(game_frame, bg=white, activebackground=white_light, borderwidth=3, state = DISABLED, command=lambda:press(1))
magenta_button = tkinter.Button(game_frame, bg=magenta, activebackground=magenta_light, borderwidth=3, state = DISABLED, command=lambda:press(2))
cyan_button = tkinter.Button(game_frame, bg=cyan, activebackground=cyan_light, borderwidth=3, state = DISABLED, command=lambda:press(3))
yellow_button = tkinter.Button(game_frame, bg=yellow, activebackground=yellow_light, borderwidth=3, state = DISABLED, command=lambda:press(4))

white_button.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipadx=60,ipady=50)
magenta_button.grid(row=0,column=2,columnspan=2,padx=10,pady=10,ipadx=60,ipady=50)
cyan_button.grid(row=1,column=0,columnspan=2,padx=10,pady=10,ipadx=60,ipady=50)
yellow_button.grid(row=1,column=2,columnspan=2,padx=10,pady=10,ipadx=60,ipady=50)

#Radio Buttons
difficulty = StringVar()
difficulty.set("Medium")
tkinter.Label(game_frame, text = "Difficulty: ", font=game_font2,bg=game_color).grid(row=2,column=0)
tkinter.Radiobutton(game_frame, text = "Easy", variable=difficulty, value="Easy",font=game_font2, bg=game_color, command=set_difficulty).grid(row=2,column=1)
tkinter.Radiobutton(game_frame, text = "Medium", variable=difficulty, value="Medium",font=game_font2, bg=game_color, command=set_difficulty).grid(row=2,column=2)
tkinter.Radiobutton(game_frame, text = "Hard", variable=difficulty, value="Hard",font=game_font2, bg=game_color, command=set_difficulty).grid(row=2,column=3)




#Run the Code
root.mainloop()
