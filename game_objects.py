from abc import ABC, abstractmethod


# Abstraction: Abstract parent class defining essential behavior for all game objects
class GameObject(ABC):
    def __init__(self, canvas, item_id):
        self.canvas = canvas
        self.item_id = item_id

    def get_coords(self):
        return self.canvas.coords(self.item_id)

    @abstractmethod
    def move(self):
        pass


# Inheritance & Polymorphism: Paddle moves horizontally via player input
class Paddle(GameObject):
    def __init__(self, canvas, x, y, width=90, height=15):
        item_id = canvas.create_rectangle(
            x, y, x + width, y + height, fill="dodgerblue"
        )
        super().__init__(canvas, item_id)
        self.speed = 30
        self.dx = 0

    def set_direction(self, dx):
        self.dx = dx
        self.move()

    def move(self):
        coords = self.get_coords()
        if not coords:
            return
        if coords[0] + self.dx >= 0 and coords[2] + self.dx <= 600:
            self.canvas.move(self.item_id, self.dx, 0)
        self.dx = 0


# Inheritance & Polymorphism: Ball moves automatically and bounces off edges
class Ball(GameObject):
    def __init__(self, canvas, x, y, size=18):
        item_id = canvas.create_oval(x, y, x + size, y + size, fill="orange")
        super().__init__(canvas, item_id)
        self.dx = 4
        self.dy = -4

    def move(self):
        self.canvas.move(self.item_id, self.dx, self.dy)
        coords = self.get_coords()
        if coords[0] <= 0 or coords[2] >= 600:
            self.dx = -self.dx
        if coords[1] <= 0:
            self.dy = -self.dy

    def bounce_vertical(self):
        self.dy = -self.dy

    def reset(self, x, y, size=18):
        self.canvas.coords(self.item_id, x, y, x + size, y + size)
        self.dx = 4
        self.dy = -4


# Inheritance & Polymorphism: Brick remains stationary until destroyed
class Brick(GameObject):
    def __init__(self, canvas, x, y, width=70, height=20, color="crimson"):
        item_id = canvas.create_rectangle(
            x, y, x + width, y + height, fill=color, outline="white"
        )
        super().__init__(canvas, item_id)

    def move(self):
        pass  # Bricks stay fixed in place

    def destroy(self):
        self.canvas.delete(self.item_id)
