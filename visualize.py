# Obstacle Space with Clearance
# Ankur Chavan and Aditya Chaugule

import numpy as np
import tkinter as tk

clearance = 3
radius = 3

def points(node):
    x,y,th = node
    r = 5
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    pts = [x0,y0,x1,y1]
    return pts

# Function for drawing original triangle
def triangle(base, height, xc,yc, angle=0):

    x1, y1 = xc+height, yc
    x2, y2 = xc, yc + base/2
    x3, y3 = xc, yc - base/2
    pts = [x1, y1, x2, y2, x3, y3]
    # canvas.create_polygon(pts, fill='blue')
    return pts

# Function for drawing inflated triangle to consider clearance and robot radius
def triangle_inflated(base, height, xc, yc, angle=0, dist=0):

    x1, y1 = xc + height + dist, yc
    x2, y2 = xc - 0.8*dist, yc + base/2 + 2.5*dist
    x3, y3 = xc - 0.8*dist, yc - base/2 - 2.5*dist
    pts = [x1, y1, x2, y2, x3, y3]
    # canvas.create_polygon(pts, fill='red')
    return pts

# Function to draw hexagon
def polygon_original(sides, length, xc, yc,orient=np.pi/2):
    n = sides
    theta = 2*np.pi/n
    p = length*0.5/np.sin(theta/2)
    pts = []
    for i in range(n):
        x = xc + p*np.cos(theta*i + orient)
        pts.append(x)
        y = yc + p*np.sin(theta*i + orient)
        pts.append(y)
    # canvas.create_polygon(pts, fill="blue")
    return pts, p

# Function to draw inflated hexagon to consider clearance and robot radius
def polygon_inflated(sides, length, xc, yc,orient=np.pi/2, dist=0):
    n = sides
    theta = 2*np.pi/n
    p = length*0.5/np.sin(theta/2)
    pts = []
    for i in range(n):
        x = xc + p*np.cos(theta*i + orient)
        pts.append(x)
        y = yc + p*np.sin(theta*i + orient)
        pts.append(y)
    # canvas.create_polygon(pts, fill="red")
    return pts, p

def main(start, goal):
    root = tk.Tk()

    wd = 600
    ht = 250
    canvas = tk.Canvas(root, width=wd, height=ht,background='white')
    canvas.pack()

    distance = clearance + radius
    rect_obs1_c = [100 - distance, 100 + distance, 100 - distance, 0 - distance, 150 + distance, 0 - distance, 150 + distance, 100 + distance]
    rect_obs2_c = [100 - distance, 250 + distance, 100 - distance, 150 - distance, 150 + distance, 150 - distance, 150 + distance, 250 + distance]
    rect_obs2 = [100, 250, 100, 150, 150, 150, 150, 250]
    rect_obs1 = [100 , 100 , 100 , 0 , 150 , 0 , 150 , 100 ]

    left_wall = [0, 250, 0, 0, 0 + distance, 0, 0 + distance, 250]
    right_wall = [601 - distance, 250, 601 - distance, 0, 600, 0, 600, 250]
    upper_wall = [0, 0 + distance, 0, 0, 600, 0, 600, 0 + distance]
    bottom_wall = [0, 250, 0, 251 - distance, 600, 251 - distance, 600, 250]

    

    canvas.create_polygon(rect_obs1_c, fill='yellow')  # Inflated rectangle
    # canvas.create_polygon(rect_obs1, fill='blue')   # original Rectangle
    canvas.create_polygon(rect_obs2_c, fill='yellow')  # Inflated rectangle
    # canvas.create_polygon(rect_obs2, fill='blue')   # original Rectangle

    canvas.create_polygon(left_wall, fill='yellow')    # left wall
    canvas.create_polygon(right_wall, fill='yellow')   # right wall
    canvas.create_polygon(upper_wall, fill='yellow')   # upper wall
    canvas.create_polygon(bottom_wall, fill='yellow')  # bottom wall


    pts = triangle_inflated(200, 50, 460, 125, angle=0, dist = distance )   # Inflated triangle
    canvas.create_polygon(pts, fill='yellow')
    pts = triangle(200,50, 460, 125)                                                 # original triangle
    # canvas.create_polygon(pts, fill='blue')

    _, p = polygon_original(6, 75, 300, 125)  # original hexagon

    length = ((distance + p)/p)*75
    pts , p0 = polygon_inflated(6, length, 300, 125)  # inlated hexagon
    canvas.create_polygon(pts, fill='yellow')

    pts, p = polygon_original(6, 75, 300, 125)  # original hexagon
    # canvas.create_polygon(pts, fill='blue')

    pts = points(start)
    canvas.create_oval(pts, fill='green')
    pts = points(goal)
    canvas.create_oval(pts, fill='green')
    # Add checks for clearance space similar to dijkstra
    return root, canvas

if __name__ == "__main__":
    main()




    




