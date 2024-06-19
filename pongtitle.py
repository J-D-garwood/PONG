import pyglet
from pyglet.shapes import Rectangle

# Define the window size
window = pyglet.window.Window(640, 427)

# Define the square size
square_size = 10

# Define the letter patterns (5x5 grid for each letter)
letter_patterns = {
    'P': [
        "#####",
        "#...#",
        "#####",
        "#....",
        "#...."
    ],
    'O': [
        "#####",
        "#...#",
        "#...#",
        "#...#",
        "#####"
    ],
    'N': [
        "#...#",
        "##..#",
        "#.#.#",
        "#..##",
        "#...#"
    ],
    'G': [
        "#####",
        "#....",
        "#..##",
        "#...#",
        "#####"
    ]
}

def DRAW_TIT():
    total_width = 4 * 5 * square_size + 3 * square_size  # 4 letters with 5 squares each and 3 spaces between them
    start_x = (window.width - total_width) // 2
    start_y = ((window.height + 5 * square_size) // 2)+60
    
    x_offset = start_x
    for letter in "PONG":
        pattern = letter_patterns[letter]
        for y, row in enumerate(pattern):
            for x, col in enumerate(row):
                if col == '#':
                    x0 = x_offset + x * square_size
                    y0 = start_y - y * square_size
                    square = Rectangle(x0, y0, square_size, square_size, color=(255, 255, 255))
                    square.draw()
        x_offset += 6 * square_size  # Move to the next letter position (5 squares + 1 space)

@window.event
def on_draw():
    window.clear()
    
    # Calculate starting position to center the text
    total_width = 4 * 5 * square_size + 3 * square_size  # 4 letters with 5 squares each and 3 spaces between them
    start_x = (window.width - total_width) // 2
    start_y = (window.height + 5 * square_size) // 2
    
    x_offset = start_x
    for letter in "PONG":
        pattern = letter_patterns[letter]
        for y, row in enumerate(pattern):
            for x, col in enumerate(row):
                if col == '#':
                    x0 = x_offset + x * square_size
                    y0 = start_y - y * square_size
                    square = Rectangle(x0, y0, square_size, square_size, color=(255, 255, 255))
                    square.draw()
        x_offset += 6 * square_size  # Move to the next letter position (5 squares + 1 space)

if __name__ == '__main__':
    pyglet.app.run()
