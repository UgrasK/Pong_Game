from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Chiller", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
