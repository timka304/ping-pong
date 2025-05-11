from tkinter import *

screen = Tk()
screen.title("Ping Pong Game")
screen.geometry("800x600")
screen.config(bg="black")
screen.resizable(0, 0)

#canvas
canvas = Canvas(screen, width=800, height=600, bg="black")
canvas.pack()

# player 1 rectangle
player1 = canvas.create_rectangle(50, 250, 70, 350, fill="blue")
# player 2 rectangle
player2 = canvas.create_rectangle(730, 250, 750, 350, fill="red")

#ball
ball = canvas.create_oval(390, 290, 410, 310, fill="white")

# give movement to the ball
ball_speed_x = 7
ball_speed_y = 7

#use game states to make the game
# paused or unpaused
game_paused = False
# function to pause the game
def pause_game(event):
    global game_paused
    if game_paused:
        game_paused = False
        canvas.delete("pause")
    else:
        game_paused = True
        canvas.create_text(400, 300, text="Game Paused", fill="white", font=("Arial", 24))
        canvas.create_text(400, 350, text="Press Space to Start", fill="white", font=("Arial", 24))
# bind the p key to pause the game
screen.bind("<p>", pause_game)
# function to unpause the game
def unpause_game(event):
    global game_paused
    if game_paused:
        game_paused = False
        canvas.delete("pause")
    else:
        game_paused = True
        canvas.create_text(400, 300, text="Game Paused", fill="white", font=("Arial", 24))
        canvas.create_text(400, 350, text="Press Space to Start", fill="white", font=("Arial", 24))
# bind the u key to unpause the game
screen.bind("<u>", unpause_game)

# function to move the ball
def move_ball():
    global ball_speed_x, ball_speed_y
    canvas.move(ball, ball_speed_x, ball_speed_y)
    ball_pos = canvas.coords(ball)

    # check for collision with walls
    if ball_pos[0] <= 0 or ball_pos[2] >= 800:
        ball_speed_x = -ball_speed_x

    # check for collision with players
    if (ball_pos[0] <= 70 and ball_pos[1] >= canvas.coords(player1)[1] and ball_pos[3] <= canvas.coords(player1)[3]) or \
       (ball_pos[2] >= 730 and ball_pos[1] >= canvas.coords(player2)[1] and ball_pos[3] <= canvas.coords(player2)[3]):
        ball_speed_x = -ball_speed_x
    
    #give the ball vertical speed and allow it to bounce off the top and bottom walls
    if ball_pos[1] <= 0 or ball_pos[3] >= 600:
        ball_speed_y = -ball_speed_y

    # check if the ball is out of bounds of the screen
    if ball_pos[0] < 0 or ball_pos[2] > 800:
        canvas.coords(ball, 390, 290, 410, 310)
        ball_speed_x = -ball_speed_x
        ball_speed_y = 7 

    #if ball goes out of bounds and position is reset, pause the game until space bar is pressed
    if ball_pos[0] < 0 or ball_pos[2] > 800:
        ball_speed_x = 0
        ball_speed_y = 0
        canvas.coords(ball, 390, 290, 410, 310)
        canvas.create_text(400, 300, text="Game Paused", fill="white", font=("Arial", 24))
        canvas.create_text(400, 350, text="Press Space to Start", fill="white", font=("Arial", 24))
        return
    #remove the pause text if the ball is in play
    canvas.delete("pause")
    canvas.delete("score")

    

    screen.after(20, move_ball)

# move the ball on press of the space bar
def start_game(event):
    global ball_speed_x, ball_speed_y
    ball_speed_x = 7
    ball_speed_y = 7
    move_ball()
# bind space bar to start the game
screen.bind("<space>", start_game)


#give movement to the players
# function to move player 1
def move_player1(event):
    if event.keysym == "Up":
        canvas.move(player1, 0, -20)
    elif event.keysym == "Down":
        canvas.move(player1, 0, 20)

# function to move player 2
def move_player2(event):
    if event.keysym == "w":
        canvas.move(player2, 0, -20)
    elif event.keysym == "s":
        canvas.move(player2, 0, 20)

# bind keys to move players
# screen.bind_all("<KeyPress>", move_player1)
# screen.bind_all("<KeyPress>", move_player2)

screen.bind_all("<KeyPress-Up>", move_player1)
screen.bind_all("<KeyPress-Down>", move_player1)
screen.bind_all("<KeyPress-w>", move_player2)
screen.bind_all("<KeyPress-s>", move_player2)

#function to update the score
player1_score = 0
player2_score = 0
def update_score():
    global player1_score, player2_score
    score_text = f"Player 1: {player1_score}  Player 2: {player2_score}"
    canvas.delete("score")
    canvas.create_text(400, 50, text=score_text, fill="white", font=("Arial", 24))

# funtion so that when the ball touches the opposite wall, the score is updated by +1
def check_score():
    global player1_score, player2_score
    ball_pos = canvas.coords(ball)
    if ball_pos[0] < 0:
        player2_score += 1
        update_score()
        canvas.coords(ball, 390, 290, 410, 310)
    elif ball_pos[2] > 800:
        player1_score += 1
        update_score()
        canvas.coords(ball, 390, 290, 410, 310)

#function to display the score on the 
def display_score():
    global player1_score, player2_score
    score_text = f"Player 1: {player1_score}  Player 2: {player2_score}"
    canvas.create_text(400, 50, text=score_text, fill="white", font=("Arial", 24))

display_score()






# # function to move the ball
# def move_ball():
#     global ball_speed_x
#     canvas.move(ball, ball_speed_x, 0)
#     ball_pos = canvas.coords(ball)

#     # check for collision with walls
#     if ball_pos[0] <= 0 or ball_pos[2] >= 800:
#         ball_speed_x = -ball_speed_x

#     # check for collision with players
#     if (ball_pos[0] <= 70 and ball_pos[1] >= canvas.coords(player1)[1] and ball_pos[3] <= canvas.coords(player1)[3]) or \
#        (ball_pos[2] >= 730 and ball_pos[1] >= canvas.coords(player2)[1] and ball_pos[3] <= canvas.coords(player2)[3]):
#         ball_speed_x = -ball_speed_x
    
#     #give the ball vertical speed and allow it to bounce off the top and bottom walls
#     ball_speed_y = 3
#     canvas.move(ball, 0, ball_speed_y)
#     ball_pos = canvas.coords(ball)
#     if ball_pos[1] <= 0 or ball_pos[3] >= 600:
#         ball_speed_y = -ball_speed_y
#     # allow the ball to bounce off the top and bottom sides of the canvas
#     if ball_pos[1] <= 0 or ball_pos[3] >= 600:
#         ball_speed_y = -ball_speed_y
#     # check if the ball is out of bounds of the screen
#     # if the ball goes out of bounds, reset its position
#     if ball_pos[0] < 0 or ball_pos[2] > 800:
#         canvas.coords(ball, 390, 290, 410, 310)
#         ball_speed_x = -ball_speed_x
#         ball_speed_y = 3

#     # check if the ball is out of bounds of the screen
#     if ball_pos[0] < 0 or ball_pos[2] > 800:
#         canvas.coords(ball, 390, 290, 410, 310)
#         ball_speed_x = -ball_speed_x
#         ball_speed_y = 3    


    
    

#     screen.after(20, move_ball)

# # start moving the ball
# move_ball()


# # function to move player 1
# def move_player1(event):
#     if event.keysym == "Up":
#         canvas.move(player1, 0, -20)
#     elif event.keysym == "Down":
#         canvas.move(player1, 0, 20)

# # function to move player 2
# def move_player2(event):
#     if event.keysym == "w":
#         canvas.move(player2, 0, -20)
#     elif event.keysym == "s":
#         canvas.move(player2, 0, 20)

# # bind keys to move players
# screen.bind("<KeyPress>", move_player1)
# screen.bind("<KeyPress-w>", move_player2)








screen.mainloop()