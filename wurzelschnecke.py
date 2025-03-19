import math
import turtle

t = turtle.Turtle()

t.speed(0)

scale = 50
num_triangles = 20
origin = (0, 0)

# Zeichne das erste Dreieck:
# 1. Basis (erste Kathete): von origin zu (scale, 0)
base_point = (scale, 0)
t.penup()
t.goto(origin)
t.pendown()
t.goto(base_point)

# 2. Zweite Kathete: von base_point senkrecht nach oben (bis (scale, scale))
hypo_point = (scale, scale)
t.goto(hypo_point)

# 3. Hypotenuse: von origin zu hypo_point
# (Die Hypotenuse wurde bereits indirekt gezeichnet, aber wir zeichnen sie nochmal explizit für Konsistenz)
t.penup()
t.goto(origin)
t.pendown()
t.goto(hypo_point)

current_point = hypo_point

# Zeichne die weiteren Dreiecke
for n in range(2, num_triangles+1):
    # Bestimme den Winkel der aktuellen Hypotenuse
    theta = math.atan2(current_point[1], current_point[0])

    # Berechne das Ende der neuen Kathete, die senkrecht zur aktuellen Hypotenuse steht
    new_point = (
        current_point[0] + scale * math.cos(theta + math.pi/2),
        current_point[1] + scale * math.sin(theta + math.pi/2)
    )

    # Zeichne die Kathete (innere Verbindung) vom aktuellen Punkt zum neuen Punkt
    t.penup()
    t.goto(current_point)
    t.pendown()
    t.goto(new_point)

    # Zeichne die neue Hypotenuse vom Ursprung zum neuen Punkt
    t.penup()
    t.goto(origin)
    t.pendown()
    t.goto(new_point)

    # Aktualisiere current_point für das nächste Dreieck
    current_point = new_point

turtle.done()