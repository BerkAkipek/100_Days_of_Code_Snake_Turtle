# 20.12.2021
from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_body = Turtle(shape="square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        self.body.append(new_body)
    

    def reset(self):
        for segment in self.body:
            segment.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    
    def extend(self):
        self.add_segment(position=self.body[-1].position())


    def move(self):
        for num_segments in range(len(self.body) - 1, 0, -1):
            xcor = self.body[num_segments - 1].xcor()
            ycor = self.body[num_segments - 1].ycor()
            self.body[num_segments].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    
