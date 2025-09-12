import os
import random
import sys
import time

def get_terminal_size():
    try:
        # Works on most Unix-like systems
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(rows), int(columns)
    except:
        # Fallback for Windows or error
        return 24, 80

class Star:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        # Start near the center
        self.x = self.width // 2
        self.y = self.height // 2
        # Random velocity outward from center
        angle = random.uniform(0, 2 * 3.14159)
        speed = random.uniform(0.1, 1.0)
        self.dx = speed * random.uniform(0.5, 1.5) * (1 if random.random() > 0.5 else -1)
        self.dy = speed * random.uniform(0.5, 1.5) * (1 if random.random() > 0.5 else -1)
        self.char = random.choice(['.', '*', '+'])

    def update(self):
        self.x += self.dx
        self.y += self.dy
        # If out of bounds, reset to center
        if not (0 < int(self.x) < self.width-1 and 0 < int(self.y) < self.height-1):
            self.reset()

    def position(self):
        return int(self.x), int(self.y)

def clear():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def draw(stars, width, height):
    # Draw all stars to a buffer
    buffer = [[' ' for _ in range(width)] for _ in range(height)]
    for star in stars:
        x, y = star.position()
        if 0 <= x < width and 0 <= y < height:
            buffer[y][x] = star.char
    # Print buffer
    for row in buffer:
        print(''.join(row))

def main():
    rows, cols = get_terminal_size()
    n_stars = (rows * cols) // 20  # density; adjust as desired
    stars = [Star(cols, rows) for _ in range(n_stars)]

    try:
        while True:
            clear()
            for star in stars:
                star.update()
            draw(stars, cols, rows)
            time.sleep(0.03)
    except KeyboardInterrupt:
        clear()
        print("Starfield animation exited.")

if __name__ == "__main__":
    main()
