import tkinter as tk
from game_objects import Paddle, Ball, Brick
from score_manager import ScoreManager


class BrickBlitzGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Brick Blitz")
        self.width = 600
        self.height = 450
        self.running = False

        self.canvas = tk.Canvas(
            root, width=self.width, height=self.height, bg="black"
        )
        self.canvas.pack()

        self.score_manager = ScoreManager(initial_lives=3)
        self.paddle = Paddle(self.canvas, 255, 410)
        self.ball = Ball(self.canvas, 290, 385)
        self.bricks = []

        self.score_text = self.canvas.create_text(
            70, 20, text="Score: 0", fill="white", font=("Arial", 14, "bold")
        )
        self.lives_text = self.canvas.create_text(
            530, 20, text="Lives: 3", fill="white", font=("Arial", 14, "bold")
        )
        self.message_text = self.canvas.create_text(
            self.width / 2,
            self.height / 2,
            text="Press SPACE to Start\nUse Left/Right Arrows to Move",
            fill="yellow",
            font=("Arial", 18, "bold"),
            justify="center",
        )

        self.create_bricks()
        self.bind_controls()

    def create_bricks(self):
        colors = ["crimson", "orange", "gold", "limegreen"]
        for row in range(4):
            for col in range(7):
                x = 25 + col * 80
                y = 50 + row * 30
                brick = Brick(self.canvas, x, y, color=colors[row])
                self.bricks.append(brick)

    def bind_controls(self):
        self.root.bind(
            "<Left>", lambda e: self.paddle.set_direction(-self.paddle.speed)
        )
        self.root.bind(
            "<Right>", lambda e: self.paddle.set_direction(self.paddle.speed)
        )
        self.root.bind("<space>", self.start_game)

    def start_game(self, event=None):
        if not self.running and not self.score_manager.is_game_over() and self.bricks:
            self.running = True
            self.canvas.itemconfig(self.message_text, text="")
            self.game_loop()

    def check_overlap(self, c1, c2):
        return (
            c1[2] >= c2[0]
            and c1[0] <= c2[2]
            and c1[3] >= c2[1]
            and c1[1] <= c2[3]
        )

    def game_loop(self):
        if not self.running:
            return

        # Polymorphism: calling move() on different GameObject subclasses
        for obj in [self.paddle, self.ball]:
            obj.move()

        ball_coords = self.ball.get_coords()
        paddle_coords = self.paddle.get_coords()

        # Paddle collision
        if self.check_overlap(ball_coords, paddle_coords) and self.ball.dy > 0:
            self.ball.bounce_vertical()

        # Brick collision
        for brick in self.bricks[:]:
            if self.check_overlap(ball_coords, brick.get_coords()):
                brick.destroy()
                self.bricks.remove(brick)
                self.ball.bounce_vertical()
                self.score_manager.add_points(10)
                self.canvas.itemconfig(
                    self.score_text,
                    text=f"Score: {self.score_manager.get_score()}",
                )
                break

        # Ball falls below paddle
        if ball_coords[3] >= self.height:
            self.score_manager.lose_life()
            self.canvas.itemconfig(
                self.lives_text,
                text=f"Lives: {self.score_manager.get_lives()}",
            )
            if self.score_manager.is_game_over():
                self.running = False
                self.canvas.itemconfig(
                    self.message_text, text="GAME OVER!", fill="red"
                )
                return
            self.ball.reset(290, 385)

        # Win condition
        if not self.bricks:
            self.running = False
            self.canvas.itemconfig(
                self.message_text, text="YOU WIN!", fill="limegreen"
            )
            return

        self.root.after(20, self.game_loop)
