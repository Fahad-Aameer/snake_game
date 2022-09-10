from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.my_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.my_score}", align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.my_score += 1
        self.clear()
        self.write(f"Score: {self.my_score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=("Arial", 20, "normal"))
