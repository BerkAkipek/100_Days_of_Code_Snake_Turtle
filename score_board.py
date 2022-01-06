from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./snake_turtle_01/data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.display_score()


    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_turtle_01/data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.display_score()


