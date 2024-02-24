from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score= 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"score:{self.score}",  align="left",font=("Arial",15,"normal"))

    def increse_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()


