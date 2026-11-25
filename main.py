import tkinter as tk
from game import BrickBlitzGame


def main():
    root = tk.Tk()
    BrickBlitzGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
