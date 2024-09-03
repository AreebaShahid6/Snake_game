from turtle import Turtle

Alignment = "center"
Font = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_value = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score_value}', align=Alignment, font=Font)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align=Alignment, font=Font)

    def increase_score(self):
        self.score_value += 1
        self.update_score()


         





