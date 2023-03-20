# Obstacle Space with Clearance
# Ankur Chavan and Aditya Chaugule

import numpy as np
import tkinter as tk
import math

# Taking user input for clearance and robot radius
clearance = int(input("Please give the clearance for the obstacles:"))
radius = int(input("Please give the radius of the robot:"))

# Function for drawing original triangle
def triangle(base, height, xc,yc, angle=0):

    x1, y1 = xc+height, yc
    x2, y2 = xc, yc + base/2
    x3, y3 = xc, yc - base/2
    pts = [x1, y1, x2, y2, x3, y3]
    canvas.create_polygon(pts, fill='blue')
    return pts

# Function for drawing inflated triangle to consider clearance and robot radius
def triangle_inflated(base, height, xc, yc, angle=0, dist=0):

    x1, y1 = xc + height + dist, yc
    x2, y2 = xc - 0.8*dist, yc + base/2 + 2.5*dist
    x3, y3 = xc - 0.8*dist, yc - base/2 - 2.5*dist
    pts = [x1, y1, x2, y2, x3, y3]
    canvas.create_polygon(pts, fill='red')
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
    canvas.create_polygon(pts, fill="blue")
    return pts, p

# Function to draw inflated hexagon to consider clearance and robot radius
def polygon_inflated(sides, length, xc, yc,orient=np.pi/2):
    n = sides
    theta = 2*np.pi/n
    p = length*0.5/np.sin(theta/2)
    pts = []
    for i in range(n):
        x = xc + p*np.cos(theta*i + orient)
        pts.append(x)
        y = yc + p*np.sin(theta*i + orient)
        pts.append(y)
    canvas.create_polygon(pts, fill="red")
    return pts, p

root = tk.Tk()

wd = 600
ht = 250
canvas = tk.Canvas(root, width=wd, height=ht)
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

canvas.create_polygon(rect_obs1_c, fill='red')  # Inflated rectangle
canvas.create_polygon(rect_obs1, fill='blue')   # original Rectangle
canvas.create_polygon(rect_obs2_c, fill='red')  # Inflated rectangle
canvas.create_polygon(rect_obs2, fill='blue')   # original Rectangle
canvas.create_polygon(left_wall, fill='red')    # left wall
canvas.create_polygon(right_wall, fill='red')   # right wall
canvas.create_polygon(upper_wall, fill='red')   # upper wall
canvas.create_polygon(bottom_wall, fill='red')  # bottom wall

tri_obs_inflated = triangle_inflated(200, 50, 460, 125, angle=0, dist = distance )   # Inflated triangle
tri_obs = triangle(200,50, 460, 125)                                                 # original triangle
 
_, p = polygon_original(6, 75, 300, 125)  # original hexagon
length = ((distance + p)/p)*75
_, p0 = polygon_inflated(6, length, 300, 125)  # inlated hexagon

_, p = polygon_original(6, 75, 300, 125)  # original hexagon

root.mainloop()






    





