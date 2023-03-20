import numpy as np
import tkinter as tk

def calculate_intersections(vertices):
    # Define equations for the sides of the rectangle
    eqs = [
        (1, 0, -vertices[0][0]),
        (-1, 0, vertices[1][0]),
        (0, 1, -vertices[0][1]),
        (0, -1, vertices[2][1])
    ]
    
    # Calculate the intersection points of the lines
    intersections = []
    for i in range(len(eqs)):
        for j in range(i+1, len(eqs)):
            a1, b1, c1 = eqs[i]
            a2, b2, c2 = eqs[j]
            det = a1*b2 - a2*b1
            if det != 0:
                x = (b2*c1 - b1*c2) / det
                y = (a1*c2 - a2*c1) / det
                intersections.append((x, y))
    
    return intersections

def draw_rectangle(canvas, vertices, clearance, fill_color):
    # Calculate the intersection points of the lines passing through the vertices
    intersections = calculate_intersections(vertices)

    # Calculate the new vertices for the clearance rectangle
    if clearance > 0:
        clear_vertices = vertices + [[-clearance, -clearance], [clearance, -clearance], [clearance, clearance], [-clearance, clearance]]
        print(clear_vertices)
    elif clearance < 0:
        clear_vertices = vertices + [[abs(clearance), abs(clearance)], [abs(clearance), -abs(clearance)], [-abs(clearance), -abs(clearance)], [-abs(clearance), abs(clearance)]]
        print(clear_vertices)
    else:
        clear_vertices = vertices

    # Calculate the intersection points of the lines passing through the clearance rectangle
    clear_intersections = calculate_intersections(clear_vertices)

    #################
    # Combine the original vertices and the intersection points
    points = vertices.tolist() + [list(point) for point in intersections]

    # Sort the points clockwise
    center = np.mean(points, axis=0)
    points = sorted(points, key=lambda point: np.arctan2(point[1]-center[1], point[0]-center[0]))

    # Create a polygon on the canvas with the points and fill the region with the specified color
    coords = sum(points, [])
    canvas.create_polygon(coords, fill=fill_color)
    #################


root = tk.Tk()
wd = 600
ht = 250
canvas = tk.Canvas(root, width=wd, height=ht)
canvas.pack()

# rect_vertices = np.array([[0, 0], [ht, 0], [ht, wd], [0, wd]])
rect_vertices = np.array([[0, 0], [0, ht], [wd, ht], [wd, 0]])
clearance = -5
color = "red"
fill_color = "blue"

draw_rectangle(canvas, rect_vertices, clearance, color)
# draw_rectangle(canvas, rect_vertices, 0, fill_color)

root.mainloop()

    # 
    # Draw lines passing through intersection points
    # for i in range(len(intersections)):
    #     for j in range(len(clear_intersections)):
    #         x1, y1 = intersections[i]
    #         x2, y2 = clear_intersections[j]
    #         canvas.create_line(x1, y1, x2, y2, fill=color, width=1)
    
    # Draw filled rectangle
    # poly = canvas.create_polygon(clear_vertices.flatten().tolist(), fill=color, outline="")
    
    # return poly