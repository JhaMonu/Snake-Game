from turtle import Turtle

STARTING_POSSITION = [(0,0),(-20,0),(-40,0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.new_square = []
        self.create_snake()

    def create_snake(self):
        for posstion in STARTING_POSSITION:
           self.add_segmernt(posstion)
    def add_segmernt(self, possition):
        tin = Turtle()
        tin.penup()
        tin.shape("square")
        tin.goto(possition)
        tin.color("white")
        self.new_square.append(tin)

    def exend_snake(self):
         self.add_segmernt(self.new_square[-1].position())

    def move(self):

        # how to move the sanke all part in a same direction
        for square in range(len(self.new_square) - 1, 0, -1):
            left = self.new_square[square - 1].xcor()
            right = self.new_square[square - 1].ycor()
            self.new_square[square].goto(left, right)
        self.new_square[0].forward(move_distance)
            # if self.new_square[0].xcor()== 290:


    def Up(self):
        if self.new_square[0].heading()!=DOWN:
            self.new_square[0].setheading(UP)
        else:
            pass
    def Down(self):
        if self.new_square[0].heading() != UP:
            self.new_square[0].setheading(DOWN)
        else:
            pass
    def Left(self):
        if self.new_square[0].heading() != RIGHT:
            self.new_square[0].setheading(LEFT)
        else:
            pass
    def Right(self):
        if self.new_square[0].heading() != LEFT:
            self.new_square[0].setheading(RIGHT)
        else:
            pass


