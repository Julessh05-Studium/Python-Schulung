import turtle

def generate_dragon_curve(iterations):
    # Start with a simple forward command
    instructions = "F"
    for _ in range(iterations):
        # For each iteration, append an 'R' and the inverted reverse of the current instructions
        instructions = instructions + "R" + ''.join('L' if char == 'R' else 'R' for char in instructions[::-1])
    return instructions


def draw_dragon_curve(instructions, length):
    for command in instructions:
        if command == "F":
            turtle.forward(length)
        elif command == "L":
            turtle.left(90)
        elif command == "R":
            turtle.right(90)


def main():
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.color("cyan")

    # Adjust these parameters to change the fractal's detail and scale
    iterations = 10  # Higher iterations produce a more detailed dragon curve
    length = 5       # Length of each step; adjust as needed

    instructions = generate_dragon_curve(iterations)

    # Reposition the turtle for a better view
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()

    draw_dragon_curve(instructions, length)
    turtle.done()


if __name__ == '__main__':
    main()
